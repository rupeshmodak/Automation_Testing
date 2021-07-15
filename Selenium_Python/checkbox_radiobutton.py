from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radiobuttons = driver.find_elements_by_xpath("//input[@class='radioButton']")
#radiobuttons[2].click()
for i in radiobuttons:
    if i.get_attribute('value') == "radio3":
        i.click()
        assert i.is_selected()
