
from . import models
from dynamic_rest import serializers


class ActionTypeSerializer(serializers.DynamicModelSerializer):
    drugmechanism_set = serializers.DynamicRelationField('DrugMechanismSerializer', many=True, deferred=True)

    class Meta:
        model = models.ActionType
        exclude = []


class ActivitiesSerializer(serializers.DynamicModelSerializer):
    activityproperties_set = serializers.DynamicRelationField('ActivityPropertiesSerializer', many=True, deferred=True)
    activitysuppmap_set = serializers.DynamicRelationField('ActivitySuppMapSerializer', many=True, deferred=True)
    assay = serializers.DynamicRelationField('AssaysSerializer')
    bao_endpoint = serializers.DynamicRelationField('BioassayOntologySerializer')
    data_validity_comment = serializers.DynamicRelationField('DataValidityLookupSerializer')
    doc = serializers.DynamicRelationField('DocsSerializer')
    ligandeff_set = serializers.DynamicRelationField('LigandEffSerializer', many=True, deferred=True)
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')
    predictedbindingdomains_set = serializers.DynamicRelationField('PredictedBindingDomainsSerializer', many=True, deferred=True)
    record = serializers.DynamicRelationField('CompoundRecordsSerializer')
    src = serializers.DynamicRelationField('SourceSerializer')

    class Meta:
        model = models.Activities
        exclude = []


class ActivityPropertiesSerializer(serializers.DynamicModelSerializer):
    activity = serializers.DynamicRelationField('ActivitiesSerializer')

    class Meta:
        model = models.ActivityProperties
        exclude = []


class ActivitySmidSerializer(serializers.DynamicModelSerializer):
    activitysupp_set = serializers.DynamicRelationField('ActivitySuppSerializer', many=True, deferred=True)
    activitysuppmap_set = serializers.DynamicRelationField('ActivitySuppMapSerializer', many=True, deferred=True)

    class Meta:
        model = models.ActivitySmid
        exclude = []


class ActivityStdsLookupSerializer(serializers.DynamicModelSerializer):

    class Meta:
        model = models.ActivityStdsLookup
        exclude = []


class ActivitySuppSerializer(serializers.DynamicModelSerializer):
    smid = serializers.DynamicRelationField('ActivitySmidSerializer')

    class Meta:
        model = models.ActivitySupp
        exclude = []


class ActivitySuppMapSerializer(serializers.DynamicModelSerializer):
    activity = serializers.DynamicRelationField('ActivitiesSerializer')
    smid = serializers.DynamicRelationField('ActivitySmidSerializer')

    class Meta:
        model = models.ActivitySuppMap
        exclude = []


class AssayParametersSerializer(serializers.DynamicModelSerializer):
    assay = serializers.DynamicRelationField('AssaysSerializer')

    class Meta:
        model = models.AssayParameters
        exclude = []


class AssayTypeSerializer(serializers.DynamicModelSerializer):
    assays_set = serializers.DynamicRelationField('AssaysSerializer', many=True, deferred=True)

    class Meta:
        model = models.AssayType
        exclude = []


class AssaysSerializer(serializers.DynamicModelSerializer):
    activities_set = serializers.DynamicRelationField('ActivitiesSerializer', many=True, deferred=True)
    assay_type = serializers.DynamicRelationField('AssayTypeSerializer')
    assayparameters_set = serializers.DynamicRelationField('AssayParametersSerializer', many=True, deferred=True)
    bao_format = serializers.DynamicRelationField('BioassayOntologySerializer')
    cell = serializers.DynamicRelationField('CellDictionarySerializer')
    chembl = serializers.DynamicRelationField('ChemblIdLookupSerializer')
    confidence_score = serializers.DynamicRelationField('ConfidenceScoreLookupSerializer')
    curated_by = serializers.DynamicRelationField('CurationLookupSerializer')
    doc = serializers.DynamicRelationField('DocsSerializer')
    left_hand_assay = serializers.DynamicRelationField('MMPSerializer', many=True, deferred=True)
    relationship_type = serializers.DynamicRelationField('RelationshipTypeSerializer')
    right_hand_assay = serializers.DynamicRelationField('MMPSerializer', many=True, deferred=True)
    src = serializers.DynamicRelationField('SourceSerializer')
    tid = serializers.DynamicRelationField('TargetDictionarySerializer')
    tissue = serializers.DynamicRelationField('TissueDictionarySerializer')
    variant = serializers.DynamicRelationField('VariantSequencesSerializer')

    class Meta:
        model = models.Assays
        exclude = []


