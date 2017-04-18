# sql expression for retrieving all valid pchembl value and the corresponding parent molecule
TARGET_PCHEMBL_ALL = """
SELECT 
  molecule_dictionary.molregno, 
  activities.pchembl_value, 
  molecule_hierarchy.parent_molregno
FROM 
  public.target_dictionary, 
  public.assays, 
  public.activities, 
  public.molecule_dictionary, 
  public.molecule_hierarchy
WHERE 
  assays.tid = target_dictionary.tid AND
  activities.assay_id = assays.assay_id AND
  activities.molregno = molecule_dictionary.molregno AND
  molecule_dictionary.molregno = molecule_hierarchy.molregno AND
  target_dictionary.tid = %s AND 
  activities.pchembl_value IS NOT NULL ;
"""
