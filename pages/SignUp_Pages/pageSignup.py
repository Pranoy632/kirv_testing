#import sys
#sys.path.append('../locators')


from pages.basepage import BasePage

from locators.sign_up_locators.locatorSignup import SigninPageLocators


class MainPage(BasePage):

    def click_signup_button(self):
        element = self.driver.find_element(*SigninPageLocators.signupLink)
        element.click()
