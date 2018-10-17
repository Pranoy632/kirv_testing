import sys
sys.path.append('../test_locators')
import time

from Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpBrand(BasePage):

    def title_check(self):
        self.wait_for_element(
            SigninPageLocators.brand_title)

        title = self.driver.find_element(
            *SigninPageLocators.brand_title)

        try:
            assert title.is_displayed() == True
            print("Success: brand title found.")
        except:
            print("No result found for brand title.")

    def select_checkbox(self):
        self.wait_for_element(SigninPageLocators.brand_signUp)
        time.sleep(1)
        element_brand_signup = self.driver.find_element(
            *SigninPageLocators.brand_signUp)
        element_brand_signup.click()

    def click_brand_signup_button(self):
        element_brand_signup_btn = self.driver.find_element(
            *SigninPageLocators.brand_start_app_btn)
        element_brand_signup_btn.click()
