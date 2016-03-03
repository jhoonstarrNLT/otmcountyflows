import os
import sys
import zipfile
from shutil import rmtree
from . import logger

def otm_unzip(zfiles):

    """Unzips a list of OTM analysis zips to their own folder"""

    if not zfiles:
        logger.error("No otm zipfiles available for extraction")
        sys.exit(1)

    extracted = []
    for zfile in zfiles:
        try:
            logger.debug("Extracting: {0}".format(zfile))
            filepath = os.path.abspath(zfile)
            basepath = os.path.dirname(filepath)
            basename = os.path.basename(zfile)
            noext = os.path.splitext(basename)[0]
            extractpath = os.path.join(basepath, noext)
            logger.debug("Destination: {0}".format(extractpath))

            if os.path.exists(extractpath):
                rmtree(extractpath)
            else:
                os.mkdir(extractpath)

            logger.debug("Unzipping all files")
            with zipfile.ZipFile(zfile, "r") as z:
                z.extractall(extractpath)

            extracted.append(extractpath)

        except Exception, e: 
            logger.error("Error unzipping: {0}".format(zfile))
            logger.error("Failed: {0}".format(str(e)))
            sys.exit(1)

    return extracted
