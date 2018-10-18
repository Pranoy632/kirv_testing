import sys
sys.path.append('../test_locators')

import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators

categoriesInfo = {}

class SignUpCategories(BasePage):


    def categories_stove_err(self):
        stove_er = self.driver.find_element(
            *SigninPageLocators.categories_cooking_stove_er)
        return stove_er.is_displayed()

    def categories_combo_err(self):
        combo_er = self.driver.find_element(
            *SigninPageLocators.categories_laundry_combo_er)
        return combo_er.is_displayed()

    def categories_dryer_err(self):
        dryer_er = self.driver.find_element(
            *SigninPageLocators.categories_laundry_dryer_er)
        return dryer_er.is_displayed()

    def categories_compactor_err(self):
        compactor_er = self.driver.find_element(
            *SigninPageLocators.categories_other_compactor_er)
        return compactor_er.is_displayed()

    def categories_icemaker_err(self):
        ice_er = self.driver.find_element(
            *SigninPageLocators.categories_refrigeration_icemaker_er)
        return ice_er.is_displayed()

    def categories_freezer_err(self):
        freezer_er = self.driver.find_element(
            *SigninPageLocators.categories_refrigeration_freezer_er)
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
        print ('1) microwave: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_cook_microwave).get_attribute('value'))
        categoriesInfo['microwave'] = self.driver.find_element(*SigninPageLocators.categories_signUp_cook_microwave).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_cook_oven).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('2) oven: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_cook_oven).get_attribute('value'))
        categoriesInfo['oven'] = self.driver.find_element(*SigninPageLocators.categories_signUp_cook_oven).get_attribute('value')


        self.driver.find_element(
            *SigninPageLocators.categories_signUp_cook_hood).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('3) hood: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_cook_hood).get_attribute('value'))
        categoriesInfo['hood'] = self.driver.find_element(*SigninPageLocators.categories_signUp_cook_hood).get_attribute('value')

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
        print ('4) dishwasher: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_dish_dishwasher).get_attribute('value'))
        categoriesInfo['dishwasher'] = self.driver.find_element(*SigninPageLocators.categories_signUp_dish_dishwasher).get_attribute('value') 

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_laundry_washer).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('5) laundry_washer: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_laundry_washer).get_attribute('value'))
        categoriesInfo['laundry_washer'] = self.driver.find_element(*SigninPageLocators.categories_signUp_laundry_washer).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_laundry_pedestal).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('6) laundry_pedestal: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_laundry_pedestal).get_attribute('value'))
        categoriesInfo['laundry_pedestal'] = self.driver.find_element(*SigninPageLocators.categories_signUp_laundry_pedestal).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_other_garbage).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('7) garbage_cabinet: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_other_garbage).get_attribute('value'))
        categoriesInfo['garbage_cabinet'] = self.driver.find_element(*SigninPageLocators.categories_signUp_other_garbage).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_refrigeration_refrigerator).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('8) refrigeration: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_refrigeration_refrigerator).get_attribute('value'))
        categoriesInfo['refrigerator'] = self.driver.find_element(*SigninPageLocators.categories_signUp_refrigeration_refrigerator).get_attribute('value')

        self.click_categories_signup_button()
        time.sleep(1)

        try:
            assert self.categories_stove_err() == True
            print("Success: signup categories cooking stove blank error found.")
        except:
            print("No result found for cooking stove")

        try:
            assert self.categories_combo_err() == True
            print("Success: signup categories laundry combo blank error found.")
        except:
            print("No result found for laundry combo")

        try:
            assert self.categories_dryer_err() == True
            print("Success: signup categories laundry dryer blank error found.")
        except:
            print("No result found for laundry dryer")

        try:
            assert self.categories_compactor_err() == True
            print("Success: signup categories other compactor blank error found.")
        except:
            print("No result found for other compactor")

        try:
            assert self.categories_icemaker_err() == True
            print("Success: signup categories refrigeration icemaker blank error found.")
        except:
            print("No result found for refrigeration icemaker")

        try:
            assert self.categories_freezer_err() == True
            print("Success: signup categories refrigeration freezer blank error found.")
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
        print ('9) stove: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_cook_stove).get_attribute('value'))
        categoriesInfo['stove'] = self.driver.find_element(*SigninPageLocators.categories_signUp_cook_stove).get_attribute('value')

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
        print ('10) laundry_combo: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_laundry_combo).get_attribute('value'))
        categoriesInfo['laundry_combo'] = self.driver.find_element(*SigninPageLocators.categories_signUp_laundry_combo).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_laundry_dryer).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('11) laundry_dryer: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_laundry_dryer).get_attribute('value'))
        categoriesInfo['laundry_dryer'] = self.driver.find_element(*SigninPageLocators.categories_signUp_laundry_dryer).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_other_compactor).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('12) compactor: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_other_compactor).get_attribute('value'))
        categoriesInfo['compactor'] = self.driver.find_element(*SigninPageLocators.categories_signUp_other_compactor).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_refrigeration_icemaker).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('13) icemaker: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_refrigeration_icemaker).get_attribute('value'))
        categoriesInfo['icemaker'] = self.driver.find_element(*SigninPageLocators.categories_signUp_refrigeration_icemaker).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.categories_signUp_refrigeration_freezer).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('14) freezer: %s'%self.driver.find_element(*SigninPageLocators.categories_signUp_refrigeration_freezer).get_attribute('value'))
        categoriesInfo['freezer'] = self.driver.find_element(*SigninPageLocators.categories_signUp_refrigeration_freezer).get_attribute('value')
        print (categoriesInfo)

        self.click_categories_signup_button()

    def click_categories_signup_button(self):
        time.sleep(1)
        categories = self.driver.find_element(
            *SigninPageLocators.categories_signUp_next_btn)
        categories.click()
