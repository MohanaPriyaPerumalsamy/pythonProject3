import inspect
import logging

import pytest


class BaseClass1:
    def test_log1(self):
        loggername=inspect.stack()[1][3]
        logger=logging.getLogger(loggername)
        #logger=logging.getLogger(--name--)
        filehander=logging.FileHandler("logfile.log")
        formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        filehander.setFormatter(formatter)
        logger.addHandler(filehander)
        logger.setLevel(logging.DEBUG)
        return logger

@pytest.mark.usefixture("setup")
class BaseClass2:
    pass