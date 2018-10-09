import sys
sys.path.append('../test_locators')

import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from Basepage import BasePage, fake
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpShipTo(BasePage):

    def ship2_street_error(self):
        street_er = self.driver.find_element(
            *SigninPageLocators.ship2_street_err)
        print("signup shipTo-2 street blank",  street_er.is_displayed())
        return street_er.is_displayed()

    def ship2_city_error(self):
        city_er = self.driver.find_element(
            *SigninPageLocators.ship2_city_err)
        print("signup shipTo-2 city blank",  city_er.is_displayed())
        return city_er.is_displayed()

    def ship2_post_error(self):
        post_error = self.driver.find_element(
            *SigninPageLocators.ship2_post_err)
        print("signup shipTo-2 postal-code blank or invalid",
              post_error.is_displayed())
        return post_error.is_displayed()

    def ship2_email_error(self):
        email_error = self.driver.find_element(
            *SigninPageLocators.ship2_email_err)
        print("signup shipTo-2  email blank or invalid",
              email_error.is_displayed())
        return email_error.is_displayed()

    def ship2_phn_error(self):
        phn_error = self.driver.find_element(
            *SigninPageLocators.ship2_phn_err)
        print("signup shipTo-2 phone-number blank or invalid",
              phn_error.is_displayed())
        return phn_error.is_displayed()

    def ship_other_phone_error(self):
        othr_er = self.driver.find_element(
            *SigninPageLocators.ship2_othr_phn_err)
        print("signup shipTo-2  other-phone-number invalid",
              othr_er.is_displayed())
        return othr_er.is_displayed()

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
            *SigninPageLocators.ship_signUp_add_ship2).click()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        ship_name2 = self.driver.find_element(
            *SigninPageLocators.ship2_name)
        ship_name2.send_keys(fake.street_name())

        self.driver.find_element(
            *SigninPageLocators.ship2_state).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.ship2_start).click()

        self.wait_for_element(SigninPageLocators.ship_start_time)

        self.driver.find_element(
            *SigninPageLocators.ship_start_time).click()

        self.driver.find_element(
            *SigninPageLocators.ship_ok_btn_start_end).click()

        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.ship2_end).click()

        self.wait_for_element(SigninPageLocators.ship_end_time)

        self.driver.find_element(
            *SigninPageLocators.ship_end_time).click()

        self.driver.find_element(
            *SigninPageLocators.ship_ok_btn_start_end).click()

        self.click_ship_signup_button()
        time.sleep(1)

        try:
            assert self.ship2_street_error()
        except:
            print("No result found for blank street-address")

        try:
            assert self.ship2_city_error()
        except:
            print("No result found for blank city")

        try:
            assert self.ship2_post_error()
        except:
            print("No result found for blank post-code")

        try:
            assert self.ship2_email_error()
        except:
            print("No result found for blank email")

        try:
            assert self.ship2_phn_error()
        except:
            print("No result found for blank phone")

        ship_street2 = self.driver.find_element(
            *SigninPageLocators.ship2_street_add)
        ship_street2.send_keys(fake.building_number() +
                               " " + fake.street_name())

        ship_city2 = self.driver.find_element(
            *SigninPageLocators.ship2_city)
        ship_city2.send_keys(fake.city())

        ship_post2 = self.driver.find_element(
            *SigninPageLocators.ship2_post)
        ship_post2.send_keys("test post")

        ship_email2 = self.driver.find_element(
            *SigninPageLocators.ship2_email)
        ship_email2.send_keys("testemail.com")

        ship_phn2 = self.driver.find_element(
            *SigninPageLocators.ship2_phn)
        ship_phn2.send_keys('1111')

        ship_othr_phn2 = self.driver.find_element(
            *SigninPageLocators.ship2_othr_phn)
        ship_othr_phn2.send_keys('2222')

        self.click_ship_signup_button()
        time.sleep(1)

        try:
            assert self.ship2_post_error()
        except:
            print("No result found for invalid ship-2 post-code")

        try:
            assert self.ship2_email_error()
        except:
            print("No result found for invalid ship-2 email")

        try:
            assert self.ship2_phn_error()
        except:
            print("No result found for invalid ship-2 phone")

        try:
            assert self.ship_other_phone_error()
        except:
            print("No result found for invalid ship-2 other-phone")

        ship_post2.clear()
        ship_post2.send_keys(fake.postcode())

        ship_email2.clear()
        ship_email2.send_keys(fake.email())

        ship_phn2.clear()
        ship_phn2.send_keys('12345678901')

        ship_othr_phn2.clear()
        ship_othr_phn2.send_keys('12345678902')

        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.ship_signUp_add_ship3).click()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.ship_signUp_delete3).click()

        self.wait_for_element(SigninPageLocators.ship_signUp_del_modal)
        self.driver.find_element(
            *SigninPageLocators.ship_signUp_del_modal).click()

        self.click_ship_signup_button()

    def click_ship_signup_button(self):
        time.sleep(1)
        ship = self.driver.find_element(
            *SigninPageLocators.ship_next_btn)
        ship.click()
