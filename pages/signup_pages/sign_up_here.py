#import sys
# sys.path.append('../locators')


from pages.basepage import BasePage

from locators.sign_up_locators.locatorSignup import SignupPageLocators


class SignUpHere(BasePage):

    def click_signup_link(self):
        element = self.driver.find_element(*SignupPageLocators.signupLink)
        element.click()
