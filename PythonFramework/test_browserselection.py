import pytest
from BaseClass import BaseClass2

@pytest.mark.usefixture("setup")
class TestFirstClass:
    def test_First(self,setup):
        self.driver.find_element_by_name("Passwd").send_keys("India")