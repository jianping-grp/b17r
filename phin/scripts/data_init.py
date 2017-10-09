from phin.models import *
from chembl import models as chembl_models
from rdkit import Chem
from rdkit.Chem.Scaffolds import MurckoScaffold
from django_rdkit.models import *
import itertools as it


def init_phin_molecule_tbl():
    # log rdkit-invalid molecule
    with open('phin/scripts/log/rdkit-invalid-mol.txt', 'w') as w:
        mol_set = chembl_models.MoleculeDictionary.objects.all()
        for idx, mol in enumerate(mol_set.iterator()):
            # print mol.molregno
            if hasattr(mol, 'as_child_molecule'):
                # get parent molecule (rm salt)
                mol = mol.as_child_molecule.parent_molregno
            #if not mol.compoundstructures:
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
    with open('phin/scripts/log/init_activities_tbl.log', 'w') as w:
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


def init_target_interaction_tbl():
    # exclude uncheck chembl (chembl912545)
    # todo: exclude target with 0 'valid' activity
    target_set = Target.objects.all().annotate(act_count=Count('activities')).order_by('-act_count')[1:]
    for target1, target2 in it.combinations(target_set, 2):
        # print target1.target_id, target2.target_id
        if target1.tid_id > target2.tid_id:
            target1, target2 = target2, target1
        TargetInteraction.objects.bulk_create(
            [
                TargetInteraction(
                    first_target=target1,
                    second_target=target2,
                    molecule_id=x['molecule_id'],
                    min=x['min'],
                    max=x['max'],
                    mean=x['mean'],
                    median=x['median']
                ) for idx, x in target1.get_common_activities(target2).iterrows()
            ]
        )


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


def init_target_scaffold_interaction_tbl():
    # exclude uncheck chembl (chembl912545)
    # todo: exclude target with 0 valid scaffold activity
    target_set = Target.objects.all().annotate(act_count=Count('scaffoldactivities')).filter(act_count__gt=0).order_by(
        '-act_count')[1:]
    for target1, target2 in it.combinations(target_set, 2):
        # print target1.target_id, target2.target_id
        if target1.tid_id > target2.tid_id:
            target1, target2 = target2, target1
        TargetScaffoldInteraction.objects.bulk_create(
            [
                TargetScaffoldInteraction(
                    first_target=target1,
                    second_target=target2,
                    scaffold_id=x['scaffold_id'],
                    min=x['min'],
                    max=x['max'],
                    mean=x['mean'],
                    median=x['median']
                ) for idx, x in target1._get_common_scaffold_activities(target2).iterrows()
            ]
        )

def run():

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
    # print 'target interaction table'
    # init_target_interaction_tbl()

    print 'scaffold activities table'
    init_scaffold_activities_tbl()

    print 'target scaffold interaction table'
    init_target_scaffold_interaction_tbl()