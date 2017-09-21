from rest_framework.fields import IntegerField

from . import models
from dynamic_rest import serializers


class ActionTypeSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ActionType
        exclude = []


class ActivitiesSerializer(serializers.DynamicModelSerializer):
    assay = serializers.DynamicRelationField('AssaysSerializer')
    molregno = serializers.DynamicRelationField('CompoundStructuresSerializer', embed=True)

    class Meta:
        model = models.Activities
        exclude = ['molregno']


class ActivityStdsLookupSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ActivityStdsLookup
        exclude = []


class AssayParametersSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.AssayParameters
        exclude = []


class AssayTypeSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.AssayType
        exclude = []


class AssaysSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Assays
        exclude = []


class AtcClassificationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.AtcClassification
        exclude = []


class BindingSitesSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.BindingSites
        exclude = []


class BioComponentSequencesSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.BioComponentSequences
        exclude = []


class BioassayOntologySerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.BioassayOntology
        exclude = []


class BiotherapeuticComponentsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.BiotherapeuticComponents
        exclude = []


class BiotherapeuticsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Biotherapeutics
        exclude = []


class CellDictionarySerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.CellDictionary
        exclude = []


class ChemblIdLookupSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ChemblIdLookup
        exclude = []


class ComponentClassSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ComponentClass
        exclude = []


class ComponentDomainsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ComponentDomains
        exclude = []


class ComponentGoSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ComponentGo
        exclude = []


class ComponentSequencesSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ComponentSequences
        exclude = []


class ComponentSynonymsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ComponentSynonyms
        exclude = []


class CompoundPropertiesSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.CompoundProperties
        exclude = []


class CompoundRecordsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.CompoundRecords
        exclude = []


class CompoundStructuralAlertsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.CompoundStructuralAlerts
        exclude = []


class CompoundStructuresSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.CompoundStructures
        exclude = []


class ConfidenceScoreLookupSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ConfidenceScoreLookup
        exclude = []


class CurationLookupSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.CurationLookup
        exclude = []


class DataValidityLookupSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.DataValidityLookup
        exclude = []


class DefinedDailyDoseSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.DefinedDailyDose
        exclude = []


class DocsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Docs
        exclude = []


class DomainsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Domains
        exclude = []


class DrugIndicationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.DrugIndication
        exclude = []


class DrugMechanismSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.DrugMechanism
        exclude = []


class FormulationsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Formulations
        exclude = []


class FracClassificationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.FracClassification
        exclude = []


class GoClassificationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.GoClassification
        exclude = []


class HracClassificationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.HracClassification
        exclude = []


class IndicationRefsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.IndicationRefs
        exclude = []


class IracClassificationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.IracClassification
        exclude = []


class LigandEffSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.LigandEff
        exclude = []


class MechanismRefsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.MechanismRefs
        exclude = []


class MetabolismSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Metabolism
        exclude = []


class MetabolismRefsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.MetabolismRefs
        exclude = []


class MoleculeAtcClassificationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.MoleculeAtcClassification
        exclude = []


class MoleculeDictionarySerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.MoleculeDictionary
        exclude = []


class MoleculeFracClassificationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.MoleculeFracClassification
        exclude = []


class MoleculeHierarchySerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.MoleculeHierarchy
        exclude = []


class MoleculeHracClassificationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.MoleculeHracClassification
        exclude = []


class MoleculeIracClassificationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.MoleculeIracClassification
        exclude = []


class MoleculeSynonymsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.MoleculeSynonyms
        exclude = []


class OrganismClassSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.OrganismClass
        exclude = []


class ParameterTypeSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ParameterType
        exclude = []


class PatentUseCodesSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.PatentUseCodes
        exclude = []


class PredictedBindingDomainsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.PredictedBindingDomains
        exclude = []


class ProductPatentsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ProductPatents
        exclude = []


class ProductsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Products
        exclude = []


class ProteinClassSynonymsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ProteinClassSynonyms
        exclude = []


class ProteinClassificationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ProteinClassification
        exclude = []


class ProteinFamilyClassificationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ProteinFamilyClassification
        exclude = []


class RelationshipTypeSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.RelationshipType
        exclude = []


class ResearchCompaniesSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ResearchCompanies
        exclude = []


class ResearchStemSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.ResearchStem
        exclude = []


class SiteComponentsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.SiteComponents
        exclude = []


class SourceSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Source
        exclude = []


class StructuralAlertSetsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.StructuralAlertSets
        exclude = []


class StructuralAlertsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.StructuralAlerts
        exclude = []


class TargetComponentsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.TargetComponents
        exclude = []


class TargetDictionarySerializer(serializers.DynamicModelSerializer):
    # assays_set = serializers.DynamicRelationField(AssaysSerializer, many=True)
    activities_count = IntegerField(read_only=True)

    class Meta:
        model = models.TargetDictionary
        exclude = []


class TargetRelationsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.TargetRelations
        exclude = []


class TargetTypeSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.TargetType
        exclude = []


class TissueDictionarySerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.TissueDictionary
        exclude = []


class UsanStemsSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.UsanStems
        exclude = []


class VariantSequencesSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.VariantSequences
        exclude = []


class VersionSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Version
        exclude = []

