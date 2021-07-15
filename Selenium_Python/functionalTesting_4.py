from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
shop = driver.find_element_by_css_selector("a[href*='/angularpractice/shop']")
driver.execute_script("arguments[0].click();", shop)
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    pname = product.find_element_by_xpath("div/h4/a").text
    print(pname)
    if pname == "Blackberry":
        product.find_element_by_xpath("div/button").click()
driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_css_selector("#country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
countries = driver.find_elements_by_css_selector("div[class='suggestions']")
for country in countries:
    if country.find_element_by_css_selector("a").text == "India":
        country.find_element_by_css_selector("a").click()
driver.find_element_by_css_selector("div[class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[value='Purchase']").click()
successText = driver.find_element_by_class_name("alert-success").text
assert "Success! Thank you!" in successText
driver.get_screenshot_as_file("scr.png")

