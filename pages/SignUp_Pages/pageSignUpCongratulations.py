#import sys
#sys.path.append('../locators')
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from pages.basepage import BasePage
from locators.sign_up_locators.locatorSignup import SigninPageLocators


class SignUpCongratulations(BasePage):

    def check_congrats_img(self):
        congrats_img = self.driver.find_element(
            *SigninPageLocators.congrats_kirv_image)
        return congrats_img.is_displayed()

    def check_congrats_title(self):
        congrat_title = self.driver.find_element(
            *SigninPageLocators.congrats_title)
        return congrat_title.is_displayed()

    def check_img_title(self):
        time.sleep(1)
        try:
            assert self.check_congrats_img() == True
            print("Success: Kirv image found.")
        except:
            print("No result for kirv image.")

        try:
            assert self.check_congrats_title() == True
            print("Success: congratulation title found.")
        except:
            print("No result for congratulation title.")

    def click_modal_close_btn(self):
        self.wait_for_element(SigninPageLocators.congratulation_modal_close)
        time.sleep(1)
        congrats = self.driver.find_element(
            *SigninPageLocators.congratulation_modal_close)
        congrats.click()
