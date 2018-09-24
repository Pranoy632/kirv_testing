import sys
sys.path.append('../test_locators')

import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from Basepage import BasePage, fake
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpCompanyInfo(BasePage):

    def fill_fields(self):
        self.wait_for_element(SigninPageLocators.compyinfo_signUp_reseller_id)

        self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_reseller_id).send_keys(fake.random_int(min=0, max=9999))
        self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_street_add).send_keys(fake.building_number() + " " + fake.street_name())
        self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_city).send_keys(fake.city())
        self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_state).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_post_code).send_keys(fake.postcode())
        self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_website).send_keys(fake.domain_name())
        self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_email).send_keys(fake.company_email())
        self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_phn).send_keys("12345678901")
        self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_otherphn).send_keys("12345678902")

    def click_companyInfo_signup_button(self):
        element_companyInfo_signup = self.driver.find_element(
            *SigninPageLocators.signup)
        element_companyInfo_signup.click()
