import sys
sys.path.append('../locators')
import time

from pages.basepage import BasePage
from locators import SigninPageLocators


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
        print ('-------------------- In brand select checkbox----------------------')
        self.wait_for_element(SigninPageLocators.brand_signUp)
        time.sleep(1)
        element_brand_signup = self.driver.find_element(
            *SigninPageLocators.brand_signUp)
        element_brand_signup.click()

    def click_brand_signup_button(self):
        print ('--------------- brand signup button --------------------')
        element_brand_signup_btn = self.driver.find_element(
            *SigninPageLocators.brand_start_app_btn)
        element_brand_signup_btn.click()
