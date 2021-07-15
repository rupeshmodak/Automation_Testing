from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("input[name='name']").send_keys("Rupesh Modak")
driver.find_element_by_css_selector("input[name='email']").send_keys("rupeshmodak@gmail.com")
driver.find_element_by_css_selector("input[id='exampleCheck1']").click()
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
driver.find_element_by_xpath("//input[@type='submit']").click()
#print(driver.find_element_by_css_selector("[class*='alert-success']").text)
print(driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text)
