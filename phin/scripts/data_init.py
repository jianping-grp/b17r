from phin.models import *
from chembl import models as chembl_models
from rdkit import Chem
from rdkit.Chem.Scaffolds import MurckoScaffold
from django_rdkit.models import *


def init_phin_molecula_tbl():
    # log rdkit-invalid molecule
    with open('phin/scripts/log/rdkit-invalid-mol.txt', 'w') as w:
        mol_set = chembl_models.MoleculeDictionary.objects.all()
        for idx, mol in enumerate(mol_set.iterator()):
            if mol.as_child_molecule.all():
                # get parent molecule (rm salt)
                mol = mol.as_child_molecule.all()[0].parent_molregno
            if not mol.compoundstructures_set.all():
                w.write('\t'.join(['NS', str(idx), str(mol.molregno), '\n']))
                continue
            smiles = mol.compoundstructures_set.all()[0].canonical_smiles
            phin_mol, created = Molecule.objects.get_or_create(molregno=mol)
            try:
                rdkit_mol = Chem.MolFromSmiles(smiles)
                phin_mol.structure = rdkit_mol
            except:
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
    for target in Target.objects.all():
        for item in target.get_activities_pchembl_list():
            pass
