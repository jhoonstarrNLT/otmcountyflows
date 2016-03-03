import time
import datetime
import logging
from constants import ODSEGMENTS

ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d-%H_%M')

logFormatter = logging.Formatter("[%(asctime)s] [%(module)s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

from otm_gatherzips import *
from otm_unzip import *
from otm_cleanupfolders import *
from otm_arrangedata import *
from otm_createtable import *
from otm_writedata import *

