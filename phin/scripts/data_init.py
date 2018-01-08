from phin.models import *
from chembl import models as chembl_models
from rdkit import Chem
from rdkit.Chem.Scaffolds import MurckoScaffold
from django_rdkit.models import *
import itertools as it
from django.db import connection


def init_phin_molecule_tbl():
    # log rdkit-invalid molecule
    with open('phin/scripts/log/rdkit-invalid-mol.txt', 'w') as w:
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


def init_molecule_interaction_tbl():
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
            # MoleculeInteraction.objects.bulk_create(
            #     MoleculeInteraction(
            #         first_molecule_id=molid_1,
            #         second_molecule_id=molid_2,
            #         target_id=x['target_id'],
            #         min=x['min'],
            #         max=x['max'],
            #         mean=x['mean'],
            #         median=x['median']
            #     ) for idx, x in mol1.get_common_activities(molid_2).iterrows()
            # )

    # for target in Target.objects.all():
    #     print target.target_id
    #     if target.tid.target_type_id in ['ADMET', 'NO TARGET', 'UNCHECKED', 'UNDEFINED', 'UNKNOWN']:
    #         continue
    #     for act1, act2 in it.combinations(target.activities_set.filter(mean__gte=5).all(), 2):
    #         if act1.molecule_id > act2.molecule_id:
    #             act1, act2 = act2, act1
    #             # act_list.append((act2, act1))
    #         try:
    #             mi = MoleculeInteraction.objects.get(
    #                 first_molecule_id=act1.molecule_id,
    #                 second_molecule_id=act2.molecule_id
    #             )
    #             mi.target.append(target.target_id)
    #             mi.min.append(min(act1.min, act2.min))
    #             mi.max.append(min(act1.max, act2.max))
    #             mi.mean.append(min(act1.mean, act2.mean))
    #             mi.median.append(min(act1.median, act2.median))
    #         except MoleculeInteraction.DoesNotExist:
    #             mi = MoleculeInteraction.objects.create(
    #                 first_molecule_id=act1.molecule_id,
    #                 second_molecule_id=act2.molecule_id,
    #                 target=[target.target_id],
    #                 min=[min(act1.min, act2.min)],
    #                 max=[min(act1.max, act2.max)],
    #                 mean=[min(act1.mean, act2.mean)],
    #                 median=[min(act1.median, act2.median)]
    #             )
    #         mi.save()

    # MoleculeInteraction.objects.bulk_create(
    #     [
    #         MoleculeInteraction(
    #             first_molecule_id=x1.molecule_id,
    #             second_molecule_id=x2.molecule_id,
    #             target_id=target.target_id,
    #             min=min(x1.min, x2.min),
    #             max=min(x1.max, x2.max),
    #             mean=min(x1.mean, x2.mean),
    #             median=min(x1.median, x2.median)
    #         ) for x1, x2 in act_list
    #     ]
    # )


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
