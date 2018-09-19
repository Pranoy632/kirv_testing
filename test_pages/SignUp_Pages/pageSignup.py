import sys
sys.path.append('../test_locators')

from .Basepage import BasePage

from SignUp_Locators.locatorSignup import SigninPageLocators


class MainPage(BasePage):

    def click_signup_button(self):
        element = self.driver.find_element(*SigninPageLocators.signup)
        element.click()