class AtcClassificationSerializer(serializers.DynamicModelSerializer):
    defineddailydose_set = serializers.DynamicRelationField('DefinedDailyDoseSerializer', many=True, deferred=True)
    moleculeatcclassification_set = serializers.DynamicRelationField('MoleculeAtcClassificationSerializer', many=True, deferred=True)

    class Meta:
        model = models.AtcClassification
        exclude = []


class BindingSitesSerializer(serializers.DynamicModelSerializer):
    drugmechanism_set = serializers.DynamicRelationField('DrugMechanismSerializer', many=True, deferred=True)
    predictedbindingdomains_set = serializers.DynamicRelationField('PredictedBindingDomainsSerializer', many=True, deferred=True)
    sitecomponents_set = serializers.DynamicRelationField('SiteComponentsSerializer', many=True, deferred=True)
    tid = serializers.DynamicRelationField('TargetDictionarySerializer')

    class Meta:
        model = models.BindingSites
        exclude = []


class BioComponentSequencesSerializer(serializers.DynamicModelSerializer):
    biotherapeuticcomponents_set = serializers.DynamicRelationField('BiotherapeuticComponentsSerializer', many=True, deferred=True)

    class Meta:
        model = models.BioComponentSequences
        exclude = []


class BioassayOntologySerializer(serializers.DynamicModelSerializer):
    activities_set = serializers.DynamicRelationField('ActivitiesSerializer', many=True, deferred=True)
    assays_set = serializers.DynamicRelationField('AssaysSerializer', many=True, deferred=True)

    class Meta:
        model = models.BioassayOntology
        exclude = []


class BiotherapeuticComponentsSerializer(serializers.DynamicModelSerializer):
    component = serializers.DynamicRelationField('BioComponentSequencesSerializer')
    molregno = serializers.DynamicRelationField('BiotherapeuticsSerializer')

    class Meta:
        model = models.BiotherapeuticComponents
        exclude = []


class BiotherapeuticsSerializer(serializers.DynamicModelSerializer):
    biotherapeuticcomponents_set = serializers.DynamicRelationField('BiotherapeuticComponentsSerializer', many=True, deferred=True)
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')

    class Meta:
        model = models.Biotherapeutics
        exclude = []


class CellDictionarySerializer(serializers.DynamicModelSerializer):
    assays_set = serializers.DynamicRelationField('AssaysSerializer', many=True, deferred=True)
    chembl = serializers.DynamicRelationField('ChemblIdLookupSerializer')

    class Meta:
        model = models.CellDictionary
        exclude = []


class ChemblIdLookupSerializer(serializers.DynamicModelSerializer):
    assays_set = serializers.DynamicRelationField('AssaysSerializer', many=True, deferred=True)
    celldictionary_set = serializers.DynamicRelationField('CellDictionarySerializer', many=True, deferred=True)
    docs_set = serializers.DynamicRelationField('DocsSerializer', many=True, deferred=True)
    moleculedictionary_set = serializers.DynamicRelationField('MoleculeDictionarySerializer', many=True, deferred=True)
    targetdictionary_set = serializers.DynamicRelationField('TargetDictionarySerializer', many=True, deferred=True)
    tissuedictionary_set = serializers.DynamicRelationField('TissueDictionarySerializer', many=True, deferred=True)

    class Meta:
        model = models.ChemblIdLookup
        exclude = []


