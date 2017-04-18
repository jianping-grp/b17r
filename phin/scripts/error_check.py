from chembl import models as chembl_models


def check_molecule_hierarchy():
    with open('phin/scripts/data/molecule_hierarchy_2.txt', 'w') as w:
        for mol in chembl_models.MoleculeDictionary.objects.all():
            if not len(mol.striped_molecule.all()) == 1:
                w.write(str(mol.molregno) + ' ' + str(len(mol.striped_molecule.all())) + '\n')


