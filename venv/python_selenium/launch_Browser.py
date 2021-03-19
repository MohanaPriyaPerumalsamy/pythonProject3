# from selenium import webdriver
# driver=webdriver.Chrome(executable_path="D:\\Mohana2020\\Python\\Python_selenium\\setup\\Drivers\\Chrome\\chromedriver.exe")
# driver.get("https://www.google.com")
# print(driver.title)
# print(driver.current_url)
# driver.maximize_window()
# driver.minimize_window()
# driver.close()



from selenium import webdriver
driver=webdriver.Firefox(executable_path="D:\\Mohana2020\\Python\\Python_selenium\\setup\\Drivers\\firefox\\geckodriver.exe")
#driver.get("https://www.google.com")
driver.get("https://in.bookmyshow.com/")
# print(driver.title)
# print(driver.current_url)
# driver.maximize_window()
# driver.minimize_window()
driver.back()
driver.implicitly_wait(10)
driver.refresh()
# driver.close()



from selenium import webdriver
driver=webdriver.Edge(executable_path="D:\\Mohana2020\\Python\\Python_selenium\\setup\\Drivers\\edge\\msedgedriver.exe")
#driver.get("https://www.google.com")
driver.get("https://in.bookmyshow.com/")
# print(driver.title)
# print(driver.current_url)
# driver.maximize_window()
# driver.minimize_window()
# driver.back()
# driver.implicitly_wait(10)
# driver.refresh()
# driver.close()