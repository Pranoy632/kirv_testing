import datetime

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from pages.basepage import *
from locators.sign_up_locators.locatorSignup import SignupPageLocators, CreateAccountLocators

time_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
create_account = {}
#token_data = {}


class CreateAccount(BasePage):

    def check_already_account_link(self):
        return self.driver.find_element(*CreateAccountLocators.already_account_link).text

    def check_kirv_logo(self):
        return self.driver.find_element(*SignupPageLocators.kirv_logo).is_displayed()

    def check_create_acc_title(self):
        return self.driver.find_element(*CreateAccountLocators.create_account_title).text

    def credential_set_para(self):
        return self.driver.find_element(*CreateAccountLocators.set_credentials_para).text

    def email_error(self):
        return self.driver.find_element(*CreateAccountLocators.email_err).text

    def email_err_user_exist(self):
        return self.driver.find_element(*CreateAccountLocators.user_exit_email_err).text

    def password_error(self):
        return self.driver.find_element(*CreateAccountLocators.password_err).text

    def confirm_button(self):
        try:
            self.driver.find_element(
                *CreateAccountLocators.confirm_btn).click()
        except WebDriverException:
            BasePage(self.driver).close_chat_popup_while_button_click(self.driver.find_element(
                *CreateAccountLocators.confirm_btn))

    def clear_put_value(self, locator):
        """
        clears and puts input in input box
        """
        time.sleep(2)
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

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

        self.confirm_button()
        time.sleep(4)

        try:
            assert self.email_error() == "This field is required."
        except:
            print("No result found for email error. ")

        try:
            assert self.password_error() == "This field is required."
        except:
            print("No result found for password error. ")

        email_field = self.driver.find_element(
            *CreateAccountLocators.email_input)

        password_field = self.driver.find_element(
            *CreateAccountLocators.password_input)

        email_field.send_keys('amz.test')
        password_field.send_keys('amz')

        self.confirm_button()
        time.sleep(2)

        try:
            assert self.email_error() == "Enter a valid email address."
        except:
            print("No result found for enter a valid email. ")

        self.clear_put_value(CreateAccountLocators.email_input)
        email_field.send_keys("amztest18" + "+" + time_now + "@gmail.com")

        self.confirm_button()
        time.sleep(2)

        try:
            assert self.password_error(
            ) == "This password is too short. It must contain at least 8 characters."
        except:
            print("No result found for 8 character password error. ")

        self.clear_put_value(CreateAccountLocators.password_input)
        password_field.send_keys('qwerty123')

        self.confirm_button()
        time.sleep(2)

        try:
            assert self.password_error(
            ) == "This password is too common."
        except:
            print("No result found for password is too common error. ")

        self.clear_put_value(CreateAccountLocators.email_input)

        self.clear_put_value(CreateAccountLocators.password_input)
        password_field.send_keys('amazatic')

        self.confirm_button()
        time.sleep(2)

        try:
            assert self.email_error() == "This field may not be blank."
        except:
            print("No result found for email field blank error. ")

        email_field.send_keys("amztest18@gmail.com")

        self.confirm_button()
        time.sleep(2)

        try:
            assert self.email_err_user_exist(
            ) == "An account already exists for this email address. Sign in here or reset your password."
        except:
            print("No result found for email user exists error. ")

        self.clear_put_value(CreateAccountLocators.email_input)

        email_field.send_keys("amztest18" + "+" + time_now + "@gmail.com")

        self.clear_put_value(CreateAccountLocators.password_input)

        self.confirm_button()
        time.sleep(2)

        try:
            assert self.password_error() == "This field may not be blank."
        except:
            print("No result found for password field blank error. ")

        self.clear_put_value(CreateAccountLocators.email_input)

        email_field.send_keys("amztest18" + "+" + time_now + "@gmail.com")
        create_account['email'] = email_field.get_attribute('value')
        print("Email:", create_account['email'])

        password_field.send_keys('amazatic')
        create_account['password'] = password_field.get_attribute('value')
        print("Password:", create_account['password'])

        self.confirm_button()

    #     time.sleep(2)
    #     self.get_token_from_localstorage()

    # def get_token_from_localstorage(self):

    #     tkn = self.driver.execute_script(
    #         'return JSON.parse(localStorage.getItem("token"));')['value']
    #     token_data['token'] = tkn
