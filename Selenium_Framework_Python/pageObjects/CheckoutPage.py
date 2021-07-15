from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOut:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    cart_button = (By.XPATH, "//div[@class='card h-100']/div/button")
    checkout_button = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    success_button = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def products_f(self):
        return self.driver.find_elements(*CheckOut.products)

    def cart_button_f(self):
        return self.driver.find_elements(*CheckOut.cart_button)

    def checkout_button_f(self):
        return self.driver.find_element(*CheckOut.checkout_button)

    def success_button_f(self):
        self.driver.find_element(*CheckOut.success_button).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage



