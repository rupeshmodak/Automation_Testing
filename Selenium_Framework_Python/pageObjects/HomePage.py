from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOut


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='/angularpractice/shop']")

    def __init__(self, driver):
        self.driver = driver

    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout = CheckOut(self.driver)
        return checkout

    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    check = (By.CSS_SELECTOR, "input[id='exampleCheck1']")
    drop = (By.ID, "exampleFormControlSelect1")
    sub = (By.XPATH, "//input[@type='submit']")
    success = (By.XPATH, "//*[contains(@class,'alert-success')]")

    def form_name(self):
        return self.driver.find_element(*HomePage.name)

    def form_email(self):
        return self.driver.find_element(*HomePage.email)

    def form_check(self):
        return self.driver.find_element(*HomePage.check)

    def form_drop(self):
        return self.driver.find_element(*HomePage.drop)

    def form_submit(self):
        return self.driver.find_element(*HomePage.sub)

    def form_success(self):
        return self.driver.find_element(*HomePage.success)





