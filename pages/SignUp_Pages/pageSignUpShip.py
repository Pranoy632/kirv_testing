import sys
sys.path.append('../locators')

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from pages.basepage import BasePage, fake
from locators import SigninPageLocators
from .pageSignUpLocation import shippingInfo


class SignUpShipTo(BasePage):

    def step_check(self):
        time.sleep(2)
        step_3 = None
        self.wait_for_element(SigninPageLocators.steps)
        step = self.driver.find_element(
            *SigninPageLocators.steps)
        step_li = step.find_elements_by_tag_name("li")

        for item in step_li:
            is_active = "active" in item.get_attribute("class")
            if is_active:
                step_3 = item.text
        if step_3 == str(3):
            print("Success: Step %s is active." % (step_3))
        else:
            print("No result found for step %s active." % (step_3))

    def title_check(self):
        self.wait_for_element(
            SigninPageLocators.ship_title)

        title = self.driver.find_element(
            *SigninPageLocators.ship_title)

        try:
            assert title.is_displayed() == True
            print("Success: ship/warehouse title found.")
        except:
            print("No result found for ship/warehouse title.")

    def ship2_street_error(self):
        street_er = self.driver.find_element(
            *SigninPageLocators.ship2_street_err)
        return street_er.is_displayed()

    def ship2_city_error(self):
        city_er = self.driver.find_element(
            *SigninPageLocators.ship2_city_err)
        return city_er.is_displayed()

    def ship2_post_error(self):
        post_error = self.driver.find_element(
            *SigninPageLocators.ship2_post_err)
        return post_error.is_displayed()

    def ship2_email_error(self):
        email_error = self.driver.find_element(
            *SigninPageLocators.ship2_email_err)
        return email_error.is_displayed()

    def ship2_phn_error(self):
        phn_error = self.driver.find_element(
            *SigninPageLocators.ship2_phn_err)
        return phn_error.is_displayed()

    def ship_other_phone_error(self):
        othr_er = self.driver.find_element(
            *SigninPageLocators.ship2_othr_phn_err)
        return othr_er.is_displayed()

    def fill_fields(self):
        self.wait_for_element(SigninPageLocators.ship_signUp_start_time)

        self.driver.find_element(
            *SigninPageLocators.ship_signUp_start_time).click()

        self.wait_for_element(SigninPageLocators.ship_start_time)

        self.driver.find_element(
            *SigninPageLocators.ship_start_time).click()

        self.driver.find_element(
            *SigninPageLocators.ship_ok_btn_start_end).click()
        print ('1) Start Time1: %s' % self.driver.find_element(
            *SigninPageLocators.ship_signUp_start_time).get_attribute('value'))
        shippingInfo['start_time1'] = self.driver.find_element(
            *SigninPageLocators.ship_signUp_start_time).get_attribute('value')

        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.ship_signUp_end_time).click()

        self.wait_for_element(SigninPageLocators.ship_end_time)

        self.driver.find_element(
            *SigninPageLocators.ship_end_time).click()

        self.driver.find_element(
            *SigninPageLocators.ship_ok_btn_start_end).click()
        print ('2) End Time1: %s' % self.driver.find_element(
            *SigninPageLocators.ship_signUp_end_time).get_attribute('value'))
        shippingInfo['end_time1'] = self.driver.find_element(
            *SigninPageLocators.ship_signUp_end_time).get_attribute('value')

        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.ship_signUp_add_ship2).click()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        ship_name2 = self.driver.find_element(
            *SigninPageLocators.ship2_name)
        ship_name2.send_keys(fake.street_name())
        print ('3) name2: %s' % ship_name2.get_attribute('value'))
        shippingInfo['name2'] = ship_name2.get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.ship2_state).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        print ('4) state2: %s' % self.driver.find_element(
            *SigninPageLocators.ship2_state).get_attribute('value'))
        shippingInfo['state2'] = self.driver.find_element(
            *SigninPageLocators.ship2_state).get_attribute('value')

        self.driver.find_element(
            *SigninPageLocators.ship2_start).click()

        self.wait_for_element(SigninPageLocators.ship_start_time)

        self.driver.find_element(
            *SigninPageLocators.ship_start_time).click()

        self.driver.find_element(
            *SigninPageLocators.ship_ok_btn_start_end).click()
        print ('5) start time2: %s' % self.driver.find_element(
            *SigninPageLocators.ship2_start).get_attribute('value'))
        shippingInfo['start_time2'] = self.driver.find_element(
            *SigninPageLocators.ship2_start).get_attribute('value')

        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.ship2_end).click()

        self.wait_for_element(SigninPageLocators.ship_end_time)

        self.driver.find_element(
            *SigninPageLocators.ship_end_time).click()

        self.driver.find_element(
            *SigninPageLocators.ship_ok_btn_start_end).click()
        print ('6) end_time2: %s' % self.driver.find_element(
            *SigninPageLocators.ship2_end).get_attribute('value'))
        shippingInfo['end_time2'] = self.driver.find_element(
            *SigninPageLocators.ship2_end).get_attribute('value')

        self.click_ship_signup_button()
        time.sleep(1)

        try:
            assert self.ship2_street_error() == True
            print("Success: signup shipTo-2  street-address blank error found.")
        except:
            print("No result found for shipTo-2 blank street-address")

        try:
            assert self.ship2_city_error() == True
            print("Success: signup shipTo-2  city blank error found.")
        except:
            print("No result found for shipTo-2 blank city")

        try:
            assert self.ship2_post_error() == True
            print("Success: signup shipTo-2  post-code blank error found.")
        except:
            print("No result found for shipTo-2 blank post-code")

        try:
            assert self.ship2_email_error() == True
            print("Success: signup shipTo-2  email blank error found.")
        except:
            print("No result found for shipTo-2 blank email")

        try:
            assert self.ship2_phn_error() == True
            print("Success: signup shipTo-2 phone-number blank error found.")
        except:
            print("No result found for shipTo-2 blank phone-number")

        ship_street2 = self.driver.find_element(
            *SigninPageLocators.ship2_street_add)
        ship_street2.send_keys(fake.building_number() +
                               " " + fake.street_name())
        print ('7) street2: %s' % ship_street2.get_attribute('value'))
        shippingInfo['street2'] = ship_street2.get_attribute('value')

        ship_city2 = self.driver.find_element(
            *SigninPageLocators.ship2_city)
        ship_city2.send_keys(fake.city())
        print ('8) city2: %s' % ship_city2.get_attribute('value'))
        shippingInfo['city2'] = ship_city2.get_attribute('value')

        ship_post2 = self.driver.find_element(
            *SigninPageLocators.ship2_post)
        ship_post2.send_keys("test post")

        ship_email2 = self.driver.find_element(
            *SigninPageLocators.ship2_email)
        ship_email2.send_keys("testemail.com")

        ship_phn2 = self.driver.find_element(
            *SigninPageLocators.ship2_phn)
        ship_phn2.send_keys('1111')

        ship_othr_phn2 = self.driver.find_element(
            *SigninPageLocators.ship2_othr_phn)
        ship_othr_phn2.send_keys('2222')

        self.click_ship_signup_button()
        time.sleep(1)

        try:
            assert self.ship2_post_error() == True
            print("Success: signup shipTo-2  post-code invalid error found.")
        except:
            print("No result found for invalid ship-2 post-code")

        try:
            assert self.ship2_email_error() == True
            print("Success: signup shipTo-2  email invalid error found.")
        except:
            print("No result found for invalid ship-2 email")

        try:
            assert self.ship2_phn_error() == True
            print("Success: signup shipTo-2  phone-number invalid error found.")
        except:
            print("No result found for invalid ship-2 phone-number")

        try:
            assert self.ship_other_phone_error() == True
            print("Success: signup shipTo-2  other-phone-number invalid error found.")
        except:
            print("No result found for invalid ship-2 other-phone-number")

        ship_post2.clear()
        ship_post2.send_keys(fake.postcode())
        print ('9) post_code: %s' % ship_post2.get_attribute('value'))
        shippingInfo['post_code2'] = ship_post2.get_attribute('value')

        ship_email2.clear()
        ship_email2.send_keys(fake.email())
        print ('10) email2: %s' % ship_email2.get_attribute('value'))
        shippingInfo['email2'] = ship_email2.get_attribute('value')

        ship_phn2.clear()
        ship_phn2.send_keys('12345678907')
        print ('11) phone_no2: %s' % ship_phn2.get_attribute('value'))
        shippingInfo['phone_no2'] = ship_phn2.get_attribute('value')

        ship_othr_phn2.clear()
        ship_othr_phn2.send_keys('12345678908')
        print ('12) other_phone no: %s' %
               ship_othr_phn2.get_attribute('value'))
        shippingInfo['other_phone_no2'] = ship_othr_phn2.get_attribute('value')
        print (shippingInfo)

        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.ship_signUp_add_ship3).click()

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        self.driver.find_element(
            *SigninPageLocators.ship_signUp_delete3).click()

        self.wait_for_element(SigninPageLocators.ship_signUp_del_modal)
        self.driver.find_element(
            *SigninPageLocators.ship_signUp_del_modal).click()

        self.click_ship_signup_button()

    def click_ship_signup_button(self):
        time.sleep(1)
        ship = self.driver.find_element(
            *SigninPageLocators.ship_next_btn)
        ship.click()
