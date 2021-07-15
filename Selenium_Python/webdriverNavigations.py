from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver.get("https://www.youtube.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://www.youtube.com/feed/explore")
driver.back()
driver.minimize_window()
driver.refresh()
driver.close()
