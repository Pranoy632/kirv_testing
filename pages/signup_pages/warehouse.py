from pages.basepage import *
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import WareHouseLocators


class WareHouse(BasePage):

    def elements_of_warehouse(self):

        self.driver.find_element(
            *WareHouseLocators.check_first_retail_location).click()

        self.driver.find_element(
            *WareHouseLocators.check_second_retail_location).click()

        time.sleep(2)
        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.check_first_retail_location_id).is_selected(), True)

        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.check_second_retail_location_id).is_selected(), True)

        self.driver.find_element(
            *WareHouseLocators.check_none_retail_location).click()

        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.check_none_retail_location_id).is_selected(), True)

        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.check_first_retail_location_id).is_selected(), False)

        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.check_second_retail_location_id).is_selected(), False)

        self.driver.find_element(
            *WareHouseLocators.confirm_btn).click()

        self.driver.find_element(
            *WareHouseLocators.no_additional_warehouse_btn).click()
