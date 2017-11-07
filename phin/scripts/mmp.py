from rdkit import Chem
#from phin import models
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    database='chembl_23',
    user='zhonghua',
    password='nankai'
)
cursor = conn.cursor()

TARGET_PCHEMBL_ACTIVITIES = """
SELECT 
  target_dictionary.tid, 
  assays.assay_id, 
  activities.activity_id, 
  molecule_dictionary.molregno, 
  activities.standard_type, 
  activities.pchembl_value, 
  molecule_dictionary.max_phase, 
  compound_structures.canonical_smiles
FROM 
  public.activities, 
  public.assays, 
  public.molecule_dictionary, 
  public.target_dictionary, 
  public.compound_structures, 
  public.molecule_hierarchy
WHERE 
  activities.assay_id = assays.assay_id AND
  molecule_dictionary.molregno = activities.molregno AND
  molecule_dictionary.molregno = molecule_hierarchy.molregno AND
  target_dictionary.tid = assays.tid AND
  molecule_hierarchy.parent_molregno = compound_structures.molregno AND
  activities.pchembl_value > 0 AND 
  target_dictionary.tid = %s;
"""


def get_all_active_molecule(target_id):
    cursor.execute(TARGET_PCHEMBL_ACTIVITIES, (target_id,))
    activity_df = pd.DataFrame(
        cursor.fetchall(),
        columns=[
            'tid', 'assay_id', 'activity_id',
            'molregno', 'standard_type', 'pchembl_value', 'max_phase', 'canonical_smiles'
        ]
    )
    print activity_df
    gb = activity_df.groupby(['molregno', 'standard_type']).agg({'pchembl_value': 'mean'})
    print gb



get_all_active_molecule(1)