class ComponentClassSerializer(serializers.DynamicModelSerializer):
    component = serializers.DynamicRelationField('ComponentSequencesSerializer')
    protein_class = serializers.DynamicRelationField('ProteinClassificationSerializer')

    class Meta:
        model = models.ComponentClass
        exclude = []


class ComponentDomainsSerializer(serializers.DynamicModelSerializer):
    component = serializers.DynamicRelationField('ComponentSequencesSerializer')
    domain = serializers.DynamicRelationField('DomainsSerializer')

    class Meta:
        model = models.ComponentDomains
        exclude = []


class ComponentGoSerializer(serializers.DynamicModelSerializer):
    component = serializers.DynamicRelationField('ComponentSequencesSerializer')
    go = serializers.DynamicRelationField('GoClassificationSerializer')

    class Meta:
        model = models.ComponentGo
        exclude = []


class ComponentSequencesSerializer(serializers.DynamicModelSerializer):
    componentclass_set = serializers.DynamicRelationField('ComponentClassSerializer', many=True, deferred=True)
    componentdomains_set = serializers.DynamicRelationField('ComponentDomainsSerializer', many=True, deferred=True)
    componentgo_set = serializers.DynamicRelationField('ComponentGoSerializer', many=True, deferred=True)
    componentsynonyms_set = serializers.DynamicRelationField('ComponentSynonymsSerializer', many=True, deferred=True)
    sitecomponents_set = serializers.DynamicRelationField('SiteComponentsSerializer', many=True, deferred=True)
    targetcomponents_set = serializers.DynamicRelationField('TargetComponentsSerializer', many=True, deferred=True)

    class Meta:
        model = models.ComponentSequences
        exclude = []


class ComponentSynonymsSerializer(serializers.DynamicModelSerializer):
    component = serializers.DynamicRelationField('ComponentSequencesSerializer')

    class Meta:
        model = models.ComponentSynonyms
        exclude = []


class CompoundPropertiesSerializer(serializers.DynamicModelSerializer):
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')

    class Meta:
        model = models.CompoundProperties
        exclude = []


class CompoundRecordsSerializer(serializers.DynamicModelSerializer):
    activities_set = serializers.DynamicRelationField('ActivitiesSerializer', many=True, deferred=True)
    doc = serializers.DynamicRelationField('DocsSerializer')
    drugindication_set = serializers.DynamicRelationField('DrugIndicationSerializer', many=True, deferred=True)
    drugmechanism_set = serializers.DynamicRelationField('DrugMechanismSerializer', many=True, deferred=True)
    formulations_set = serializers.DynamicRelationField('FormulationsSerializer', many=True, deferred=True)
    metabolism_set = serializers.DynamicRelationField('MetabolismSerializer', many=True, deferred=True)
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')
    src = serializers.DynamicRelationField('SourceSerializer')

    class Meta:
        model = models.CompoundRecords
        exclude = []


class CompoundStructuralAlertsSerializer(serializers.DynamicModelSerializer):
    alert = serializers.DynamicRelationField('StructuralAlertsSerializer')
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')

    class Meta:
        model = models.CompoundStructuralAlerts
        exclude = []


class CompoundStructuresSerializer(serializers.DynamicModelSerializer):
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')

    class Meta:
        model = models.CompoundStructures
        exclude = []


class ConfidenceScoreLookupSerializer(serializers.DynamicModelSerializer):
    assays_set = serializers.DynamicRelationField('AssaysSerializer', many=True, deferred=True)

    class Meta:
        model = models.ConfidenceScoreLookup
        exclude = []


class CurationLookupSerializer(serializers.DynamicModelSerializer):
    assays_set = serializers.DynamicRelationField('AssaysSerializer', many=True, deferred=True)

    class Meta:
        model = models.CurationLookup
        exclude = []


class DataValidityLookupSerializer(serializers.DynamicModelSerializer):
    activities_set = serializers.DynamicRelationField('ActivitiesSerializer', many=True, deferred=True)

    class Meta:
        model = models.DataValidityLookup
        exclude = []


