import sys
sys.path.append('../test_locators')


from Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpBrand(BasePage):

    def select_checkbox(self):
        self.wait_for_element(SigninPageLocators.brand_signUp)
        element_brand_signup = self.driver.find_element(
            *SigninPageLocators.brand_signUp)
        element_brand_signup.click()

    def click_brand_signup_button(self):
        element_brand_signup_btn = self.driver.find_element(
            *SigninPageLocators.signup)
        element_brand_signup_btn.click()
