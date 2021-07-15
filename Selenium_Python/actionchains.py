from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
menu = driver.find_element_by_css_selector("#mousehover")
action.move_to_element(menu).perform()
submenu = driver.find_element_by_link_text("Reload")
action.move_to_element(submenu).click().perform()

driver.find_element_by_css_selector("#show-textbox").click()
assert driver.find_element_by_css_selector("#displayed-text").is_displayed()
driver.find_element_by_css_selector("#hide-textbox").click()
assert not driver.find_element_by_css_selector("#displayed-text").is_displayed()
