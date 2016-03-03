from . import logger
import os
from shutil import rmtree


def otm_cleanupfolders(foldlist):

    """Removes created OTM folders"""

    if not foldlist:
        logger.error("No OTM folders to remove")
        sys.exit(1)

    logger.debug("Removing folders")
    for fold in foldlist:
        try:
            if os.path.isdir(fold):
                rmtree(fold)

        except Exception, e:
            logger.error("Error removing: {0}".format(fold))
            logger.error("Failed: {0}".format(str(e)))