class DefinedDailyDoseSerializer(serializers.DynamicModelSerializer):
    atc_code = serializers.DynamicRelationField('AtcClassificationSerializer')

    class Meta:
        model = models.DefinedDailyDose
        exclude = []


class DocsSerializer(serializers.DynamicModelSerializer):
    activities_set = serializers.DynamicRelationField('ActivitiesSerializer', many=True, deferred=True)
    assays_set = serializers.DynamicRelationField('AssaysSerializer', many=True, deferred=True)
    chembl = serializers.DynamicRelationField('ChemblIdLookupSerializer')
    compoundrecords_set = serializers.DynamicRelationField('CompoundRecordsSerializer', many=True, deferred=True)
    src = serializers.DynamicRelationField('SourceSerializer')

    class Meta:
        model = models.Docs
        exclude = []


class DomainsSerializer(serializers.DynamicModelSerializer):
    componentdomains_set = serializers.DynamicRelationField('ComponentDomainsSerializer', many=True, deferred=True)
    sitecomponents_set = serializers.DynamicRelationField('SiteComponentsSerializer', many=True, deferred=True)

    class Meta:
        model = models.Domains
        exclude = []


class DrugIndicationSerializer(serializers.DynamicModelSerializer):
    indicationrefs_set = serializers.DynamicRelationField('IndicationRefsSerializer', many=True, deferred=True)
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')
    record = serializers.DynamicRelationField('CompoundRecordsSerializer')

    class Meta:
        model = models.DrugIndication
        exclude = []


class DrugMechanismSerializer(serializers.DynamicModelSerializer):
    action_type = serializers.DynamicRelationField('ActionTypeSerializer')
    mechanismrefs_set = serializers.DynamicRelationField('MechanismRefsSerializer', many=True, deferred=True)
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')
    record = serializers.DynamicRelationField('CompoundRecordsSerializer')
    site = serializers.DynamicRelationField('BindingSitesSerializer')
    tid = serializers.DynamicRelationField('TargetDictionarySerializer')

    class Meta:
        model = models.DrugMechanism
        exclude = []


class FormulationsSerializer(serializers.DynamicModelSerializer):
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')
    product = serializers.DynamicRelationField('ProductsSerializer')
    record = serializers.DynamicRelationField('CompoundRecordsSerializer')

    class Meta:
        model = models.Formulations
        exclude = []


class FracClassificationSerializer(serializers.DynamicModelSerializer):
    moleculefracclassification_set = serializers.DynamicRelationField('MoleculeFracClassificationSerializer', many=True, deferred=True)

    class Meta:
        model = models.FracClassification
        exclude = []


class GoClassificationSerializer(serializers.DynamicModelSerializer):
    componentgo_set = serializers.DynamicRelationField('ComponentGoSerializer', many=True, deferred=True)

    class Meta:
        model = models.GoClassification
        exclude = []


class HracClassificationSerializer(serializers.DynamicModelSerializer):
    moleculehracclassification_set = serializers.DynamicRelationField('MoleculeHracClassificationSerializer', many=True, deferred=True)

    class Meta:
        model = models.HracClassification
        exclude = []


class IndicationRefsSerializer(serializers.DynamicModelSerializer):
    drugind = serializers.DynamicRelationField('DrugIndicationSerializer')

    class Meta:
        model = models.IndicationRefs
        exclude = []


class IracClassificationSerializer(serializers.DynamicModelSerializer):
    moleculeiracclassification_set = serializers.DynamicRelationField('MoleculeIracClassificationSerializer', many=True, deferred=True)

    class Meta:
        model = models.IracClassification
        exclude = []


class LigandEffSerializer(serializers.DynamicModelSerializer):
    activity = serializers.DynamicRelationField('ActivitiesSerializer')

    class Meta:
        model = models.LigandEff
        exclude = []


class MechanismRefsSerializer(serializers.DynamicModelSerializer):
    mec = serializers.DynamicRelationField('DrugMechanismSerializer')

    class Meta:
        model = models.MechanismRefs
        exclude = []


