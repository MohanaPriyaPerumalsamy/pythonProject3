from selenium.webdriver.common.by import By
class PageModel_AmazonSearchResultScreen:
    def __init__(self, driver):  # constructor
       self.driver = driver
       getItTodayCheckbox1 = (By.XPATH,"//*[@id='p_90/6741117031']/span/a/div/label/i")
    def getItTodayCheckbox(self):
        return self.driver.find_element(*PageModel_AmazonSearchResultScreen.getItTodayCheckbox1)
