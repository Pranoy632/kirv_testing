import sys
sys.path.append('../locators')

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from pages.basepage import BasePage
from locators import SigninPageLocators

volumeInfo = {}


class SignUpVolumes(BasePage):

    def step_check(self):
        time.sleep(2)
        step_5 = None
        self.wait_for_element(SigninPageLocators.steps)
        step = self.driver.find_element(
            *SigninPageLocators.steps)
        step_li = step.find_elements_by_tag_name("li")

        for item in step_li:
            is_active = "active" in item.get_attribute("class")
            if is_active:
                step_5 = item.text
        if step_5 == str(5):
            print("Success: Step %s is active." % (step_5))
        else:
            print("No result found for step %s active." % (step_5))

    def title_check(self):
        self.wait_for_element(
            SigninPageLocators.volumes_title)

        title = self.driver.find_element(
            *SigninPageLocators.volumes_title)

        try:
            assert title.is_displayed() == True
            print("Success: volumes title found.")
        except:
            print("No result found for volumes title.")

    def full_truck_q1_err(self):
        full_q1_er = self.driver.find_element(
            *SigninPageLocators.volumes_num_full_trucks_q1_err)
        return full_q1_er.is_displayed()

    def half_truck_q2_err(self):
        half_q2_er = self.driver.find_element(
            *SigninPageLocators.volumes_num_half_trucks_q2_err)
        return half_q2_er.is_displayed()

    def full_truck_q2_err(self):
        full_q2_er = self.driver.find_element(
            *SigninPageLocators.volumes_num_full_trucks_q2_err)
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
        print ('1) q1_quarterTruck: %s' % self.driver.find_element(
            *SigninPageLocators.volumes_signUp_quarter_truck_q1).get_attribute('value'))
        volumeInfo['q1_quarterTruck'] = self.driver.find_element(
            *SigninPageLocators.volumes_signUp_quarter_truck_q1).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.volumes_signUp_half_truck_q1).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('2) q1_halfTruck: %s' % self.driver.find_element(
            *SigninPageLocators.volumes_signUp_half_truck_q1).get_attribute('value'))
        volumeInfo['q1_halfTruck'] = self.driver.find_element(
            *SigninPageLocators.volumes_signUp_half_truck_q1).get_attribute('value')

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
        print ('3) q2_quarterTruck: %s' % self.driver.find_element(
            *SigninPageLocators.volumes_signUp_quarter_truck_q2).get_attribute('value'))
        volumeInfo['q2_quarterTruck'] = self.driver.find_element(
            *SigninPageLocators.volumes_signUp_quarter_truck_q2).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.volumes_signUp_acknowledge_check).click()

        self.click_volumes_signup_button()
        time.sleep(1)

        try:
            assert self.full_truck_q1_err() == True
            print("Success: signup volumes full truck q1 blank error found.")
        except:
            print("No result found for q1 full-truck")

        try:
            assert self.half_truck_q2_err() == True
            print("Success: signup volumes half truck q2 blank error found.")
        except:
            print("No result found for q2 half-truck")

        try:
            assert self.full_truck_q2_err() == True
            print("Success: signup volumes full truck q2 blank error found.")
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
        print ('4) q1_fullTruck: %s' % self.driver.find_element(
            *SigninPageLocators.volumes_signUp_full_truck_q1).get_attribute('value'))
        volumeInfo['q1_fullTruck'] = self.driver.find_element(
            *SigninPageLocators.volumes_signUp_full_truck_q1).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.volumes_signUp_half_truck_q2).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('5) q2_halfTruck: %s' % self.driver.find_element(
            *SigninPageLocators.volumes_signUp_half_truck_q2).get_attribute('value'))
        volumeInfo['q2_halfTruck'] = self.driver.find_element(
            *SigninPageLocators.volumes_signUp_half_truck_q2).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.volumes_signUp_full_truck_q2).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('6) q2_fullTruck: %s' % self.driver.find_element(
            *SigninPageLocators.volumes_signUp_full_truck_q2).get_attribute('value'))
        volumeInfo['q2_fullTruck'] = self.driver.find_element(
            *SigninPageLocators.volumes_signUp_full_truck_q2).get_attribute('value')
        print (volumeInfo)

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
