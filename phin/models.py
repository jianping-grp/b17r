from __future__ import unicode_literals

from chembl import models as chembl_models
from django.db import models, connection
from django.db.models import Q, Count
from django.contrib.postgres.fields import ArrayField
from django_rdkit.models import *
from django_rdkit.models.fields import MolField, BfpField
from django_rdkit.config import config as django_rdk_conf
from sql_helper import *
import pandas as pd


class ScaffoldManager(models.Manager):

    def structure_search(self, smiles, similarity):
        search_mfp2 = MORGANBV_FP(Value(smiles))
        django_rdk_conf.tanimoto_threshold = similarity
        queryset = super(ScaffoldManager, self).get_queryset().filter(mfp2__tanimoto=search_mfp2)
        queryset = queryset.annotate(similarity=TANIMOTO_SML('mfp2', search_mfp2))
        queryset = queryset.order_by('-similarity')
        return queryset


class MoleculeManager(models.Manager):

    def structure_search(self, smiles, similarity):
        search_mfp2 = MORGANBV_FP(Value(smiles))
        django_rdk_conf.tanimoto_threshold = similarity
        queryset = super(MoleculeManager, self).get_queryset().filter(mfp2__tanimoto=search_mfp2)
        queryset = queryset.annotate(similarity=TANIMOTO_SML('mfp2', search_mfp2))
        queryset = queryset.order_by('-similarity')
        return queryset


class Scaffold(models.Model):

    objects = ScaffoldManager()

    scaffold_id = models.BigAutoField(primary_key=True)
    structure = MolField(null=True, blank=True)
    smiles = models.CharField(max_length=4000, blank=True, null=True)
    torsionbv = BfpField(null=True)
    atompairbv = BfpField(null=True)
    mfp2 = BfpField(null=True, db_index=True)
    ffp2 = BfpField(null=True)


class Molecule(models.Model):

    objects = MoleculeManager()

    # only parent molecule of ChEMBL used here
    mol_id = models.BigAutoField(primary_key=True)
    molregno = models.OneToOneField(
        chembl_models.MoleculeDictionary,
        related_name='chembl_molecule'
    )
    scaffold = models.ForeignKey(Scaffold, null=True)
    structure = MolField(null=True, blank=True)
    torsionbv = BfpField(null=True)
    atompairbv = BfpField(null=True)
    mfp2 = BfpField(null=True, db_index=True)
    ffp2 = BfpField(null=True)
    # todo add fp index

    def get_common_activities(self, other_molecule_id):
        """
        :return:
        """

        with connection.cursor() as cursor:
            cursor.execute(MOLECULE_COMMON_ACTIVITIES, (self.mol_id, other_molecule_id))
            rows = cursor.fetchall()
        return pd.DataFrame(rows, columns=['target_id', 'min', 'max', 'mean', 'median'])


class Target(models.Model):
    target_id = models.BigAutoField(primary_key=True)
    tid = models.OneToOneField(
        chembl_models.TargetDictionary,
        related_name='chembl_target'
    )

    def get_target_interaction(self, activity_type='mean'):
        with connection.cursor() as cursor:
            cursor.execute(TARGET_INTERACTION.format(activity_type, self.target_id))
            data = pd.DataFrame(cursor.fetchall(), columns=['pk', 'first_target', 'second_target', 'activity_list'])
            # print data
            return data

    def get_related_targets(self):
        return TargetInteraction.objects.get_target_interaction(self.target_id) \
            .distinct().values('first_target', 'second_target')

    # related_targets = property(_get_related_targets)

    def _get_scaffold_activites(self):
        """
        
        :return: 
        """
        with connection.cursor() as cursor:
            cursor.execute(TARGET_SCAFFOLD_ACTIVITIES, (self.target_id,))
            return pd.DataFrame(cursor.fetchall(), columns=['min', 'mean', 'max', 'median', 'count', 'scaffold_id'])

    def get_activities_pchembl_list(self):
        """
        
        :return: [(molregno, pchembl, parent_molregno)...] 
        """
        with connection.cursor() as cursor:
            cursor.execute(TARGET_PCHEMBL_ALL, (self.tid_id,))
            rows = cursor.fetchall()
        return pd.DataFrame(rows, columns=['molregno', 'pchembl_value', 'parent_molregno'])

    def get_common_activities(self, other_target):
        """
        
        :return: 
        """

        with connection.cursor() as cursor:
            cursor.execute(TARGET_COMMON_ACTIVITY, (self.target_id, other_target.target_id))
            rows = cursor.fetchall()
        return pd.DataFrame(rows, columns=['molecule_id', 'min', 'max', 'mean', 'median'])

    def _get_common_scaffold_activities(self, other_target):
        with connection.cursor() as cursor:
            cursor.execute(TARGET_COMMON_SCAFFOLD_ACTIVITY, (self.target_id, other_target.target_id))
            return pd.DataFrame(cursor.fetchall(), columns=['scaffold_id', 'min', 'max', 'mean', 'median'])


