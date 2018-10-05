import sys
sys.path.append('../test_locators')

import datetime
import time

from Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators

time_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


class SignUpLogin(BasePage):

    def login_email_error_displayed(self):
        emailElement = self.driver.find_element(
            *SigninPageLocators.email_login_signup_error)
        print("email blank",  emailElement.is_displayed())
        return emailElement.is_displayed()

    def login_pwd_error_displayed(self):
        pwdElement = self.driver.find_element(
            *SigninPageLocators.pwd_login_signup_error)
        print("password blank", pwdElement.is_displayed())
        return pwdElement.is_displayed()

    def login_with_blank_email(self):
        self.wait_for_element(
            SigninPageLocators.email_login_signup)

        self.driver.find_element(
            *SigninPageLocators.email_login_signup).send_keys("")
        self.driver.find_element(
            *SigninPageLocators.pwd_login_signup).send_keys("amazatic")

    def login_with_invalid_email(self):

        self.driver.find_element(
            *SigninPageLocators.email_login_signup).send_keys("amz.amazatic.com")

        self.driver.find_element(
            *SigninPageLocators.pwd_login_signup).send_keys("amazatic")

    def login_with_blank_pwd(self):

        self.driver.find_element(
            *SigninPageLocators.email_login_signup).send_keys("amz" + "+" + time_now + "@amazatic.com")

        self.driver.find_element(
            *SigninPageLocators.pwd_login_signup).send_keys("")

    def clear_data(self):

        self.wait_for_element_clickable(SigninPageLocators.email_login_signup)

        self.driver.find_element(
            *SigninPageLocators.email_login_signup).clear()

        self.driver.find_element(
            *SigninPageLocators.pwd_login_signup).clear()

    def fill_email_pwd(self):

        self.wait_for_element_clickable(SigninPageLocators.email_login_signup)

        input_email = self.driver.find_element(
            *SigninPageLocators.email_login_signup)
        input_email.send_keys("amztest18" + "+" + time_now + "@gmail.com")
        #input_email.send_keys("aaditi.d" + "+" + time_now + "@amazatic.com")
        #input_email.send_keys("priyanka.c" + "+" + time_now + "@amazatic.com")
        print("email", input_email.get_attribute('value'))

        input_pwd = self.driver.find_element(
            *SigninPageLocators.pwd_login_signup)
        input_pwd.send_keys("amazatic")
        print("password", input_pwd.get_attribute('value'))

    def click_login_signup_button(self):

        self.wait_for_element(
            SigninPageLocators.signup_login_btn)

        element_login_signup = self.driver.find_element(
            *SigninPageLocators.signup_login_btn)
        element_login_signup.click()
