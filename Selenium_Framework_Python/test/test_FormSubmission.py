import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from testdata.TestData import TestData


class TestForm(BaseClass):
    def test_formsubmit(self, getdata):
        log = self.getLogger()
        homepg = HomePage(self.driver)
        log.info("Name of the user is "+getdata["name"])
        homepg.form_name().send_keys(getdata["name"])
        homepg.form_email().send_keys(getdata["email"])
        homepg.form_check().click()
        self.select(homepg.form_drop(), getdata["gender"])
        homepg.form_submit().click()
        # print(driver.find_element_by_css_selector("[class*='alert-success']").text)
        print(homepg.form_success().text)
        self.driver.refresh()

    @pytest.fixture(params=TestData.testdatavariable)
    # @pytest.fixture(params=TestData.get_TestData("TestCase2"))
    def getdata(self, request):
        return request.param
