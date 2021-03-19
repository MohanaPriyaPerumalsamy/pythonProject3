import time
import pytest
from BaseClass import BaseClass2
from PageModel_FlipkartSearch import PageModel_FlipkartSearch
from PageModel_AmazonSearchResultSceen import PageModel_AmazonSearchResultScreen
@pytest.mark.usefixture("setup")
class TestFirstClass:
    def test_First(self,setup):
        SearchFlipkart=PageModel_FlipkartSearch(self.driver)  #object creation to get the "search" object from Page object class
        SearchFlipkart.searchItems().send_keys("LG")
        time.sleep(10)
        searchImageIconobj = PageModel_FlipkartSearch(self.driver)  # object creation to get the "searchImageIcon" object from Page object class
        searchImageIconobj.searchImageIcon().click()
        time.sleep(10)
        getItTodayobj=PageModel_AmazonSearchResultScreen(self.driver)
        getItTodayobj.getItTodayCheckbox().click()
        time.sleep(10)