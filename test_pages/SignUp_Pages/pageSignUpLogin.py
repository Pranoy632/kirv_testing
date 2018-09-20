import sys
sys.path.append('../test_locators')

import datetime

from Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpLogin(BasePage):
    def fill_email_pwd(self):
        time_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        input_email = self.driver.find_element(
            *SigninPageLocators.email_login_signup)
        input_email.send_keys("pranoy.s" + "+" + time_now + "@amazatic.com")

        input_pwd = self.driver.find_element(
            *SigninPageLocators.pwd_login_signup)
        input_pwd.send_keys("amazatic")

    def click_login_signup_button(self):
        element_login_signup = self.driver.find_element(
            *SigninPageLocators.signup)
        element_login_signup.click()
