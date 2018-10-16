import sys
sys.path.append('../test_locators')
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpCongratulations(BasePage):

    def congrats_title_check(self):
        self.wait_for_element(SigninPageLocators.congrats_title)

        cong_title = self.driver.find_element(
            *SigninPageLocators.congrats_title)

        try:
            assert cong_title.is_displayed() == True
            print("Success: Congratulation title found.")
        except:
            print("No record found for Congratulation title.")

    def click_modal_close_btn(self):
        self.wait_for_element(SigninPageLocators.congratulation_modal_close)
        time.sleep(1)
        congrats = self.driver.find_element(
            *SigninPageLocators.congratulation_modal_close)
        congrats.click()
