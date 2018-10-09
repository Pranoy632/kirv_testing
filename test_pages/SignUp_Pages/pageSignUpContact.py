import sys
sys.path.append('../test_locators')
import time

from Basepage import BasePage, fake
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpContact(BasePage):

    def company_name_error(self):
        companyName = self.driver.find_element(
            *SigninPageLocators.contactInfo_companyName_error)
        print("signup-contact comapany-name blank",
              companyName.is_displayed())
        return companyName.is_displayed()

    def contact_name_error(self):
        contactName = self.driver.find_element(
            *SigninPageLocators.contactInfo_contactName_error)
        print("signup-contact contact-name blank",  contactName.is_displayed())
        return contactName.is_displayed()

    def phone_number_error(self):
        phn_number = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_phn_number_error)
        print("signup-contact phone-number blank or invalid",
              phn_number.is_displayed())
        return phn_number.is_displayed()

    def fill_fields(self):

        self.wait_for_element(
            SigninPageLocators.contactInfo_signUp_companyName)

        self.click_contact_signup_button()
        time.sleep(1)

        try:
            assert self.company_name_error()
        except:
            print("No result found for blank comapany-name.")

        input_companyName = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_companyName)
        input_companyName.send_keys(fake.company())

        self.click_contact_signup_button()
        time.sleep(1)

        try:
            assert self.contact_name_error()
        except:
            print("No result found for blank contact-name.")

        try:
            assert self.phone_number_error()
        except:
            print("No result found for blank phone-number")

        self.wait_for_element_clickable(
            SigninPageLocators.contactInfo_signUp_contactName)

        input_contactName = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_contactName)
        input_contactName.send_keys(fake.name())

        input_phn = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_phn)
        input_phn.send_keys('4545')

        self.click_contact_signup_button()
        time.sleep(1)

        try:
            assert self.phone_number_error()
        except:
            print("No result found for blank phone-number")

        input_phn.clear()
        input_phn.send_keys('12345678901')

        self.click_contact_signup_button()

    def click_contact_signup_button(self):
        element_contact_signup = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_btn)
        element_contact_signup.click()
