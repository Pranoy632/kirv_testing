from pages.basepage import *
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import SignupPageLocators, ContactInfoLocators, CompanyInfoLocators


class CompanyInfo(BasePage):

    def check_kirv_logo(self):
        return self.driver.find_element(*SignupPageLocators.kirv_logo).is_displayed()

    def check_quit_sign_up_title(self):
        return self.driver.find_element(*ContactInfoLocators.quit_sign_up).text

    def company_info_page_element(self):
        try:
            assert self.check_kirv_logo() == True
            print("Success: kirv logo found on company Info page.")
        except:
            print("No result found for kirv logo in company Info page.")

        try:
            assert self.check_quit_sign_up_title() == 'Quit sign up'
            print("Success: contact info quit sign-up title found.")
        except:
            print("No result found for contact info quit sign-up title.")
