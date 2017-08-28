from . import models

from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField
from dynamic_rest.fields import CountField


class ActionTypeSerializer(DynamicModelSerializer):
    class Meta:
        model = models.ActionType
        exclude = []


class ActivitiesSerializer(DynamicModelSerializer):
    class Meta:
        model = models.Activities
        exclude = []


class ActivityStdsLookupSerializer(DynamicModelSerializer):
    class Meta:
        model = models.ActivityStdsLookup
        exclude = []


class AssayParametersSerializer(DynamicModelSerializer):
    class Meta:
        model = models.AssayParameters
        exclude = []


class AssayTypeSerializer(DynamicModelSerializer):
    class Meta:
        model = models.AssayType
        exclude = []


class AssaysSerializer(DynamicModelSerializer):
    class Meta:
        model = models.Assays
        exclude = []


class AtcClassificationSerializer(DynamicModelSerializer):
    class Meta:
        model = models.AtcClassification
        exclude = []


class BindingSitesSerializer(DynamicModelSerializer):
    class Meta:
        model = models.BindingSites
        exclude = []


class BioComponentSequencesSerializer(DynamicModelSerializer):
    class Meta:
        model = models.BioComponentSequences
        exclude = []


class BioassayOntologySerializer(DynamicModelSerializer):
    class Meta:
        model = models.BioassayOntology
        exclude = []


class BiotherapeuticComponentsSerializer(DynamicModelSerializer):
    class Meta:
        model = models.BiotherapeuticComponents
        exclude = []


class BiotherapeuticsSerializer(DynamicModelSerializer):
    class Meta:
        model = models.Biotherapeutics
        exclude = []


class CellDictionarySerializer(DynamicModelSerializer):
    class Meta:
        model = models.CellDictionary
        exclude = []


class ChemblIdLookupSerializer(DynamicModelSerializer):
    class Meta:
        model = models.ChemblIdLookup
        exclude = []


class ComponentClassSerializer(DynamicModelSerializer):
    class Meta:
        model = models.ComponentClass
        exclude = []


class ComponentDomainsSerializer(DynamicModelSerializer):
    class Meta:
        model = models.ComponentDomains
        exclude = []


class ComponentGoSerializer(DynamicModelSerializer):
    class Meta:
        model = models.ComponentGo
        exclude = []