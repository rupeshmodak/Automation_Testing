import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector(".search-keyword").send_keys("ber")
time.sleep(4)
count = driver.find_elements_by_xpath("//div[@class='product']/div/button")
print(len(count))
products = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for product in products:
    product.click()
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)


