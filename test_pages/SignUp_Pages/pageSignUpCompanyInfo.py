import sys
sys.path.append('../test_locators')

import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from Basepage import BasePage, fake
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpCompanyInfo(BasePage):

    def street_add_error(self):
        street_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_street_add_error)
        print("signup company-info street blank",  street_er.is_displayed())
        return street_er.is_displayed()

    def city_error(self):
        city_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_city_error)
        print("signup company-info city blank",  city_er.is_displayed())
        return city_er.is_displayed()

    def state_error(self):
        state_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_state_error)
        print("signup company-info state blank",  state_er.is_displayed())
        return state_er.is_displayed()

    def post_error(self):
        post_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_post_error)
        print("signup company-info  postal-code blank or invalid",
              post_er.is_displayed())
        return post_er.is_displayed()

    def website_error(self):
        web_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_website_error)
        print("signup company-info website-name blank or invalid",
              web_er.is_displayed())
        return web_er.is_displayed()

    def email_error(self):
        email_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_email_error)
        print("signup company-info email blank or invalid",
              email_er.is_displayed())
        return email_er.is_displayed()

    def phn_error(self):
        phn_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_phn_error)
        print("signup company-info phone-number blank or invalid",
              phn_er.is_displayed())
        return phn_er.is_displayed()

    def othr_error(self):
        othr_phn_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_othr_error)
        print("signup company-info other-phone-number invalid",
              othr_phn_er.is_displayed())
        return othr_phn_er.is_displayed()

    def fill_fields(self):
        self.wait_for_element(SigninPageLocators.compyinfo_signUp_reseller_id)

        reseller_id = self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_reseller_id)
        reseller_id.send_keys(fake.random_int(min=0, max=9999))

        self.click_companyInfo_signup_button()
        time.sleep(1)
        try:
            assert self.street_add_error()
        except:
            print("No result found for street-address")
        try:
            assert self.city_error()
        except:
            print("No result found for city")
        try:
            assert self.state_error()
        except:
            print("No result found for state")

        try:
            assert self.post_error()
        except:
            print("No result found for post-code")
        try:
            assert self.website_error()
        except:
            print("No result found for website")
        try:
            assert self.email_error()
        except:
            print("No result found for email")
        try:
            assert self.phn_error()
        except:
            print("No result found for phone-number")

        street_add = self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_street_add)
        street_add.send_keys(fake.building_number() + " " + fake.street_name())

        city = self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_city)
        city.send_keys(fake.city())

        self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_state).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        post_code = self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_post_code)
        post_code.send_keys('test post')

        domain = self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_website)
        domain.send_keys('test website')

        email = self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_email)
        email.send_keys('testemail.com')

        phn_num = self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_phn)
        phn_num.send_keys("11111")

        otr_phn = self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_otherphn)
        otr_phn.send_keys("2222")

        self.click_companyInfo_signup_button()
        time.sleep(1)

        try:
            assert self.post_error()
        except:
            print("No result found for post-code")
        try:
            assert self.website_error()
        except:
            print("No result found for website")
        try:
            assert self.email_error()
        except:
            print("No result found for email")
        try:
            assert self.phn_error()
        except:
            print("No result found for phone-number")
        try:
            assert self.othr_error()
        except:
            print("No result found for other-number")

        post_code.clear()
        post_code.send_keys(fake.postcode())

        domain.clear()
        domain.send_keys(fake.domain_name())

        email.clear()
        email.send_keys(fake.company_email())

        phn_num.clear()
        phn_num.send_keys("12345678901")

        otr_phn.clear()
        otr_phn.send_keys("12345678902")

        self.click_companyInfo_signup_button()

    def click_companyInfo_signup_button(self):
        element_companyInfo_signup = self.driver.find_element(
            *SigninPageLocators.companyinfo_next_btn)
        element_companyInfo_signup.click()