class MetabolismSerializer(serializers.DynamicModelSerializer):
    drug_record = serializers.DynamicRelationField('CompoundRecordsSerializer')
    enzyme_tid = serializers.DynamicRelationField('TargetDictionarySerializer')
    metabolismrefs_set = serializers.DynamicRelationField('MetabolismRefsSerializer', many=True, deferred=True)
    metabolite_record = serializers.DynamicRelationField('CompoundRecordsSerializer')
    substrate_record = serializers.DynamicRelationField('CompoundRecordsSerializer')

    class Meta:
        model = models.Metabolism
        exclude = []


class MetabolismRefsSerializer(serializers.DynamicModelSerializer):
    met = serializers.DynamicRelationField('MetabolismSerializer')

    class Meta:
        model = models.MetabolismRefs
        exclude = []


class MoleculeAtcClassificationSerializer(serializers.DynamicModelSerializer):
    level5 = serializers.DynamicRelationField('AtcClassificationSerializer')
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')

    class Meta:
        model = models.MoleculeAtcClassification
        exclude = []


class MoleculeDictionarySerializer(serializers.DynamicModelSerializer):
    activities_set = serializers.DynamicRelationField('ActivitiesSerializer', many=True, deferred=True)
    biotherapeutics_set = serializers.DynamicRelationField('BiotherapeuticsSerializer', many=True, deferred=True)
    chembl = serializers.DynamicRelationField('ChemblIdLookupSerializer')
    compoundproperties_set = serializers.DynamicRelationField('CompoundPropertiesSerializer', many=True, deferred=True)
    compoundrecords_set = serializers.DynamicRelationField('CompoundRecordsSerializer', many=True, deferred=True)
    compoundstructuralalerts_set = serializers.DynamicRelationField('CompoundStructuralAlertsSerializer', many=True, deferred=True)
    compoundstructures_set = serializers.DynamicRelationField('CompoundStructuresSerializer', many=True, deferred=True)
    drugindication_set = serializers.DynamicRelationField('DrugIndicationSerializer', many=True, deferred=True)
    drugmechanism_set = serializers.DynamicRelationField('DrugMechanismSerializer', many=True, deferred=True)
    formulations_set = serializers.DynamicRelationField('FormulationsSerializer', many=True, deferred=True)
    left_hand_mol = serializers.DynamicRelationField('MMPSerializer', many=True, deferred=True)
    moleculeatcclassification_set = serializers.DynamicRelationField('MoleculeAtcClassificationSerializer', many=True, deferred=True)
    moleculefracclassification_set = serializers.DynamicRelationField('MoleculeFracClassificationSerializer', many=True, deferred=True)
    moleculehierarchy_set = serializers.DynamicRelationField('MoleculeHierarchySerializer', many=True, deferred=True)
    moleculehracclassification_set = serializers.DynamicRelationField('MoleculeHracClassificationSerializer', many=True, deferred=True)
    moleculeiracclassification_set = serializers.DynamicRelationField('MoleculeIracClassificationSerializer', many=True, deferred=True)
    moleculesynonyms_set = serializers.DynamicRelationField('MoleculeSynonymsSerializer', many=True, deferred=True)
    phin_hierarchy = serializers.DynamicRelationField('MoleculeHierarchySerializer')
    phin_molecule = serializers.DynamicRelationField('MoleculeSerializer')
    right_hand_mol = serializers.DynamicRelationField('MMPSerializer', many=True, deferred=True)

    class Meta:
        model = models.MoleculeDictionary
        exclude = []


class MoleculeFracClassificationSerializer(serializers.DynamicModelSerializer):
    frac_class = serializers.DynamicRelationField('FracClassificationSerializer')
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')

    class Meta:
        model = models.MoleculeFracClassification
        exclude = []


class MoleculeHierarchySerializer(serializers.DynamicModelSerializer):
    active_molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')
    parent_molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')

    class Meta:
        model = models.MoleculeHierarchy
        exclude = []


class MoleculeHracClassificationSerializer(serializers.DynamicModelSerializer):
    hrac_class = serializers.DynamicRelationField('HracClassificationSerializer')
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')

    class Meta:
        model = models.MoleculeHracClassification
        exclude = []


