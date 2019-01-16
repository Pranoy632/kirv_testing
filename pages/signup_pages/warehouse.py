from pages.basepage import *
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import WareHouseLocators


class WareHouse(BasePage):

    def elements_of_warehouse(self):

        self.driver.find_element(
            *WareHouseLocators.check_retail_locartion).click()

        self.driver.find_element(
            *WareHouseLocators.confirm_btn).click()

        self.driver.find_element(
            *WareHouseLocators.no_additional_warehouse_btn).click()