class Activities(models.Model):
    # aggregation activities of max, min, mean and median pchembl value
    act_id = models.BigAutoField(primary_key=True)
    molecule = models.ForeignKey(Molecule)
    target = models.ForeignKey(Target)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    mean = models.FloatField(blank=True, null=True)
    median = models.FloatField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    # todo: activity type


class ScaffoldActivities(models.Model):
    # aggregation activities of max, min, mean and median pchembl value
    act_id = models.BigAutoField(primary_key=True)
    scaffold = models.ForeignKey(Scaffold)
    target = models.ForeignKey(Target)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    mean = models.FloatField(blank=True, null=True)
    median = models.FloatField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)


class TargetInteractionManager(models.Manager):
    # def get_target_interaction(self):
    def get_target_interaction_agg(self, target_id):
        return super(TargetInteractionManager, self).raw(TARGET_INTERACTION.format('mean', target_id))

    def get_target_interaction(self, target_id):
        return super(TargetInteractionManager, self).get_queryset().filter(
            Q(first_target_id=target_id) | Q(second_target_id=target_id)
        )

class MoleculeInteraction(models.Model):
    """
    first_molecule.molregno > second_molecule.molregno
    """
    moli_id = models.BigAutoField(primary_key=True, db_index=True)
    first_molecule = models.ForeignKey(Molecule, related_name='as_first', db_index=True)
    second_molecule = models.ForeignKey(Molecule, related_name='as_second', db_index=True)
    target = ArrayField(models.BigIntegerField(), blank=True, null=True)
    min = ArrayField(models.FloatField(), blank=True, null=True)
    max = ArrayField(models.FloatField(), blank=True, null=True)
    mean = ArrayField(models.FloatField(), blank=True, null=True)
    median = ArrayField(models.FloatField(), blank=True, null=True)


class TargetInteraction(models.Model):
    """
    first_target.tid_id > second_target.tid_id
    """
    ti_id = models.BigAutoField(primary_key=True, db_index=True)
    first_target = models.ForeignKey(Target, related_name='as_first', db_index=True)
    second_target = models.ForeignKey(Target, related_name='as_second', db_index=True)
    molecule = models.ForeignKey(Molecule, db_index=True)
    # MIN(min, max, mean, and media activity value) of this two targets
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    mean = models.FloatField(blank=True, null=True)
    median = models.FloatField(blank=True, null=True)

    objects = TargetInteractionManager()


class TargetScaffoldInteraction(models.Model):
    """
    first_target.tid_id > second_target.tid_id
    """
    ti_id = models.BigAutoField(primary_key=True, db_index=True)
    first_target = models.ForeignKey(Target, related_name='as_scaffold_first', db_index=True)
    second_target = models.ForeignKey(Target, related_name='as_scaffold_second', db_index=True)
    scaffold = models.ForeignKey(Scaffold, db_index=True)
    # MIN(min, max, mean, and media activity value) of this two targets
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    mean = models.FloatField(blank=True, null=True)
    median = models.FloatField(blank=True, null=True)


class MMP(models.Model):
    target = models.ForeignKey(chembl_models.TargetDictionary, db_index=True)
    RHMol = models.ForeignKey(chembl_models.MoleculeDictionary, related_name="right_hand_mol", db_index=True)
    LHMol = models.ForeignKey(chembl_models.MoleculeDictionary, related_name="left_hand_mol", db_index=True)
    RHAct = models.FloatField()
    LHAct = models.FloatField()
    RHAssay = models.ForeignKey(chembl_models.Assays, related_name='right_hand_assay', db_index=True)
    LHAssay = models.ForeignKey(chembl_models.Assays, related_name='left_hand_assay', db_index=True)
    transform = models.CharField(max_length=2048)
    core = models.CharField(max_length=2048)
