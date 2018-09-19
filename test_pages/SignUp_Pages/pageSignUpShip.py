import sys
sys.path.append('../test_locators')

import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from .Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpShipTo(BasePage):

    def fill_fields(self):
        self.wait_for_element(SigninPageLocators.ship_signUp_start_time)

        self.driver.find_element(
            *SigninPageLocators.ship_signUp_start_time).click()

        self.wait_for_element(SigninPageLocators.ship_start_time)

        self.driver.find_element(
            *SigninPageLocators.ship_start_time).click()

        self.driver.find_element(
            *SigninPageLocators.ship_ok_btn_start_end).click()

        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.ship_signUp_end_time).click()

        self.wait_for_element(SigninPageLocators.ship_end_time)

        self.driver.find_element(
            *SigninPageLocators.ship_end_time).click()

        self.driver.find_element(
            *SigninPageLocators.ship_ok_btn_start_end).click()

        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.ship_signUp_add_ship).click()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.ship_signUp_delete2).click()

        self.wait_for_element(SigninPageLocators.ship_signUp_del_modal)
        self.driver.find_element(
            *SigninPageLocators.ship_signUp_del_modal).click()

    def click_ship_signup_button(self):
        time.sleep(1)
        ship = self.driver.find_element(
            *SigninPageLocators.ship_next_btn)
        ship.click()
