import os
import sys
import csv
from . import logger, ODSEGMENTS

def otm_arrangedata(folds, year, jobtype='s000'):
    if jobtype not in ODSEGMENTS.keys():
        logger.warning("Jobtype not available: {0}")
        logger.warning("Reverting to default s000")
        jobtype = 's000'

    if not year:
        logger.error("No year set")
        sys.exit(1)

    if not folds:
        logger.error("No folders passed for arrangement")
        sys.exit(1)
    
    logger.debug("Processing folders and arranging data")
    final_data = {}
    for fold in folds:
        try:
            with open(os.path.join(fold, "selection.csv"),"rb") as sel, open(os.path.join(fold, "polygon_{0}.csv".format(year)), "rb") as poly:
                polygon_data = {}

                logger.debug("Processing selection csv")
                sreader = csv.reader(sel)
                sheader = next(sreader)
                snameindex = sheader.index("shape_name")
                sdata = next(sreader)[snameindex]

                logger.debug("Processing polygon csv")
                preader = csv.reader(poly)
                pheader = next(preader)
                pdataindex = pheader.index(jobtype)
                pnameindex = pheader.index("label")

                for row in preader:
                    polygon_data[row[pnameindex]] = row[pdataindex]

                final_data[sdata] = polygon_data
                
        except Exception, e:
            logger.error("Error arranging: {0}".format(fold))
            logger.error("Failed: {0}".format(str(e)))

    return final_data

