import sys
sys.path.append('../locators')

from pages.basepage import BasePage
from locators.sign_in_page_locators.signin_buyer_supplier_locator import SignInLocators
from locators import SupplierPageLocators


class SignIn(BasePage):

    def set_email(self):
        email = self.driver.find_element(*SignInLocators.email_login)
        email.send_keys("w@kirv.co")

    def set_password(self):
        password = self.driver.find_element(*SignInLocators.pwd_login)
        password.send_keys("qwerty123")

    def click_button(self):
        button = self.driver.find_element(*SupplierPageLocators.signin)
        button.click()

    def sign_in_credentials(self):
        self.set_email()
        self.set_password()
        self.click_button()
