import sys
sys.path.append('../test_locators')

import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from Basepage import BasePage, fake
from SignUp_Locators.locatorSignup import SigninPageLocators

companyInfo = {}


class SignUpCompanyInfo(BasePage):

    def step_check(self):
        time.sleep(2)
        step_1 = None
        self.wait_for_element(SigninPageLocators.steps)
        step = self.driver.find_element(
            *SigninPageLocators.steps)
        step_li = step.find_elements_by_tag_name("li")

        for item in step_li:
            is_active = "active" in item.get_attribute("class")
            if is_active:
                step_1 = item.text
        if step_1 == str(1):
            print("Success: Step %s is active." % (step_1))
        else:
            print("No result found for step %s active." % (step_1))

    def title_check(self):
        self.wait_for_element(
            SigninPageLocators.companyinfo_title)

        title = self.driver.find_element(
            *SigninPageLocators.companyinfo_title)

        try:
            assert title.is_displayed() == True
            print("Success: comapanyInfo title found.")
        except:
            print("No result found for companyInfo title.")

    def street_add_error(self):
        street_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_street_add_error)
        return street_er.is_displayed()

    def city_error(self):
        city_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_city_error)
        return city_er.is_displayed()

    def state_error(self):
        state_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_state_error)
        return state_er.is_displayed()

    def post_error(self):
        post_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_post_error)
        return post_er.is_displayed()

    def website_error(self):
        web_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_website_error)
        return web_er.is_displayed()

    def email_error(self):
        email_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_email_error)
        return email_er.is_displayed()

    def phn_error(self):
        phn_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_phn_error)
        return phn_er.is_displayed()

    def othr_error(self):
        othr_phn_er = self.driver.find_element(
            *SigninPageLocators.companyinfo_othr_error)
        return othr_phn_er.is_displayed()

    def fill_fields(self):
        self.wait_for_element(SigninPageLocators.compyinfo_signUp_reseller_id)

        reseller_id = self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_reseller_id)
        reseller_id.send_keys(fake.random_int(min=0, max=9999))
        print ('1) reseller_id: %s' % reseller_id.get_attribute('value'))
        companyInfo['reseller_id'] = reseller_id.get_attribute('value')

        self.click_companyInfo_signup_button()
        time.sleep(1)
        try:
            assert self.street_add_error() == True
            print("Success: signup company-info street-address blank error found.")
        except:
            print("No result found for blank street-address")
        try:
            assert self.city_error() == True
            print("Success: signup company-info city blank error found.")
        except:
            print("No result found for blank  city")
        try:
            assert self.state_error() == True
            print("Success: signup company-info state blank error found.")
        except:
            print("No result found for blank  state")

        try:
            assert self.post_error() == True
            print("Success: signup company-info post-code blank error found.")
        except:
            print("No result found for blank  post-code")
        try:
            assert self.website_error() == True
            print("Success: signup company-info website blank error found.")
        except:
            print("No result found for blank  website")
        try:
            assert self.email_error() == True
            print("Success: signup company-info email blank error found.")
        except:
            print("No result found for blank  email")
        try:
            assert self.phn_error() == True
            print("Success: signup company-info phone-number blank error found.")
        except:
            print("No result found for blank  phone-number")

        street_add = self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_street_add)
        street_add.send_keys(fake.building_number() + " " + fake.street_name())
        print ('2) Street address: %s' % street_add.get_attribute('value'))
        companyInfo['street_address'] = street_add.get_attribute('value')

        city = self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_city)
        city.send_keys(fake.city())
        print ('3) City: %s' % city.get_attribute('value'))
        companyInfo['city'] = city.get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_state).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('4) State: %s' % self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_state).get_attribute('value'))
        companyInfo['state'] = self.driver.find_element(
            *SigninPageLocators.compyinfo_signUp_state).get_attribute('value')

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
            assert self.post_error() == True
            print("Success: signup company-info post-code invalid error found.")
        except:
            print("No result found for post-code")
        try:
            assert self.website_error() == True
            print("Success: signup company-info website invalid error found.")
        except:
            print("No result found for website")
        try:
            assert self.email_error() == True
            print("Success: signup company-info email invalid error found.")
        except:
            print("No result found for email")
        try:
            assert self.phn_error() == True
            print("Success: signup company-info phone-number invalid error found.")
        except:
            print("No result found for phone-number")
        try:
            assert self.othr_error() == True
            print("Success: signup company-info other-number invalid error found.")
        except:
            print("No result found for other-number")

        post_code.clear()
        post_code.send_keys(fake.postcode())
        print ('5) PostCode: %s' % post_code.get_attribute('value'))
        companyInfo['post_code'] = post_code.get_attribute('value')

        domain.clear()
        domain.send_keys(fake.domain_name())
        print ('6) Domain: %s' % domain.get_attribute('value'))
        companyInfo['domain'] = domain.get_attribute('value')

        email.clear()
        email.send_keys(fake.company_email())
        print ('7) Email: %s' % email.get_attribute('value'))
        companyInfo['email'] = email.get_attribute('value')

        phn_num.clear()
        phn_num.send_keys("12345678901")
        print ('8) Phone No: %s' % phn_num.get_attribute('value'))
        companyInfo['phone_no'] = phn_num.get_attribute('value')

        otr_phn.clear()
        otr_phn.send_keys("12345678902")
        print ('9) Other Phone no: %s' % otr_phn.get_attribute('value'))
        companyInfo['other_phone_no'] = otr_phn.get_attribute('value')
        print (companyInfo)

        self.click_companyInfo_signup_button()

    def click_companyInfo_signup_button(self):
        element_companyInfo_signup = self.driver.find_element(
            *SigninPageLocators.companyinfo_next_btn)
        element_companyInfo_signup.click()
