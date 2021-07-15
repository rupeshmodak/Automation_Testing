from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Rupesh")
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shop = driver.find_element_by_css_selector("a[href*='angularpractice/shop']")
driver.execute_script("arguments[0].click();", shop)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
