import pytest
from BaseClass import BaseClass1

class TestLogin(BaseClass1):
    def test_Login1(self):
        loggerobj=self.test_log1()
        loggerobj.debug("Debug will be displayed")
        loggerobj.info("Info will be displayed")
        loggerobj.critical("Critical will be displayed")
        loggerobj.error("Error will be displayed")