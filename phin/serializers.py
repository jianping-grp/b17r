
from . import models
from rest_framework.serializers import IntegerField, ListField
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


class TargetNetworkSerializer(serializers.DynamicModelSerializer):
    activity_list = ListField(child=IntegerField(min_value=0, max_value=99))
    class Meta:
        model = models.TargetInteraction
        include = [
            'first_target', 
            'second_target',
            'activity_list'
        ]