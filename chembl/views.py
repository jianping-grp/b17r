from django.db.models import Count, F
from rest_framework import generics, permissions
from dynamic_rest import viewsets
from . import models, serializers


class ActionTypeViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ActionType.objects.all()
    serializer_class = serializers.ActionTypeSerializer


class ActivitiesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Activities.objects.all()
    serializer_class = serializers.ActivitiesSerializer
    ordering = ('activity_id',)


class ActivityPropertiesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ActivityProperties.objects.all()
    serializer_class = serializers.ActivityPropertiesSerializer


class ActivitySmidViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ActivitySmid.objects.all()
    serializer_class = serializers.ActivitySmidSerializer


class ActivityStdsLookupViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ActivityStdsLookup.objects.all()
    serializer_class = serializers.ActivityStdsLookupSerializer


class ActivitySuppMapViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ActivitySuppMap.objects.all()
    serializer_class = serializers.ActivitySuppMapSerializer


class ActivitySuppViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ActivitySupp.objects.all()
    serializer_class = serializers.ActivitySuppSerializer


class AssayParametersViewSet(viewsets.DynamicModelViewSet):
    queryset = models.AssayParameters.objects.all()
    serializer_class = serializers.AssayParametersSerializer


class AssayTypeViewSet(viewsets.DynamicModelViewSet):
    queryset = models.AssayType.objects.all()
    serializer_class = serializers.AssayTypeSerializer


class AssaysViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Assays.objects.all()
    serializer_class = serializers.AssaysSerializer


class AtcClassificationViewSet(viewsets.DynamicModelViewSet):
    queryset = models.AtcClassification.objects.all()
    serializer_class = serializers.AtcClassificationSerializer


class BindingSitesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.BindingSites.objects.all()
    serializer_class = serializers.BindingSitesSerializer


class BioComponentSequencesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.BioComponentSequences.objects.all()
    serializer_class = serializers.BioComponentSequencesSerializer


class BioassayOntologyViewSet(viewsets.DynamicModelViewSet):
    queryset = models.BioassayOntology.objects.all()
    serializer_class = serializers.BioassayOntologySerializer


class BiotherapeuticComponentsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.BiotherapeuticComponents.objects.all()
    serializer_class = serializers.BiotherapeuticComponentsSerializer


class BiotherapeuticsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Biotherapeutics.objects.all()
    serializer_class = serializers.BiotherapeuticsSerializer


class CellDictionaryViewSet(viewsets.DynamicModelViewSet):
    queryset = models.CellDictionary.objects.all()
    serializer_class = serializers.CellDictionarySerializer


class ChemblIdLookupViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ChemblIdLookup.objects.all()
    serializer_class = serializers.ChemblIdLookupSerializer


class ComponentClassViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ComponentClass.objects.all()
    serializer_class = serializers.ComponentClassSerializer


class ComponentDomainsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ComponentDomains.objects.all()
    serializer_class = serializers.ComponentDomainsSerializer


class ComponentGoViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ComponentGo.objects.all()
    serializer_class = serializers.ComponentGoSerializer


class ComponentSequencesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ComponentSequences.objects.all()
    serializer_class = serializers.ComponentSequencesSerializer


class ComponentSynonymsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ComponentSynonyms.objects.all()
    serializer_class = serializers.ComponentSynonymsSerializer


class CompoundPropertiesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.CompoundProperties.objects.all()
    serializer_class = serializers.CompoundPropertiesSerializer


class CompoundRecordsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.CompoundRecords.objects.all()
    serializer_class = serializers.CompoundRecordsSerializer


class CompoundStructuralAlertsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.CompoundStructuralAlerts.objects.all()
    serializer_class = serializers.CompoundStructuralAlertsSerializer


class CompoundStructuresViewSet(viewsets.DynamicModelViewSet):
    queryset = models.CompoundStructures.objects.all()
    serializer_class = serializers.CompoundStructuresSerializer


class ConfidenceScoreLookupViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ConfidenceScoreLookup.objects.all()
    serializer_class = serializers.ConfidenceScoreLookupSerializer


class CurationLookupViewSet(viewsets.DynamicModelViewSet):
    queryset = models.CurationLookup.objects.all()
    serializer_class = serializers.CurationLookupSerializer


class DataValidityLookupViewSet(viewsets.DynamicModelViewSet):
    queryset = models.DataValidityLookup.objects.all()
    serializer_class = serializers.DataValidityLookupSerializer


class DefinedDailyDoseViewSet(viewsets.DynamicModelViewSet):
    queryset = models.DefinedDailyDose.objects.all()
    serializer_class = serializers.DefinedDailyDoseSerializer


class DocsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Docs.objects.all()
    serializer_class = serializers.DocsSerializer


class DomainsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Domains.objects.all()
    serializer_class = serializers.DomainsSerializer


class DrugIndicationViewSet(viewsets.DynamicModelViewSet):
    queryset = models.DrugIndication.objects.all()
    serializer_class = serializers.DrugIndicationSerializer


class DrugMechanismViewSet(viewsets.DynamicModelViewSet):
    queryset = models.DrugMechanism.objects.all()
    serializer_class = serializers.DrugMechanismSerializer


class FormulationsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Formulations.objects.all()
    serializer_class = serializers.FormulationsSerializer


class FracClassificationViewSet(viewsets.DynamicModelViewSet):
    queryset = models.FracClassification.objects.all()
    serializer_class = serializers.FracClassificationSerializer


class GoClassificationViewSet(viewsets.DynamicModelViewSet):
    queryset = models.GoClassification.objects.all()
    serializer_class = serializers.GoClassificationSerializer


