from phin.models import *
from chembl import models as chembl_models
from rdkit import Chem
from rdkit.Chem.Scaffolds import MurckoScaffold
from django_rdkit.models import *
import itertools as it
from django.db import connection
from b17r import settings
import os


def init_phin_molecule_hierarchy():
    for mol in chembl_models.MoleculeDictionary.objects.all().iterator():
        parent_mol = mol
        if hasattr(mol, 'as_child_molecule'):
            parent_mol = mol.as_child_molecule.parent_molregno
        MoleculeHierarchy.objects.create(
            molregno=mol,
            parent=parent_mol
        )


def init_phin_molecule_tbl():
    # log rdkit-invalid molecule
    with open(os.path.join(settings.BASE_DIR, 'logs', 'rdkit-invalid-mol.txt'), 'w') as w:
        mol_set = chembl_models.MoleculeDictionary.objects.all()
        for idx, mol in enumerate(mol_set.iterator()):
            # print mol.molregno
            if hasattr(mol, 'as_child_molecule'):
                # get parent molecule (rm salt)
                mol = mol.as_child_molecule.parent_molregno
            # if not mol.compoundstructures:
            if not hasattr(mol, 'compoundstructures'):
                # no structure
                w.write('\t'.join(['NS', str(idx), str(mol.molregno), '\n']))
                continue
            smiles = mol.compoundstructures.canonical_smiles
            phin_mol, created = Molecule.objects.get_or_create(molregno=mol)
            try:
                rdkit_mol = Chem.MolFromSmiles(smiles)
                phin_mol.structure = rdkit_mol
            except:
                # invalid molecular structure
                w.write('\t'.join(['IM', str(idx), str(mol.molregno), smiles, '\n']))
            phin_mol.save()


def init_phin_target_tbl():
    for idx, target in enumerate(chembl_models.TargetDictionary.objects.all()):
        phin_target, created = Target.objects.get_or_create(tid=target)
        phin_target.save()


def init_scaffold_tbl():
    mol_set = Molecule.objects.all()
    for mol in mol_set.iterator():
        try:
            core = MurckoScaffold.GetScaffoldForMol(mol.structure)
        except:
            continue
        core_smiles = Chem.MolToSmiles(core)
        # print core_smiles
        if core_smiles:
            scaffold, created = Scaffold.objects.get_or_create(smiles=core_smiles)
            scaffold.structure = core
            mol.scaffold = scaffold
            scaffold.save()
            mol.save()


def init_phin_activities_tbl():
    target_set = Target.objects.all()
    with open('init_activities_tbl.log', 'w') as w:
        for target in target_set.iterator():
            print target.target_id, target.tid_id
            for idx, row in target.get_activities_pchembl_list() \
                    .groupby('parent_molregno')[['pchembl_value', 'parent_molregno']]:
                molregno = row['parent_molregno'].values[0]
                try:
                    molecule = Molecule.objects.get(molregno_id=molregno)
                except:  # some molecule may not have structures
                    w.write('{0}, {1}\n'.format(target.target_id, molregno))

                    continue
                activity, created = Activities.objects.get_or_create(
                    molecule=molecule,
                    target=target
                )

                activity.mean = round(row['pchembl_value'].mean(), 2)
                activity.max = row['pchembl_value'].max()
                activity.min = row['pchembl_value'].min()
                activity.median = round(row['pchembl_value'].median(), 2)
                activity.count = row['pchembl_value'].count()
                activity.save()


def init_molecule_interaction_tbl():
    # todo: exclude targets of admet, unchecked etc.
    sql = '''
    SELECT 
      phin_molecule.mol_id,
      count(phin_activities.act_id) as activity_count
    FROM 
      public.phin_molecule, 
      public.phin_activities
    WHERE 
      phin_activities.molecule_id = phin_molecule.mol_id
    GROUP BY phin_molecule.mol_id
    ORDER BY activity_count DESC
    '''
    with connection.cursor() as cursor:
        cursor.execute(sql)
        # get molecules that number of activities gte 10.
        data = map(lambda x: x[0], filter(lambda x: x[1] >= 10, cursor.fetchall()))
        for molid_1, molid_2 in it.combinations(data, 2):
            if molid_1 > molid_2:
                molid_1, molid_2 = molid_2, molid_1
            mol1 = Molecule.objects.get(pk=molid_1)
            comm_act = mol1.get_common_activities(molid_2)
            if len(comm_act) >= 5:
                MoleculeInteraction.objects.create(
                    first_molecule_id=molid_1,
                    second_molecule_id=molid_2,
                    target=list(comm_act['target_id']),
                    min=list(comm_act['min']),
                    max=list(comm_act['max']),
                    mean=list(comm_act['mean']),
                    median=list(comm_act['median'])
                )


def init_target_network_tbl():
    filter_out_type = ['ADMET', 'NO TARGET', 'UNCHECKED', 'UNDEFINED', 'UNKNOWN']
    target_set = Target.objects.exclude(tid__target_type__in=filter_out_type) \
        .annotate(act_count=Count('activities')) \
        .order_by('-act_count')
    for target1, target2 in it.combinations(target_set, 2):
        if target1.tid_id > target2.tid_id:
            target1, target2 = target2, target1
        comm = target1.get_common_activities(target2)
        if len(comm) > 0:
            TargetNetwork.objects.create(
                first_target=target1,
                second_target=target2,
                molecule=list(comm['molecule_id']),
                min=list(comm['min']),
                max=list(comm['max']),
                mean=list(comm['mean']),
                median=list(comm['median'])

            )


