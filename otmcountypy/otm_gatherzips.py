import os
from . import logger

def otm_gatherzips(fold):

    """Gathers OTM zip files"""

    try:
        zipfiles = []
        logger.debug("Gathering OTM zipfiles in: {0}".format(fold))
        filepath = os.path.abspath(fold)
        for file in os.listdir(filepath):
            if file.startswith("otm_") and file.endswith(".zip"):
                zipfiles.append(os.path.join(filepath, file))
        return zipfiles

    except Exception, e:
        logger.error("Error gathering: {0}".format(fold))
        logger.error("Failed: {0}".format(str(e)))
