from pages.basepage import *
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import LocationLocators


class Location(BasePage):

    def element_in_location_page(self):
        self.driver.find_element(
            *LocationLocators.location_num).click()

        self.asserts(self.is_button_enabled(LocationLocators.add_loc_btn), 'true')

        self.driver.find_element(
            *LocationLocators.enter_manually).click()

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.loc_name_input).send_keys('loc1')

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.address_input).send_keys('address')

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.city_input).send_keys('test city')

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.state_input).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.zip_code_input).send_keys('786')

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.add_loc_btn).click()

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.email_address_input).send_keys('test@test.com')

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.phone_number_input).send_keys('12345678901')

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.next_btn).click()

    def is_button_enabled(self, button):
        return self.driver.find_element(*button).is_enabled()

    def asserts(self, first_arg, second_arg):
        assert first_arg == second_arg
