from . import models
from rest_framework.serializers import IntegerField, FloatField, ListField
from dynamic_rest import serializers
from chembl import serializers as chembl_serializers


class ActivitiesSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Activities
        exclude = []


class MoleculeSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Molecule
        exclude = []


class ScaffoldSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Scaffold
        exclude = []


class ScaffoldActivitiesSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ScaffoldActivities
        exclude = []


class TargetSerializer(serializers.DynamicModelSerializer):
    tid = serializers.DynamicRelationField(chembl_serializers.TargetDictionarySerializer, embed=True)

    class Meta:
        model = models.Target
        exclude = []


class TargetInteractionSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.TargetInteraction
        exclude = []


class TargetScaffoldInteractionSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.TargetScaffoldInteraction
        exclude = []


class TargetNetworkSerializer(serializers.DynamicEphemeralSerializer):
    class Meta:
        name = 'target-network'

    first_target = serializers.DynamicRelationField(TargetSerializer, embed=True)
    second_target = serializers.DynamicRelationField(TargetSerializer, embed=True)
    activity_list = ListField(child=FloatField(min_value=0, max_value=99))


class MMPSerializer(serializers.DynamicModelSerializer):
    target = serializers.DynamicRelationField(chembl_serializers.TargetDictionarySerializer)
    RHAssay = serializers.DynamicRelationField(chembl_serializers.AssaysSerializer)
    LHAssay = serializers.DynamicRelationField(chembl_serializers.AssaysSerializer)
    RHMol = serializers.DynamicRelationField(chembl_serializers.MoleculeDictionarySerializer)
    LHMol = serializers.DynamicRelationField(chembl_serializers.MoleculeDictionarySerializer)
    class Meta:
        model = models.MMP
        exclude = []
