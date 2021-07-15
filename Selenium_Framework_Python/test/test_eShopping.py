from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class Testframe1(BaseClass):
    def test_frame1(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkout = homepage.shopitems()
        log.info("Cart items names as follows :")
        products = checkout.products_f()
        i = -1
        for product in products:
            i = i + 1
            pname = product.text
            log.info(pname)
            if pname == "Blackberry":
                checkout.cart_button_f()[i].click()
        checkout.checkout_button_f().click()
        checkout.success_button_f()
        self.driver.find_element_by_css_selector("#country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyelementpresence("India")
        countries = self.driver.find_elements_by_css_selector("div[class='suggestions']")
        for country in countries:
            if country.find_element_by_css_selector("a").text == "India":
                country.find_element_by_css_selector("a").click()
        self.driver.find_element_by_css_selector("div[class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("input[value='Purchase']").click()
        successtext = self.driver.find_element_by_class_name("alert-success").text
        log.info("Success message is shown as "+successtext)
        assert "Success! Thank you!" in successtext
        self.driver.get_screenshot_as_file("scr.png")
