import sys
sys.path.append('../test_locators')

import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from Basepage import BasePage, fake
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpLocation(BasePage):

    def loc1_street_error(self):
        street_er = self.driver.find_element(
            *SigninPageLocators.street_error1)
        return street_er.is_displayed()

    def loc1_city_error(self):
        city_er = self.driver.find_element(
            *SigninPageLocators.city_error1)
        return city_er.is_displayed()

    def loc1_state_error(self):
        state_er = self.driver.find_element(
            *SigninPageLocators.state_error1)
        return state_er.is_displayed()

    def loc1_post_error(self):
        post_er = self.driver.find_element(
            *SigninPageLocators.post_error1)
        return post_er.is_displayed()

    def loc1_other_phone_error(self):
        othr_er = self.driver.find_element(
            *SigninPageLocators.otr_phn_error1)
        return othr_er.is_displayed()

    def loc2_post_error(self):
        post_error = self.driver.find_element(
            *SigninPageLocators.loc2_post_code_err)
        return post_error.is_displayed()

    def loc2_email_error(self):
        email_error = self.driver.find_element(
            *SigninPageLocators.loc2_email_err)
        return email_error.is_displayed()

    def loc2_phn_error(self):
        phn_error = self.driver.find_element(
            *SigninPageLocators.loc2_phn_err)
        return phn_error.is_displayed()

    def fill_fields(self):
        self.wait_for_element(SigninPageLocators.location_signUp_name1)

        loc_name1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_name1)
        loc_name1.send_keys(fake.street_name())

        loc_email1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_email1)
        loc_email1.send_keys(fake.email())

        loc_ph1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_phn1)
        loc_ph1.send_keys("12345678901")

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

        self.driver.find_element(
            *SigninPageLocators.location_signUp_check2).click()

        self.click_location_signup_button()
        time.sleep(1)

        try:
            assert self.loc1_street_error() == True
            print("Success: sign-up location-1 blank street-address error found.")
        except:
            print("No result found for location-1  blank street-address")

        try:
            assert self.loc1_city_error() == True
            print("Success: sign-up location-1 blank city error found.")
        except:
            print("No result found for location-1  blank city")

        try:
            assert self.loc1_state_error() == True
            print("Success: sign-up location-1 blank state error found.")
        except:
            print("No result found for location-1  blank  state")

        try:
            assert self.loc1_post_error() == True
            print("Success: sign-up location-1 blank post-code error found.")
        except:
            print("No result found for location-1  blank  post-code")

        try:
            assert self.loc2_post_error() == True
            print("Success: sign-up location-2 blank post-code error found.")
        except:
            print("No result found for location-2 blank post-code")

        try:
            assert self.loc2_email_error() == True
            print("Success: sign-up location-2 blank email error found.")
        except:
            print("No result found for location-2 blank email")

        try:
            assert self.loc2_phn_error() == True
            print("Success: sign-up location-2 blank phone-number error found.")
        except:
            print("No result found for location-2 blank phone-number")

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(document.body.scrollHeight, 0);")
        time.sleep(1)

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
        loc_post_code1.send_keys("test post")

        loc_other_phn1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_otherphn1)
        loc_other_phn1.send_keys("22222")

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        loc_post_code2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_post_code2)
        loc_post_code2.send_keys("test post")

        loc_email2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_email2)
        loc_email2.send_keys("test.email.com")

        loc_phn2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_phn2)
        loc_phn2.send_keys("1111")

        self.click_location_signup_button()
        time.sleep(1)

        try:
            assert self.loc1_post_error() == True
            print("Success: sign-up location-1 invalid post-code error found.")
        except:
            print("No result found for invalid location-1 post-code")

        try:
            assert self.loc1_other_phone_error() == True
            print("Success: sign-up location-1 invalid other-number error found.")
        except:
            print("No result found for invalid location-1 other-phone number")

        try:
            assert self.loc2_post_error() == True
            print("Success: sign-up location-2 invalid post-code error found.")
        except:
            print("No result found for invalid location-2 post-code")

        try:
            assert self.loc2_email_error() == True
            print("Success: sign-up location-2 invalid email error found.")
        except:
            print("No result found for invalid location-2 email")

        try:
            assert self.loc2_phn_error() == True
            print("Success: sign-up location-2 invalid phone-number error found.")
        except:
            print("No result found for invalid location-2 phone-number")

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(document.body.scrollHeight, 0);")
        time.sleep(1)

        loc_post_code1.clear()
        loc_post_code1.send_keys(fake.postcode())

        loc_other_phn1.clear()
        loc_other_phn1.send_keys("12345678902")

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        loc_post_code2.clear()
        loc_post_code2.send_keys(fake.postcode())

        loc_email2.clear()
        loc_email2.send_keys(fake.email())

        loc_phn2.clear()
        loc_phn2.send_keys("12345678901")

        # Modal

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

        self.click_location_signup_button()

    def click_location_signup_button(self):
        time.sleep(1)
        loc = self.driver.find_element(
            *SigninPageLocators.loc_next_btn)
        loc.click()
