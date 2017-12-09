import csv
from phin import models
from chembl import models as chembl_models
from datetime import datetime
import gzip


def load_mmp():
    mmp_data_file = '/home/zhonghua/Downloads/mmp/mmp-max-rm-missing-entityid.csv.gz'
    log_file = 'mmp.log'
    start_time = datetime.now()
    mmp_list = []
    for idx, row in enumerate(csv.DictReader(gzip.open(mmp_data_file))):
        #print idx
        if idx % 100000 == 0 and not idx == 0:
            st = datetime.now()
            print 'start loading ', idx
            models.MMP.objects.bulk_create(mmp_list)
            mmp_list = []
            print 'finished ', idx, datetime.now() - st

        tid = row['target_id']
        molregno1 = row['mol1_parent_id']
        molregno2 = row['mol2_parent_id']
        smi1 = row['mol1_diff']
        smi2 = row['mol2_diff']
        act1 = row['mol1_pchembl_value']
        act2 = row['mol2_pchembl_value']
        assay_id1 = row['mol1_assay_id']
        assay_id2 = row['mol2_assay_id']
        core = row['Col0 (RDKit Mol)']
        if act1 < act2:
            mmp = models.MMP(
                target_id=tid,
                LHMol_id=molregno1,
                RHMol_id=molregno2,
                LHAct=act1,
                RHAct=act2,
                LHAssay_id=assay_id1,
                RHAssay_id=assay_id2,
                transform='{0}>>{1}'.format(smi1, smi2),
                core=core
            )
        else:
            mmp = models.MMP(
                target_id=tid,
                LHMol_id=molregno2,
                RHMol_id=molregno1,
                LHAct=act2,
                RHAct=act1,
                LHAssay_id=assay_id2,
                RHAssay_id=assay_id1,
                transform='{0}>>{1}'.format(smi2, smi1),
                core=core

            )
        mmp_list.append(mmp)
    models.MMP.objects.bulk_create(mmp_list)
    print datetime.now() - start_time
