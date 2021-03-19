import pytest

from BaseClass import BaseClass2

@pytest.mark.usefixture("setup")
class TestFirstClass(BaseClass2):
    def test_First(self,setup):
        self.driver.find_element_by_name("passwd").send_keys("India")