class MoleculeIracClassificationSerializer(serializers.DynamicModelSerializer):
    irac_class = serializers.DynamicRelationField('IracClassificationSerializer')
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')

    class Meta:
        model = models.MoleculeIracClassification
        exclude = []


class MoleculeSynonymsSerializer(serializers.DynamicModelSerializer):
    molregno = serializers.DynamicRelationField('MoleculeDictionarySerializer')
    res_stem = serializers.DynamicRelationField('ResearchStemSerializer')

    class Meta:
        model = models.MoleculeSynonyms
        exclude = []


class OrganismClassSerializer(serializers.DynamicModelSerializer):

    class Meta:
        model = models.OrganismClass
        exclude = []


class PatentUseCodesSerializer(serializers.DynamicModelSerializer):
    productpatents_set = serializers.DynamicRelationField('ProductPatentsSerializer', many=True, deferred=True)

    class Meta:
        model = models.PatentUseCodes
        exclude = []


class PredictedBindingDomainsSerializer(serializers.DynamicModelSerializer):
    activity = serializers.DynamicRelationField('ActivitiesSerializer')
    site = serializers.DynamicRelationField('BindingSitesSerializer')

    class Meta:
        model = models.PredictedBindingDomains
        exclude = []


class ProductPatentsSerializer(serializers.DynamicModelSerializer):
    patent_use_code = serializers.DynamicRelationField('PatentUseCodesSerializer')
    product = serializers.DynamicRelationField('ProductsSerializer')

    class Meta:
        model = models.ProductPatents
        exclude = []


class ProductsSerializer(serializers.DynamicModelSerializer):
    formulations_set = serializers.DynamicRelationField('FormulationsSerializer', many=True, deferred=True)
    productpatents_set = serializers.DynamicRelationField('ProductPatentsSerializer', many=True, deferred=True)

    class Meta:
        model = models.Products
        exclude = []


class ProteinClassSynonymsSerializer(serializers.DynamicModelSerializer):
    protein_class = serializers.DynamicRelationField('ProteinClassificationSerializer')

    class Meta:
        model = models.ProteinClassSynonyms
        exclude = []


class ProteinClassificationSerializer(serializers.DynamicModelSerializer):
    componentclass_set = serializers.DynamicRelationField('ComponentClassSerializer', many=True, deferred=True)
    proteinclasssynonyms_set = serializers.DynamicRelationField('ProteinClassSynonymsSerializer', many=True, deferred=True)

    class Meta:
        model = models.ProteinClassification
        exclude = []


class ProteinFamilyClassificationSerializer(serializers.DynamicModelSerializer):

    class Meta:
        model = models.ProteinFamilyClassification
        exclude = []


class RawDataSerializer(serializers.DynamicModelSerializer):

    class Meta:
        model = models.RawData
        exclude = []


class RelationshipTypeSerializer(serializers.DynamicModelSerializer):
    assays_set = serializers.DynamicRelationField('AssaysSerializer', many=True, deferred=True)

    class Meta:
        model = models.RelationshipType
        exclude = []


class ResearchCompaniesSerializer(serializers.DynamicModelSerializer):
    res_stem = serializers.DynamicRelationField('ResearchStemSerializer')

    class Meta:
        model = models.ResearchCompanies
        exclude = []


class ResearchStemSerializer(serializers.DynamicModelSerializer):
    moleculesynonyms_set = serializers.DynamicRelationField('MoleculeSynonymsSerializer', many=True, deferred=True)
    researchcompanies_set = serializers.DynamicRelationField('ResearchCompaniesSerializer', many=True, deferred=True)

    class Meta:
        model = models.ResearchStem
        exclude = []


class SiteComponentsSerializer(serializers.DynamicModelSerializer):
    component = serializers.DynamicRelationField('ComponentSequencesSerializer')
    domain = serializers.DynamicRelationField('DomainsSerializer')
    site = serializers.DynamicRelationField('BindingSitesSerializer')

    class Meta:
        model = models.SiteComponents
        exclude = []


