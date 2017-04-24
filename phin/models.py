from __future__ import unicode_literals

from chembl import models as chembl_models
from django.db import models, connection
from django_rdkit.models.fields import MolField, BfpField
from sql_helper import *
import pandas as pd


class Scaffold(models.Model):
    scaffold_id = models.BigAutoField(primary_key=True)
    structure = MolField(null=True, blank=True)
    smiles = models.CharField(max_length=4000, blank=True, null=True)
    torsionbv = BfpField(null=True)
    atompairbv = BfpField(null=True)
    mfp2 = BfpField(null=True)
    ffp2 = BfpField(null=True)


class Molecule(models.Model):
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
    mfp2 = BfpField(null=True)
    ffp2 = BfpField(null=True)
    # todo add fp index


class Target(models.Model):
    target_id = models.BigAutoField(primary_key=True)
    tid = models.OneToOneField(
        chembl_models.TargetDictionary,
        related_name='chembl_target'
    )

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


