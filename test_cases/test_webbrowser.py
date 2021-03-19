from selenium import webdriver

def test_webbrowser():
   driver = webdriver.Chrome(executable_path="D:\\Mohana2020\\Python\\Python_selenium\\setup\\Drivers\\Chrome\\chromedriver.exe")
   driver.get("https://www.google.com")
   driver.maximize_window()