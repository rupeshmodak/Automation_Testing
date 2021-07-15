import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
list1 = []
list2 = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector(".search-keyword").send_keys("ber")
time.sleep(4)
count = driver.find_elements_by_xpath("//div[@class='product']/div/button")
print(len(count))
products = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for product in products:
    product.click()
    list1.append(product.find_element_by_xpath("parent::div/parent::div/h4").text)
print(list1)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))
pcounts = driver.find_elements_by_xpath("//p[@class='product-name']")
for pcount in pcounts:
    list2.append(pcount.text)
print(list2)
assert list1 == list2
originalamount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
# time.sleep(5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
discountamount = driver.find_element_by_css_selector(".discountAmt").text
print(originalamount)
print(discountamount)
assert float(discountamount) < int(originalamount)
print(driver.find_element_by_css_selector("span.promoInfo").text)
summation = (driver.find_elements_by_xpath("//table[@class='cartTable']/tbody/tr/td[5]"))
sum = 0
for summ in summation:
    sum = sum + int(summ.text)
print(sum)
amount = int(driver.find_element_by_css_selector(".totAmt").text)
print(amount)
assert sum == amount
driver.close()


