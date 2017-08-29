
from . import models
from dynamic_rest import serializers


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


