from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=eu")
driver.find_element_by_css_selector("#username").send_keys("rupeshmodak")
driver.find_element_by_xpath("//*[contains(@class,'password')]").send_keys("pappumaster")
driver.find_element_by_xpath("//*[contains(@class,'password')]").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//div[@id='usernamegroup']/label").text)
print(driver.find_element_by_css_selector("div[id='usernamegroup'] label").text)
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
#print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)

