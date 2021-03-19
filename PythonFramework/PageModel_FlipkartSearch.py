from selenium.webdriver.common.by import By
class PageModel_FlipkartSearch:

    def __init__(self,driver): #constructor
        self.driver=driver

        searchEditBox=(By.XPATH,"//*[@id='twotabsearchtextbox']")
        searchImageIcon1=(By.XPATH,"//*[@id='nav-search-submit-button']")

        def searchItems(self):
            return self.driver.find_element(*PageModel_FlipkartSearch.searchEditBox)
        def searchImageIcon(self):
            return self.driver.find_element(*PageModel_FlipkartSearch.searchImageIcon1)
