from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Rupesh Modak"
driver.find_element_by_id("name").send_keys(name)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
assert name in alert.text
alert.accept()
driver.find_element_by_css_selector("#confirmbtn").click()
print(alert.text)
alert.dismiss()
