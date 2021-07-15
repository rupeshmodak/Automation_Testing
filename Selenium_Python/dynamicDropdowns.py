import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_css_selector("input[id='autosuggest']").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("a[class='ui-corner-all']")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
assert driver.find_element_by_css_selector("input[id='autosuggest']").get_attribute('value') == "India"
valuee = driver.find_element_by_css_selector("input[id='autosuggest']").get_attribute('value')
print(valuee)
