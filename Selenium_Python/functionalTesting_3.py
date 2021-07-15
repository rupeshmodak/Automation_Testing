import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
list1 = []
strn = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector(".search-keyword").send_keys("ma")
time.sleep(4)
products = driver.find_elements_by_xpath("//div[@class='product']")
pcount = len(products)
print(pcount)
productnames = driver.find_elements_by_xpath("//h4[@class='product-name']")
for pname in productnames:
    list1.append(pname.text)
print(list1)
listcount = len(list1)
assert pcount == listcount