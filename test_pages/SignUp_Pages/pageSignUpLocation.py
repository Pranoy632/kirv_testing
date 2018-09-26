import sys
sys.path.append('../test_locators')

import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from Basepage import BasePage, fake
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpLocation(BasePage):

    def fill_fields(self):
        self.wait_for_element(SigninPageLocators.location_signUp_name1)

        loc_name1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_name1)
        loc_name1.send_keys(fake.street_name())

        loc_street1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_street_add1)
        loc_street1.send_keys(fake.building_number() +
                              " " + fake.street_name())

        loc_city1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_city1)
        loc_city1.send_keys(fake.city())

        self.driver.find_element(
            *SigninPageLocators.location_signUp_state1).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        loc_post_code1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_post_code1)
        loc_post_code1.send_keys(fake.postcode())

        loc_email1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_email1)
        loc_email1.send_keys(fake.email())

        loc_ph1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_phn1)
        loc_ph1.send_keys("12345678901")

        loc_other_phn1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_otherphn1)
        loc_other_phn1.send_keys("12345678902")

        self.driver.find_element(
            *SigninPageLocators.location_signUp_add_loc).click()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        loc_name2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_name2)
        loc_name2.send_keys(fake.street_name())

        loc_street2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_street_add2)
        loc_street2.send_keys(fake.building_number() +
                              " " + fake.street_name())

        loc_city2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_city2)
        loc_city2.send_keys(fake.city())

        self.driver.find_element(
            *SigninPageLocators.location_signUp_state2).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        loc_post_code2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_post_code2)
        loc_post_code2.send_keys(fake.postcode())

        loc_email2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_email2)
        loc_email2.send_keys(fake.email())

        loc_phn2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_phn2)
        loc_phn2.send_keys("12345678901")

        loc_other_phn2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_otherphn2)
        loc_other_phn2.send_keys("12345678902")

        self.driver.find_element(
            *SigninPageLocators.location_signUp_check2).click()

        self.driver.find_element(
            *SigninPageLocators.location_signUp_add_loc).click()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.location_signUp_delete3).click()

        self.wait_for_element(SigninPageLocators.location_signUp_del_modal)
        self.driver.find_element(
            *SigninPageLocators.location_signUp_del_modal).click()

        # time.sleep(1)
        # self.driver.execute_script(
        #     "window.scrollTo(document.body.scrollHeight, 0);")
        # time.sleep(1)

    def click_location_signup_button(self):
        time.sleep(1)
        loc = self.driver.find_element(
            *SigninPageLocators.loc_next_btn)
        loc.click()
