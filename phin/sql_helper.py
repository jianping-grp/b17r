# sql expression for retrieving all valid pchembl value and the corresponding parent molecule
TARGET_PCHEMBL_ALL = """
    SELECT 
      molecule_dictionary.molregno, 
      activities.pchembl_value::FLOAT , 
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

TARGET_COMMON_ACTIVITY = """
    SELECT 
      act1.molecule_id,
      least(act1.min, act2.min),
      least(act1.max, act2.max),
      least(act1.mean, act2.mean),
      least(act1.median, act2.median)
    FROM 
      public.phin_activities as act1, 
      public.phin_activities as act2
    WHERE 
      act1.molecule_id = act2.molecule_id
    AND
    act1.target_id = %s AND act2.target_id = %s
      ;
"""

TARGET_SCAFFOLD_ACTIVITIES = """
    SELECT 
      MIN(phin_activities.mean) as min,
      AVG(phin_activities.mean) as mean, 
      MAX(phin_activities.mean) as max,
      median(phin_activities.mean::numeric) as median,
      COUNT(phin_activities.mean) as count,
      phin_scaffold.scaffold_id
    FROM 
      public.phin_target, 
      public.phin_molecule, 
      public.phin_scaffold, 
      public.phin_activities
    WHERE 
      phin_target.target_id = phin_activities.target_id AND
      phin_scaffold.scaffold_id = phin_molecule.scaffold_id AND
      phin_activities.molecule_id = phin_molecule.mol_id AND
      phin_target.target_id = %s
    GROUP BY 
    phin_scaffold.scaffold_id
     ;
"""


TARGET_COMMON_SCAFFOLD_ACTIVITY = """
    SELECT 
      act1.scaffold_id,
      least(act1.min, act2.min),
      least(act1.max, act2.max),
      least(act1.mean, act2.mean),
      least(act1.median, act2.median)
    FROM 
      public.phin_scaffoldactivities as act1, 
      public.phin_scaffoldactivities as act2
    WHERE 
      act1.scaffold_id = act2.scaffold_id
    AND
    act1.target_id = %s AND act2.target_id = %s
      ;
"""