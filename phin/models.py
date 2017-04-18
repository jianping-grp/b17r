from __future__ import unicode_literals

from chembl import models as chembl_models
from django.db import models, connection
from django_rdkit.models.fields import MolField, BfpField
from sql_helper import *

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

    def get_activities_pchembl_list(self):
        """
        
        :return: [(molregno, pchembl, parent_molregno)...] 
        """
        with connection.cursor() as cursor:
            cursor = connection.cursor()
            cursor.execute(TARGET_PCHEMBL_ALL, (self.tid_id,))
            rows = cursor.fetchall()
        return rows



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


class TargetInteraction(models.Model):
    first_target = models.ForeignKey(Target, related_name='as_first')
    second_target = models.ForeignKey(Target, related_name='as_second')
    molecule = models.ForeignKey(Molecule)
    # MIN(min, max, mean, and media activity value) of this two targets
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    mean = models.FloatField(blank=True, null=True)
    median = models.FloatField(blank=True, null=True)
