from . import models
from rest_framework.serializers import IntegerField, FloatField, ListField
from dynamic_rest import serializers
from chembl import serializers as chembl_serializers


class ActivitiesSerializer(serializers.DynamicModelSerializer):
    target = serializers.DynamicRelationField('TargetSerializer')
    molecule = serializers.DynamicRelationField('MoleculeSerializer')

    class Meta:
        model = models.Activities
        exclude = []


class MoleculeHierarchySerializer(serializers.DynamicModelSerializer):
    molregno = serializers.DynamicRelationField(chembl_serializers.MoleculeDictionarySerializer, embed=True)
    parent = serializers.DynamicRelationField(chembl_serializers.MoleculeDictionarySerializer, embed=True)

    class Meta:
        model = models.MoleculeHierarchy
        exclude = []


class MoleculeSerializer(serializers.DynamicModelSerializer):
    molregno = serializers.DynamicRelationField(chembl_serializers.MoleculeDictionarySerializer, embed=True)
    scaffold = serializers.DynamicRelationField('ScaffoldSerializer', embed=True, deferred=True)

    class Meta:
        model = models.Molecule
        exclude = ['ffp2', 'mfp2', 'structure', 'torsionbv', 'atompairbv']


class ScaffoldSerializer(serializers.DynamicModelSerializer):
    molecule_set = serializers.DynamicRelationField('MoleculeSerializer', many=True)

    class Meta:
        model = models.Scaffold
        exclude = ['ffp2', 'mfp2', 'structure', 'torsionbv', 'atompairbv']


class ScaffoldActivitiesSerializer(serializers.DynamicModelSerializer):
    target = serializers.DynamicRelationField('TargetSerializer')
    scaffold = serializers.DynamicRelationField(ScaffoldSerializer)

    class Meta:
        model = models.ScaffoldActivities
        exclude = []


class TargetSerializer(serializers.DynamicModelSerializer):
    tid = serializers.DynamicRelationField(chembl_serializers.TargetDictionarySerializer, embed=True)

    class Meta:
        model = models.Target
        exclude = []


class MoleculeInteraction(serializers.DynamicModelSerializer):
    first_molecule = serializers.DynamicRelationField(MoleculeSerializer)
    second_molecule = serializers.DynamicRelationField(MoleculeSerializer)

    class Meta:
        model = models.MoleculeInteraction
        exclude = ['min', 'max', 'median']


class TargetNetworkSerializer(serializers.DynamicModelSerializer):
    first_target = serializers.DynamicRelationField(TargetSerializer)
    second_target = serializers.DynamicRelationField(TargetSerializer)

    class Meta:
        model = models.TargetNetwork
        exclude = ['min', 'max', 'median']


class TargetScaffoldNetworkSerializer(serializers.DynamicModelSerializer):
    first_target = serializers.DynamicRelationField(TargetSerializer)
    second_target = serializers.DynamicRelationField(TargetSerializer)

    class Meta:
        model = models.TargetScaffoldNetwork
        exclude = ['min', 'max', 'median']


# class TargetNetworkSerializer(serializers.DynamicEphemeralSerializer):
#     class Meta:
#         name = 'target-network'
#
#     first_target = serializers.DynamicRelationField(TargetSerializer, embed=True)
#     second_target = serializers.DynamicRelationField(TargetSerializer, embed=True)
#     activity_list = ListField(child=FloatField(min_value=0, max_value=99))


# class TargetScaffoldNetworkSerializer(serializers.DynamicEphemeralSerializer):
#     class Meta:
#         name = 'target-scaffold-network'
#
#     first_target = serializers.DynamicRelationField(TargetSerializer, embed=True)
#     second_target = serializers.DynamicRelationField(TargetSerializer, embed=True)
#     activity_list = ListField(child=FloatField(min_value=0, max_value=99))


class MMPSerializer(serializers.DynamicModelSerializer):
    target = serializers.DynamicRelationField(chembl_serializers.TargetDictionarySerializer)
    RHAssay = serializers.DynamicRelationField(chembl_serializers.AssaysSerializer)
    LHAssay = serializers.DynamicRelationField(chembl_serializers.AssaysSerializer)
    RHMol = serializers.DynamicRelationField(chembl_serializers.MoleculeDictionarySerializer)
    LHMol = serializers.DynamicRelationField(chembl_serializers.MoleculeDictionarySerializer)

    class Meta:
        model = models.MMP
        exclude = []


class KEGGDiseaseClassSerializer(serializers.DynamicModelSerializer):
    parent = serializers.DynamicRelationField('KEGGDiseaseClassSerializer')
    mapping_counts = IntegerField(read_only=True)

    class Meta:
        model = models.KEGGDiseaseClass
        exclude = ['rght', 'lft']



class KEGGDiseaseSerializer(serializers.DynamicModelSerializer):
    kegg_class = serializers.DynamicRelationField(KEGGDiseaseClassSerializer, embed=True)
    chembl_mappings = serializers.DynamicRelationField(chembl_serializers.ComponentSequencesSerializer, many=True)

    class Meta:
        model = models.KEGGDisease
        exclude = []


class ICDSerializer(serializers.DynamicModelSerializer):
    chembl_mappings = serializers.DynamicRelationField(chembl_serializers.TargetDictionarySerializer, many=True)

    class Meta:
        model = models.ICD
        exclude = []