class SourceSerializer(serializers.DynamicModelSerializer):
    activities_set = serializers.DynamicRelationField('ActivitiesSerializer', many=True, deferred=True)
    assays_set = serializers.DynamicRelationField('AssaysSerializer', many=True, deferred=True)
    compoundrecords_set = serializers.DynamicRelationField('CompoundRecordsSerializer', many=True, deferred=True)
    docs_set = serializers.DynamicRelationField('DocsSerializer', many=True, deferred=True)

    class Meta:
        model = models.Source
        exclude = []


class StructuralAlertSetsSerializer(serializers.DynamicModelSerializer):
    structuralalerts_set = serializers.DynamicRelationField('StructuralAlertsSerializer', many=True, deferred=True)

    class Meta:
        model = models.StructuralAlertSets
        exclude = []


class StructuralAlertsSerializer(serializers.DynamicModelSerializer):
    alert_set = serializers.DynamicRelationField('StructuralAlertSetsSerializer')
    compoundstructuralalerts_set = serializers.DynamicRelationField('CompoundStructuralAlertsSerializer', many=True, deferred=True)

    class Meta:
        model = models.StructuralAlerts
        exclude = []


class TargetComponentsSerializer(serializers.DynamicModelSerializer):
    component = serializers.DynamicRelationField('ComponentSequencesSerializer')
    tid = serializers.DynamicRelationField('TargetDictionarySerializer')

    class Meta:
        model = models.TargetComponents
        exclude = []


class TargetDictionarySerializer(serializers.DynamicModelSerializer):
    assays_set = serializers.DynamicRelationField('AssaysSerializer', many=True, deferred=True)
    bindingsites_set = serializers.DynamicRelationField('BindingSitesSerializer', many=True, deferred=True)
    chembl = serializers.DynamicRelationField('ChemblIdLookupSerializer')
    drugmechanism_set = serializers.DynamicRelationField('DrugMechanismSerializer', many=True, deferred=True)
    metabolism_set = serializers.DynamicRelationField('MetabolismSerializer', many=True, deferred=True)
    mmp_set = serializers.DynamicRelationField('MMPSerializer', many=True, deferred=True)
    phin_target = serializers.DynamicRelationField()
    target_type = serializers.DynamicRelationField('TargetTypeSerializer')
    targetcomponents_set = serializers.DynamicRelationField('TargetComponentsSerializer', many=True, deferred=True)
    targetrelations_set = serializers.DynamicRelationField('TargetRelationsSerializer', many=True, deferred=True)

    class Meta:
        model = models.TargetDictionary
        exclude = []


class TargetRelationsSerializer(serializers.DynamicModelSerializer):
    related_tid = serializers.DynamicRelationField('TargetDictionarySerializer')
    tid = serializers.DynamicRelationField('TargetDictionarySerializer')

    class Meta:
        model = models.TargetRelations
        exclude = []


class TargetTypeSerializer(serializers.DynamicModelSerializer):
    targetdictionary_set = serializers.DynamicRelationField('TargetDictionarySerializer', many=True, deferred=True)

    class Meta:
        model = models.TargetType
        exclude = []


class TissueDictionarySerializer(serializers.DynamicModelSerializer):
    assays_set = serializers.DynamicRelationField('AssaysSerializer', many=True, deferred=True)
    chembl = serializers.DynamicRelationField('ChemblIdLookupSerializer')

    class Meta:
        model = models.TissueDictionary
        exclude = []


class UsanStemsSerializer(serializers.DynamicModelSerializer):

    class Meta:
        model = models.UsanStems
        exclude = []


class VariantSequencesSerializer(serializers.DynamicModelSerializer):
    assays_set = serializers.DynamicRelationField('AssaysSerializer', many=True, deferred=True)

    class Meta:
        model = models.VariantSequences
        exclude = []


class VersionSerializer(serializers.DynamicModelSerializer):

    class Meta:
        model = models.Version
        exclude = []