def init_target_scaffold_network_tbl():
    filter_out_types = ['ADMET', 'NO TARGET', 'UNCHECKED', 'UNDEFINED', 'UNKNOWN']
    target_set = Target.objects.exclude(tid__target_type__in=filter_out_types) \
        .annotate(act_count=Count('activities')) \
        .order_by('-act_count')
    for target1, target2 in it.combinations(target_set, 2):
        if target1.tid_id > target2.tid_id:
            target1, target2 = target2, target1
        comm = target1._get_common_scaffold_activities(target2)
        if len(comm) >=0:
            TargetScaffoldNetwork.objects.create(
                first_target=target1,
                second_target=target2,
                scaffold=list(comm['scaffold_id']),
                min=list(comm['min']),
                max=list(comm['max']),
                mean=list(comm['mean']),
                median=list(comm['median'])

            )


# def init_target_interaction_tbl():
#     # exclude uncheck chembl (chembl912545)
#     # todo: exclude target with 0 'valid' activity
#     target_set = Target.objects.all().annotate(act_count=Count('activities')).order_by('-act_count')[1:]
#     for target1, target2 in it.combinations(target_set, 2):
#         # print target1.target_id, target2.target_id
#         if target1.tid_id > target2.tid_id:
#             target1, target2 = target2, target1
#         TargetInteraction.objects.bulk_create(
#             [
#                 TargetInteraction(
#                     first_target=target1,
#                     second_target=target2,
#                     molecule_id=x['molecule_id'],
#                     min=x['min'],
#                     max=x['max'],
#                     mean=x['mean'],
#                     median=x['median']
#                 ) for idx, x in target1.get_common_activities(target2).iterrows()
#             ]
#         )


def init_scaffold_activities_tbl():
    for target in Target.objects.all():
        ScaffoldActivities.objects.bulk_create(
            [
                ScaffoldActivities(
                    target=target,
                    scaffold_id=row['scaffold_id'],
                    min=row['min'],
                    max=row['max'],
                    mean=round(row['mean'], 2),
                    median=round(row['median'], 2),
                    count=row['count']

                ) for idx, row in target._get_scaffold_activites().iterrows()
            ]
        )


# def init_target_scaffold_interaction_tbl():
#     # exclude uncheck chembl (chembl912545)
#     # todo: exclude target with 0 valid scaffold activity
#     target_set = Target.objects.all().annotate(act_count=Count('scaffoldactivities')).filter(act_count__gt=0).order_by(
#         '-act_count')[1:]
#     for target1, target2 in it.combinations(target_set, 2):
#         # print target1.target_id, target2.target_id
#         if target1.tid_id > target2.tid_id:
#             target1, target2 = target2, target1
#         TargetScaffoldInteraction.objects.bulk_create(
#             [
#                 TargetScaffoldInteraction(
#                     first_target=target1,
#                     second_target=target2,
#                     scaffold_id=x['scaffold_id'],
#                     min=x['min'],
#                     max=x['max'],
#                     mean=x['mean'],
#                     median=x['median']
#                 ) for idx, x in target1._get_common_scaffold_activities(target2).iterrows()
#             ]
#         )


def kegg_disease_class_tbl():
    import kegg
    json_file = 'phin/scripts/br08403.json'
    for elements in kegg.parse_ds_json(json_file):
        print elements
        if len(elements) == 2:
            kegg_id, kegg_name = elements
            disease_class, created = KEGGDiseaseClass.objects.get_or_create(kegg_id=kegg_id)
            disease_class.name = kegg_name

        elif len(elements) == 3:
            kegg_id, kegg_name, parent_id = elements
            parent, created = KEGGDiseaseClass.objects.get_or_create(kegg_id=parent_id)
            disease_class, created = KEGGDiseaseClass.objects.get_or_create(kegg_id=kegg_id)
            disease_class.parent = parent
            disease_class.name = kegg_name
        disease_class.save()


def kegg_disease_tbl():
    disease_uniprot_file = os.path.join(settings.BASE_DIR, 'phin/scripts', 'disease-uniprot.csv')
    for row in open(disease_uniprot_file):
        cell_list = row.strip().split(',')
        if len(cell_list) >= 2:
            kegg_id = cell_list[0]
            print kegg_id
            kegg_disease_class = KEGGDiseaseClass.objects.get(kegg_id=kegg_id)
            kegg_disease, created = KEGGDisease.objects.get_or_create(kegg_id=kegg_id)
            kegg_disease.kegg_class = kegg_disease_class
            kegg_disease.all_gene_accessions = cell_list[1:]
            for el in cell_list[1:]:
                try:
                    chembl_seq = chembl_models.ComponentSequences.objects.get(accession=el)
                    kegg_disease.chembl_mappings.add(chembl_seq)
                except chembl_models.ComponentSequences.DoesNotExist:
                    continue
            kegg_disease.save()

def create_molecule_fp():
    from django_rdkit.models import *

    Molecule.objects.update(
        mfp2=MORGANBV_FP('structure')
    )

def run():
    print 'start loading'
    # print 'init molecule hirarchy'
    # init_phin_molecule_hierarchy()
    #
    # print 'init molecule table'
    # init_phin_molecule_tbl()
    #
    # print 'init target table'
    # init_phin_target_tbl()
    #
    # print 'init scaffold table'
    # init_scaffold_tbl()
    #
    # print 'init phin activities table',
    # init_phin_activities_tbl()
    #
    # print 'scaffold activities table'
    # init_scaffold_activities_tbl()

    # print 'target interaction'
    # init_target_network_tbl()

    # print 'molecule interactions'
    # init_molecule_interaction_tbl()

    print 'init target scaffold network'
    init_target_scaffold_network_tbl()

    # print 'kegg disease'
    # kegg_disease_class_tbl()
    # kegg_disease_tbl()

    #print 'update phin molecule with fingerprints'
    #create_molecule_fp()
