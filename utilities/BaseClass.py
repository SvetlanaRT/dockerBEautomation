import logging
import pytest

from util import *


@pytest.mark.usefixtures("setup")
class BaseClass:

  def log_error(self, e):
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logs/logfile.log')

    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.critical(e)