class HracClassificationViewSet(viewsets.DynamicModelViewSet):
    queryset = models.HracClassification.objects.all()
    serializer_class = serializers.HracClassificationSerializer


class IndicationRefsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.IndicationRefs.objects.all()
    serializer_class = serializers.IndicationRefsSerializer


class IracClassificationViewSet(viewsets.DynamicModelViewSet):
    queryset = models.IracClassification.objects.all()
    serializer_class = serializers.IracClassificationSerializer


class LigandEffViewSet(viewsets.DynamicModelViewSet):
    queryset = models.LigandEff.objects.all()
    serializer_class = serializers.LigandEffSerializer


class MechanismRefsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.MechanismRefs.objects.all()
    serializer_class = serializers.MechanismRefsSerializer


class MetabolismRefsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.MetabolismRefs.objects.all()
    serializer_class = serializers.MetabolismRefsSerializer


class MetabolismViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Metabolism.objects.all()
    serializer_class = serializers.MetabolismSerializer


class MoleculeAtcClassificationViewSet(viewsets.DynamicModelViewSet):
    queryset = models.MoleculeAtcClassification.objects.all()
    serializer_class = serializers.MoleculeAtcClassificationSerializer


class MoleculeDictionaryViewSet(viewsets.DynamicModelViewSet):
    queryset = models.MoleculeDictionary.objects.all().annotate(
        activities_count=Count('activities')
    )
    serializer_class = serializers.MoleculeDictionarySerializer


class MoleculeFracClassificationViewSet(viewsets.DynamicModelViewSet):
    queryset = models.MoleculeFracClassification.objects.all()
    serializer_class = serializers.MoleculeFracClassificationSerializer


class MoleculeHierarchyViewSet(viewsets.DynamicModelViewSet):
    queryset = models.MoleculeHierarchy.objects.all()
    serializer_class = serializers.MoleculeHierarchySerializer


class MoleculeHracClassificationViewSet(viewsets.DynamicModelViewSet):
    queryset = models.MoleculeHracClassification.objects.all()
    serializer_class = serializers.MoleculeHracClassificationSerializer


class MoleculeIracClassificationViewSet(viewsets.DynamicModelViewSet):
    queryset = models.MoleculeIracClassification.objects.all()
    serializer_class = serializers.MoleculeIracClassificationSerializer


class MoleculeSynonymsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.MoleculeSynonyms.objects.all()
    serializer_class = serializers.MoleculeSynonymsSerializer


class OrganismClassViewSet(viewsets.DynamicModelViewSet):
    queryset = models.OrganismClass.objects.all()
    serializer_class = serializers.OrganismClassSerializer


class PatentUseCodesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.PatentUseCodes.objects.all()
    serializer_class = serializers.PatentUseCodesSerializer


class PredictedBindingDomainsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.PredictedBindingDomains.objects.all()
    serializer_class = serializers.PredictedBindingDomainsSerializer


class ProductPatentsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ProductPatents.objects.all()
    serializer_class = serializers.ProductPatentsSerializer


class ProductsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer


class ProteinClassSynonymsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ProteinClassSynonyms.objects.all()
    serializer_class = serializers.ProteinClassSynonymsSerializer


class ProteinClassificationViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ProteinClassification.objects.all()
    serializer_class = serializers.ProteinClassificationSerializer


class ProteinFamilyClassificationViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ProteinFamilyClassification.objects.all()
    serializer_class = serializers.ProteinFamilyClassificationSerializer


class RawDataViewSet(viewsets.DynamicModelViewSet):
    queryset = models.RawData.objects.all()
    serializer_class = serializers.RawDataSerializer


class RelationshipTypeViewSet(viewsets.DynamicModelViewSet):
    queryset = models.RelationshipType.objects.all()
    serializer_class = serializers.RelationshipTypeSerializer


class ResearchCompaniesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ResearchCompanies.objects.all()
    serializer_class = serializers.ResearchCompaniesSerializer


class ResearchStemViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ResearchStem.objects.all()
    serializer_class = serializers.ResearchStemSerializer


class SiteComponentsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.SiteComponents.objects.all()
    serializer_class = serializers.SiteComponentsSerializer


class SourceViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Source.objects.all()
    serializer_class = serializers.SourceSerializer


class StructuralAlertSetsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.StructuralAlertSets.objects.all()
    serializer_class = serializers.StructuralAlertSetsSerializer


class StructuralAlertsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.StructuralAlerts.objects.all()
    serializer_class = serializers.StructuralAlertsSerializer


class TargetComponentsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.TargetComponents.objects.all()
    serializer_class = serializers.TargetComponentsSerializer


class TargetDictionaryViewSet(viewsets.DynamicModelViewSet):
    queryset = models.TargetDictionary.objects.all().annotate(assays_count=Count('assays'))
    serializer_class = serializers.TargetDictionarySerializer


class TargetRelationsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.TargetRelations.objects.all()
    serializer_class = serializers.TargetRelationsSerializer


class TargetTypeViewSet(viewsets.DynamicModelViewSet):
    queryset = models.TargetType.objects.all()
    serializer_class = serializers.TargetTypeSerializer


class TissueDictionaryViewSet(viewsets.DynamicModelViewSet):
    queryset = models.TissueDictionary.objects.all()
    serializer_class = serializers.TissueDictionarySerializer


class UsanStemsViewSet(viewsets.DynamicModelViewSet):
    queryset = models.UsanStems.objects.all()
    serializer_class = serializers.UsanStemsSerializer


class VariantSequencesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.VariantSequences.objects.all()
    serializer_class = serializers.VariantSequencesSerializer


class VersionViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Version.objects.all()
    serializer_class = serializers.VersionSerializer
