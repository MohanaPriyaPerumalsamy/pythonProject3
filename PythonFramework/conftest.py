import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browsername", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    browsername=request.config.getoption("browsername")
    if browsername=="chrome":
        driver=webdriver.Chrome(executable_path=r"D:\Mohana2020\Python\Python_selenium\setup\Drivers\Chrome\chromedriver.exe")
    elif browsername=="firefox":
        driver = webdriver.Chrome(executable_path=r"D:\Mohana2020\Python\Python_selenium\setup\Drivers\Chrome\chromedriver.exe")
   # driver.get("https://accounts.google.com/signup/v2/webcreateaccount?hl=en-GB&flowName=GlifWebSignIn&flowEntry=SignUp")
    driver.get("https://www.amazon.in/")

    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
