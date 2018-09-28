import sys
sys.path.append('../test_locators')

import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpCategories(BasePage):

    def categories_stove_err(self):
        stove_er = self.driver.find_element(
            *SigninPageLocators.categories_cooking_stove_er)
        print(" stove blank",  stove_er.is_displayed())
        return stove_er.is_displayed()

    def categories_combo_err(self):
        combo_er = self.driver.find_element(
            *SigninPageLocators.categories_laundry_combo_er)
        print(" combo blank",  combo_er.is_displayed())
        return combo_er.is_displayed()

    def categories_dryer_err(self):
        dryer_er = self.driver.find_element(
            *SigninPageLocators.categories_laundry_dryer_er)
        print(" dryer blank",  dryer_er.is_displayed())
        return dryer_er.is_displayed()

    def categories_compactor_err(self):
        compactor_er = self.driver.find_element(
            *SigninPageLocators.categories_other_compactor_er)
        print(" compactor blank",  compactor_er.is_displayed())
        return compactor_er.is_displayed()

    def categories_icemaker_err(self):
        ice_er = self.driver.find_element(
            *SigninPageLocators.categories_refrigeration_icemaker_er)
        print(" icemaker blank",  ice_er.is_displayed())
        return ice_er.is_displayed()

    def categories_freezer_err(self):
        freezer_er = self.driver.find_element(
            *SigninPageLocators.categories_refrigeration_freezer_er)
        print(" freezer blank",  freezer_er.is_displayed())
        return freezer_er.is_displayed()

    def fill_fields(self):
        self.wait_for_element(
            SigninPageLocators.categories_signUp_cook_microwave)

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_cook_microwave).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_cook_oven).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_cook_hood).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_dish_dishwasher).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_laundry_washer).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_laundry_pedestal).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_other_garbage).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_refrigeration_refrigerator).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.click_categories_signup_button()
        time.sleep(1)

        try:
            assert self.categories_stove_err()
        except:
            print("No result found for cooking stove")

        try:
            assert self.categories_combo_err()
        except:
            print("No result found for laundry combo")

        try:
            assert self.categories_dryer_err()
        except:
            print("No result found for laundry dryer")

        try:
            assert self.categories_compactor_err()
        except:
            print("No result found for other compactor")

        try:
            assert self.categories_icemaker_err()
        except:
            print("No result found for refrigeration icemaker")

        try:
            assert self.categories_freezer_err()
        except:
            print("No result found for refrigeration freezer")

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(document.body.scrollHeight, 0);")
        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_cook_stove).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_laundry_combo).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_laundry_dryer).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_other_compactor).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_refrigeration_icemaker).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_refrigeration_freezer).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.click_categories_signup_button()

    def click_categories_signup_button(self):
        time.sleep(1)
        categories = self.driver.find_element(
            *SigninPageLocators.categories_signUp_next_btn)
        categories.click()
