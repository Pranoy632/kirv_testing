import sys
sys.path.append('../test_locators')

from Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators
from Supplier_Locators.locatorSupplier import SupplierPageLocators

class SignIn(BasePage):

    def set_email(self):
        email = self.driver.find_element(*SigninPageLocators.email_login_signup)
        email.send_keys("w@kirv.co")

    def set_password(self):
        password = self.driver.find_element(*SigninPageLocators.pwd_login_signup)
        password.send_keys("qwerty123")

    def click_button(self):
        button = self.driver.find_element(*SupplierPageLocators.signin)
        button.click()

    def sign_in_credentials(self):
        self.set_email()
        self.set_password()
        self.click_button()
