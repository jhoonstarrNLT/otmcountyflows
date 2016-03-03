import csv
from . import logger

def otm_writedata(dat, fyle):

    if not dat:
        logger.error("No data passed for output")
        sys.exit(1)

    if not fyle:
        logger.error("No output file passed")
        sys.exit(1)

    try:
        with open(fyle, 'wb') as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL)

            for item in dat:
                wr.writerow(item)

                    
    except Exception, e:
        logger.error("Error writing data")
        logger.error("Failed: {0}".format(str(e)))

