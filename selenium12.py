from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver.exe")
driver.get("https://www.python.org")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.close()