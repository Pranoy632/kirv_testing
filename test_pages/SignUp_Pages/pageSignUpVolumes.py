import sys
sys.path.append('../test_locators')

import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpVolumes(BasePage):

    def full_truck_q1_err(self):
        full_q1_er = self.driver.find_element(
            *SigninPageLocators.volumes_num_full_trucks_q1_err)
        print("signup volumes full truck q1 blank",  full_q1_er.is_displayed())
        return full_q1_er.is_displayed()

    def half_truck_q2_err(self):
        half_q2_er = self.driver.find_element(
            *SigninPageLocators.volumes_num_half_trucks_q2_err)
        print("signup volumes half truck q2 blank", half_q2_er.is_displayed())
        return half_q2_er.is_displayed()

    def full_truck_q2_err(self):
        full_q2_er = self.driver.find_element(
            *SigninPageLocators.volumes_num_full_trucks_q2_err)
        print("signup volumes full truck q2 blank",  full_q2_er.is_displayed())
        return full_q2_er.is_displayed()

    def fill_fields(self):

        # back button check from volumes to categories

        self.wait_for_element(
            SigninPageLocators.volumes_back_button)

        self.click_volumes_signup_back_btn()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(document.body.scrollHeight, 0);")
        time.sleep(1)

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        self.wait_for_element(
            SigninPageLocators.categories_signUp_next_btn)

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_next_btn).click()

        # volumes

        self.wait_for_element(
            SigninPageLocators.volumes_signUp_quarter_truck_q1)

        self.driver.find_element(
            *SigninPageLocators.volumes_signUp_quarter_truck_q1).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.volumes_signUp_half_truck_q1).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.volumes_signUp_check_q2).click()

        self.driver.find_element(
            *SigninPageLocators.volumes_signUp_quarter_truck_q2).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.volumes_signUp_acknowledge_check).click()

        self.click_volumes_signup_button()
        time.sleep(1)

        try:
            assert self.full_truck_q1_err()
        except:
            print("No result found for q1 full-truck")

        try:
            assert self.half_truck_q2_err()
        except:
            print("No result found for q2 half-truck")

        try:
            assert self.full_truck_q2_err()
        except:
            print("No result found for q2 full-truck")

        self.driver.find_element(
            *SigninPageLocators.volumes_signUp_full_truck_q1).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.volumes_signUp_half_truck_q2).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.volumes_signUp_full_truck_q2).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.click_volumes_signup_button()

    def click_volumes_signup_button(self):
        time.sleep(1)
        vol = self.driver.find_element(
            *SigninPageLocators.volumes_signUp_sub_app_btn)
        vol.click()

    def click_volumes_signup_back_btn(self):
        time.sleep(1)
        vol_back = self.driver.find_element(
            *SigninPageLocators.volumes_back_button)
        vol_back.click()
