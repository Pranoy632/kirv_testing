import sys
sys.path.append('../test_locators')
import time

from Basepage import BasePage, fake
from SignUp_Locators.locatorSignup import SigninPageLocators

contactInfo = {}

class SignUpContact(BasePage):

    def company_name_error(self):
        companyName = self.driver.find_element(
            *SigninPageLocators.contactInfo_companyName_error)
        return companyName.is_displayed()

    def contact_name_error(self):
        contactName = self.driver.find_element(
            *SigninPageLocators.contactInfo_contactName_error)
        return contactName.is_displayed()

    def phone_number_error(self):
        phn_number = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_phn_number_error)
        return phn_number.is_displayed()

    def fill_fields(self):

        self.wait_for_element(
            SigninPageLocators.contactInfo_signUp_companyName)

        self.click_contact_signup_button()
        time.sleep(1)

        try:
            assert self.company_name_error() == True
            print("Success: signup-contact comapany-name blank error found.")
        except:
            print("No result found for blank comapany-name.")

        input_companyName = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_companyName)
        input_companyName.send_keys(fake.company())
        print ('1) companyName: %s'%input_companyName.get_attribute('value'))
        contactInfo['company_name'] = input_companyName.get_attribute('value')

        self.click_contact_signup_button()
        time.sleep(1)

        try:
            assert self.contact_name_error() == True
            print("Success: signup-contact contact-name blank error found.")
        except:
            print("No result found for blank contact-name.")

        try:
            assert self.phone_number_error() == True
            print("Success: signup-contact phone-number blank error found.")
        except:
            print("No result found for blank phone-number")

        self.wait_for_element_clickable(
            SigninPageLocators.contactInfo_signUp_contactName)

        input_contactName = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_contactName)
        input_contactName.send_keys(fake.name())
        print ('2) contactName: %s'%input_contactName.get_attribute('value'))
        contactInfo['contact_name'] = input_contactName.get_attribute('value')

        input_phn = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_phn)
        input_phn.send_keys('4545')

        self.click_contact_signup_button()
        time.sleep(1)

        try:
            assert self.phone_number_error() == True
            print("Success: signup-contact phone-number invalid error found.")
        except:
            print("No result found for invalid phone-number")
        
        time.sleep(1)
        input_phn.clear()
        time.sleep(1)
        input_phn.send_keys('12345678900')
        print ('3) Phone no.: %s'%input_phn.get_attribute('value'))
        contactInfo['phone_no'] = input_phn.get_attribute('value')
        print (contactInfo)

        self.click_contact_signup_button()

    def click_contact_signup_button(self):
        element_contact_signup = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_btn)
        try:
            element_contact_signup.click()
        except:
            self.close_chat_popup()
            element_contact_signup.click()
