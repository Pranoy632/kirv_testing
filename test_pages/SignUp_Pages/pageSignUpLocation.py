import sys
sys.path.append('../test_locators')

import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from Basepage import BasePage, fake
from SignUp_Locators.locatorSignup import SigninPageLocators

locationInfo = {}
shippingInfo = {}


class SignUpLocation(BasePage):

    def step_check(self):
        time.sleep(2)
        step_2 = None
        self.wait_for_element(SigninPageLocators.steps)
        step = self.driver.find_element(
            *SigninPageLocators.steps)
        step_li = step.find_elements_by_tag_name("li")

        for item in step_li:
            is_active = "active" in item.get_attribute("class")
            if is_active:
                step_2 = item.text
        if step_2 == str(2):
            print("Success: Step %s is active." % (step_2))
        else:
            print("No result found for step %s active." % (step_2))

    def title_check(self):
        self.wait_for_element(
            SigninPageLocators.location_title)

        title = self.driver.find_element(
            *SigninPageLocators.location_title)

        try:
            assert title.is_displayed() == True
            print("Success: location title found.")
        except:
            print("No result found for location title.")

    def loc1_street_error(self):
        street_er = self.driver.find_element(
            *SigninPageLocators.street_error1)
        return street_er.is_displayed()

    def loc1_city_error(self):
        city_er = self.driver.find_element(
            *SigninPageLocators.city_error1)
        return city_er.is_displayed()

    def loc1_state_error(self):
        state_er = self.driver.find_element(
            *SigninPageLocators.state_error1)
        return state_er.is_displayed()

    def loc1_post_error(self):
        post_er = self.driver.find_element(
            *SigninPageLocators.post_error1)
        return post_er.is_displayed()

    def loc1_other_phone_error(self):
        othr_er = self.driver.find_element(
            *SigninPageLocators.otr_phn_error1)
        return othr_er.is_displayed()

    def loc2_post_error(self):
        post_error = self.driver.find_element(
            *SigninPageLocators.loc2_post_code_err)
        return post_error.is_displayed()

    def loc2_email_error(self):
        email_error = self.driver.find_element(
            *SigninPageLocators.loc2_email_err)
        return email_error.is_displayed()

    def loc2_phn_error(self):
        phn_error = self.driver.find_element(
            *SigninPageLocators.loc2_phn_err)
        return phn_error.is_displayed()

    def fill_fields(self):
        self.wait_for_element(SigninPageLocators.location_signUp_name1)

        loc_name1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_name1)
        loc_name1.send_keys(fake.street_name())
        print ('1) name1: %s' % loc_name1.get_attribute('value'))
        locationInfo['name1'] = loc_name1.get_attribute('value')

        loc_email1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_email1)
        loc_email1.send_keys(fake.email())
        print ('2) email1: %s' % loc_email1.get_attribute('value'))
        locationInfo['email1'] = loc_email1.get_attribute('value')

        loc_ph1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_phn1)
        loc_ph1.send_keys("12345678904")
        print ('3) phone no1: %s' % loc_ph1.get_attribute('value'))
        locationInfo['phone_no1'] = loc_ph1.get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.location_signUp_add_loc).click()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        loc_name2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_name2)
        loc_name2.send_keys(fake.street_name())
        print ('4) name2: %s' % loc_name2.get_attribute('value'))
        locationInfo['name2'] = loc_name2.get_attribute('value')
        shippingInfo['name1'] = loc_name2.get_attribute('value')

        loc_street2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_street_add2)
        loc_street2.send_keys(fake.building_number() +
                              " " + fake.street_name())
        print ('5) street2: %s' % loc_street2.get_attribute('value'))
        locationInfo['street2'] = loc_street2.get_attribute('value')
        shippingInfo['street1'] = loc_street2.get_attribute('value')

        loc_city2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_city2)
        loc_city2.send_keys(fake.city())
        print ('6) city2: %s' % loc_city2.get_attribute('value'))
        locationInfo['city2'] = loc_city2.get_attribute('value')
        shippingInfo['city1'] = loc_city2.get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.location_signUp_state2).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('7) state1: %s' % self.driver.find_element(
            *SigninPageLocators.location_signUp_state2).get_attribute('value'))
        locationInfo['state1'] = self.driver.find_element(
            *SigninPageLocators.location_signUp_state2).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.location_signUp_check2).click()

        self.click_location_signup_button()
        time.sleep(1)

        try:
            assert self.loc1_street_error() == True
            print("Success: sign-up location-1 blank street-address error found.")
        except:
            print("No result found for location-1  blank street-address")

        try:
            assert self.loc1_city_error() == True
            print("Success: sign-up location-1 blank city error found.")
        except:
            print("No result found for location-1  blank city")

        try:
            assert self.loc1_state_error() == True
            print("Success: sign-up location-1 blank state error found.")
        except:
            print("No result found for location-1  blank  state")

        try:
            assert self.loc1_post_error() == True
            print("Success: sign-up location-1 blank post-code error found.")
        except:
            print("No result found for location-1  blank  post-code")

        try:
            assert self.loc2_post_error() == True
            print("Success: sign-up location-2 blank post-code error found.")
        except:
            print("No result found for location-2 blank post-code")

        try:
            assert self.loc2_email_error() == True
            print("Success: sign-up location-2 blank email error found.")
        except:
            print("No result found for location-2 blank email")

        try:
            assert self.loc2_phn_error() == True
            print("Success: sign-up location-2 blank phone-number error found.")
        except:
            print("No result found for location-2 blank phone-number")

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(document.body.scrollHeight, 0);")
        time.sleep(1)

        loc_street1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_street_add1)
        loc_street1.send_keys(fake.building_number() +
                              " " + fake.street_name())
        print ('8) street1: %s' % loc_street1.get_attribute('value'))
        locationInfo['street1'] = loc_street1.get_attribute('value')

        loc_city1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_city1)
        loc_city1.send_keys(fake.city())
        print ('9) city1: %s' % loc_city1.get_attribute('value'))
        locationInfo['city1'] = loc_city1.get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.location_signUp_state1).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('10) state2:%s ' % self.driver.find_element(
            *SigninPageLocators.location_signUp_state1).get_attribute('value'))
        locationInfo['state2'] = self.driver.find_element(
            *SigninPageLocators.location_signUp_state1).get_attribute('value')
        shippingInfo['state1'] = self.driver.find_element(
            *SigninPageLocators.location_signUp_state1).get_attribute('value')

        loc_post_code1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_post_code1)
        loc_post_code1.send_keys("test post")

        loc_other_phn1 = self.driver.find_element(
            *SigninPageLocators.location_signUp_otherphn1)
        loc_other_phn1.send_keys("22222")

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        loc_post_code2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_post_code2)
        loc_post_code2.send_keys("test post")

        loc_email2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_email2)
        loc_email2.send_keys("test.email.com")

        loc_phn2 = self.driver.find_element(
            *SigninPageLocators.location_signUp_phn2)
        loc_phn2.send_keys("1111")

        self.click_location_signup_button()
        time.sleep(1)

        try:
            assert self.loc1_post_error() == True
            print("Success: sign-up location-1 invalid post-code error found.")
        except:
            print("No result found for invalid location-1 post-code")

        try:
            assert self.loc1_other_phone_error() == True
            print("Success: sign-up location-1 invalid other-number error found.")
        except:
            print("No result found for invalid location-1 other-phone number")

        try:
            assert self.loc2_post_error() == True
            print("Success: sign-up location-2 invalid post-code error found.")
        except:
            print("No result found for invalid location-2 post-code")

        try:
            assert self.loc2_email_error() == True
            print("Success: sign-up location-2 invalid email error found.")
        except:
            print("No result found for invalid location-2 email")

        try:
            assert self.loc2_phn_error() == True
            print("Success: sign-up location-2 invalid phone-number error found.")
        except:
            print("No result found for invalid location-2 phone-number")

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(document.body.scrollHeight, 0);")
        time.sleep(1)

        loc_post_code1.clear()
        loc_post_code1.send_keys(fake.postcode())
        print ('11)post_code1: %s' % loc_post_code1.get_attribute('value'))
        locationInfo['post_code1'] = loc_post_code1.get_attribute('value')

        loc_other_phn1.clear()
        loc_other_phn1.send_keys("12345678905")
        print ('12)other_phone no1: %s' %
               loc_other_phn1.get_attribute('value'))
        locationInfo['other_phone_no1'] = loc_other_phn1.get_attribute('value')

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        loc_post_code2.clear()
        loc_post_code2.send_keys(fake.postcode())
        print ('13)post_code2: %s' % loc_post_code2.get_attribute('value'))
        locationInfo['post_code2'] = loc_post_code2.get_attribute('value')
        shippingInfo['post_code1'] = loc_post_code2.get_attribute('value')

        loc_email2.clear()
        loc_email2.send_keys(fake.email())
        print ('14) email2: %s' % loc_email2.get_attribute('value'))
        locationInfo['email2'] = loc_email2.get_attribute('value')
        shippingInfo['email1'] = loc_email2.get_attribute('value')

        loc_phn2.clear()
        loc_phn2.send_keys("12345678906")
        print ('15) phone_no2: %s' % loc_phn2.get_attribute('value'))
        locationInfo['phone_no2'] = loc_phn2.get_attribute('value')
        shippingInfo['phone_no1'] = loc_phn2.get_attribute('value')
        print (locationInfo)
        # Modal

        self.driver.find_element(
            *SigninPageLocators.location_signUp_add_loc).click()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.location_signUp_delete3).click()

        self.wait_for_element(SigninPageLocators.location_signUp_del_modal)
        self.driver.find_element(
            *SigninPageLocators.location_signUp_del_modal).click()

        self.click_location_signup_button()

    def click_location_signup_button(self):
        time.sleep(1)
        loc = self.driver.find_element(
            *SigninPageLocators.loc_next_btn)
        loc.click()
