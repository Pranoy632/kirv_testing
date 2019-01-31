import datetime

from selenium.webdriver.common.keys import Keys
from pages.basepage import *
from locators.sign_up_locators.locatorSignup import SignupPageLocators, CreateAccountLocators


time_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


class CreateAccount(BasePage):

    def check_already_account_link(self):
        return self.driver.find_element(*CreateAccountLocators.already_account_link).text

    def check_kirv_logo(self):
        return self.driver.find_element(*SignupPageLocators.kirv_logo).is_displayed()

    def check_create_acc_title(self):
        return self.driver.find_element(*CreateAccountLocators.create_account_title).text

    def credential_set_para(self):
        return self.driver.find_element(*CreateAccountLocators.set_credentials_para).text

    def confirm_button(self):
        self.driver.find_element(
            *CreateAccountLocators.confirm_btn).click()

    def create_account_page_elements(self):
        try:
            assert self.check_kirv_logo() == True
        except:
            print("No result found for kirv logo in create account page.")

        try:
            assert self.check_create_acc_title() == "Create your account"
        except:
            print("No result found for create account title.")

        try:
            assert self.credential_set_para() == "Set the credentials for your Kirv account."
        except:
            print("No result found for create account set credential paragraph.")

        try:
            assert self.check_already_account_link() == "Already have an account?"
        except:
            print("No result found for create account already have account link.")

        email_feild = self.driver.find_element(
            *CreateAccountLocators.email_input)

        password_feild = self.driver.find_element(
            *CreateAccountLocators.password_input)

        email_feild.send_keys("amztest18" + "+" + time_now + "@gmail.com")
        print("Email:", email_feild.get_attribute('value'))

        password_feild.send_keys('amazatic')
        print("Password:", password_feild.get_attribute('value'))

        self.confirm_button()
