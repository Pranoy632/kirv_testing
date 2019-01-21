from pages.basepage import *
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import WareHouseLocators
from .location import cities

class WareHouse(BasePage):

    def elements_of_warehouse(self):
        print(self.driver.find_element(*WareHouseLocators.check_first_retail_location).text)
        print(cities[0])
        self.subset_assert(self.driver.find_element(
            *WareHouseLocators.check_first_retail_location).text, cities)

        self.subset_assert(self.driver.find_element(
            *WareHouseLocators.check_second_retail_location).text, cities)

        self.negative_retail_checklist_test()
        self.positive_retail_checklist_test()

    def negative_retail_checklist_test(self):
        """
            checks all combiations of retail location checklist
        """
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
        time.sleep(1)
  
        self.driver.find_element(
            *WareHouseLocators.back_a_step).click()
        time.sleep(1)

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
            *WareHouseLocators.confirm_btn).click()

        self.driver.find_element(
            *WareHouseLocators.no_additional_warehouse_btn).click()

        self.subset_assert("Step 4 of 5 - Purchasing preferences",
            self.driver.find_element(*WareHouseLocators.purchasing_preferences).text)

        self.driver.find_element(
            *WareHouseLocators.back_a_step).click()

        self.equality_assert(
            self.driver.find_element(*WareHouseLocators.no_additional_warehouse_btn).is_displayed(), True)

        self.driver.find_element(
            *WareHouseLocators.back_a_step).click()

    def positive_retail_checklist_test(self):
        """
            selects one of the retail location
        """
        self.driver.find_element(
            *WareHouseLocators.check_first_retail_location).click()

        self.driver.find_element(
            *WareHouseLocators.confirm_btn).click()
