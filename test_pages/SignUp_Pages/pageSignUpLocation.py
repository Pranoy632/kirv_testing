import sys
sys.path.append('../test_locators')

import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpLocation(BasePage):

    def fill_fields(self):
        time_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.wait_for_element(SigninPageLocators.location_signUp_name1)

        self.driver.find_element(
            *SigninPageLocators.location_signUp_name1).send_keys("Amz1")
        self.driver.find_element(
            *SigninPageLocators.location_signUp_street_add1).send_keys("Bake-street, st-111")
        self.driver.find_element(
            *SigninPageLocators.location_signUp_city1).send_keys("colorado")
        self.driver.find_element(
            *SigninPageLocators.location_signUp_state1).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.location_signUp_post_code1).send_keys("12345")
        self.driver.find_element(
            *SigninPageLocators.location_signUp_email1).send_keys("amazatic" + "+" + time_now + "@amazatic.com")
        self.driver.find_element(
            *SigninPageLocators.location_signUp_phn1).send_keys("12345678901")
        self.driver.find_element(
            *SigninPageLocators.location_signUp_otherphn1).send_keys("12345678902")

        self.driver.find_element(
            *SigninPageLocators.location_signUp_add_loc).click()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.location_signUp_name2).send_keys("Amz2")
        self.driver.find_element(
            *SigninPageLocators.location_signUp_street_add2).send_keys("Bake-street, st-222")
        self.driver.find_element(
            *SigninPageLocators.location_signUp_city2).send_keys("Michigan")

        self.driver.find_element(
            *SigninPageLocators.location_signUp_state2).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.location_signUp_post_code2).send_keys("12345")
        self.driver.find_element(
            *SigninPageLocators.location_signUp_email2).send_keys("amazatic" + "+" + time_now + "@amazatic.com")
        self.driver.find_element(
            *SigninPageLocators.location_signUp_phn2).send_keys("12345678901")
        self.driver.find_element(
            *SigninPageLocators.location_signUp_otherphn2).send_keys("12345678902")
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

    def click_location_signup_button(self):
        time.sleep(1)
        loc = self.driver.find_element(
            *SigninPageLocators.loc_next_btn)
        loc.click()
