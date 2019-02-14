#import requests
from pages.basepage import *
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import SignupPageLocators, CreateAccountLocators,  ContactInfoLocators
#from .create_account import token_data

contact_info = {}

class ContactInfo(BasePage):

    def check_kirv_logo(self):
        return self.driver.find_element(*ContactInfoLocators.kirv_logo).is_displayed()

    def check_create_acc_title(self):
        return self.driver.find_element(*CreateAccountLocators.create_account_title).text

    def check_quit_sign_up_title(self):
        return self.driver.find_element(*ContactInfoLocators.quit_sign_up).text

    def check_tell_us_about_para(self):
        return self.driver.find_element(*ContactInfoLocators.tell_us_about_para).text

    def click_create_account_btn(self):
        time.sleep(3)
        self.driver.find_element(
            *ContactInfoLocators.create_account_button).click()

    def company_name_error(self):
        return self.driver.find_element(*ContactInfoLocators.company_name_err).text

    def contact_name_error(self):
        return self.driver.find_element(*ContactInfoLocators.contact_name_err).text

    def phone_error(self):
        return self.driver.find_element(*ContactInfoLocators.phone_err).text

    def clear_put_value(self, locator):
        """
        clears and puts input in input box
        """
        time.sleep(2)
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    def contact_info_page_element(self):
        time.sleep(2)

        try:
            assert self.check_kirv_logo() == True
        except:
            print("No result found for kirv logo in contact Info page.")

        try:
            assert self.check_quit_sign_up_title() == 'Quit sign up'
        except:
            print("No result found for contact info quit sign-up title.")

        try:
            assert self.check_create_acc_title() == "Create your accounts"
        except:
            print("No result found for create account title in contact Info page..")

        try:
            assert self.check_tell_us_about_para(
            ) == "Tell us about you and your company and lets get your Kirv platform account created."
        except:
            print("No result found for tell us about title in contact info page.")

        self.click_create_account_btn()
        time.sleep(3)

        try:
            assert self.company_name_error() == "This field is required."
        except:
            print("No result found for contact info company name field is required.")

        company_name_field = self.driver.find_element(
            *ContactInfoLocators.company_name_input)

        company_name_field.send_keys(fake.company())

        self.click_create_account_btn()
        time.sleep(3)

        try:
            assert self.contact_name_error() == "This field may not be blank."
        except:
            print("No result found for contact info contact name field is blank.")

        try:
            assert self.phone_error() == "This field may not be blank."
        except:
            print("No result found for contact info phone number field is blank.")

        contact_name_field = self.driver.find_element(
            *ContactInfoLocators.contact_name_input)

        phone_num_field = self.driver.find_element(
            *ContactInfoLocators.phone_input)

        contact_name_field.send_keys(fake.name())

        phone_num_field.send_keys(self.create_phone_number())

        self.clear_put_value(ContactInfoLocators.company_name_input)

        self.click_create_account_btn()
        time.sleep(3)

        try:
            assert self.company_name_error() == "This field may not be blank."
        except:
            print("No result found for contact info company name field blank.")

        company_name_field.send_keys(fake.company())

        self.clear_put_value(ContactInfoLocators.phone_input)

        phone_num_field.send_keys('54667')

        self.click_create_account_btn()
        time.sleep(3)

        try:
            assert self.phone_error() == "The phone number entered is not valid."
        except:
            print("No result found for contact info phone number is not valid.")

        self.clear_put_value(ContactInfoLocators.phone_input)

        phone_num_field.send_keys(self.create_phone_number())

        contact_info['company_name'] = company_name_field.get_attribute('value')
        contact_info['contact_name'] = contact_name_field.get_attribute('value')
        contact_info['phone_no'] = phone_num_field.get_attribute('value')

        self.click_create_account_btn()


    #    self.get_contact_data()

    # def get_contact_data(self):
    #     usr = self.driver.execute_script(
    #         'return JSON.parse(localStorage.getItem("user"));')['accesses']
    #     print("---------user---------", usr)
    #     token_data['accesses'] = usr
    #     print("-----token----------",
    # token_data['accesses'][0]['buyer'], token_data['accesses'][0]['id'])

    #     req = requests.get("https://kirv-services-staging.herokuapp.com/buyer/" +
    # str(token_data['accesses'][0]['buyer']) + "/contact/",
    # headers={"content-type": "application/json", "Authorization": "token " +
    # str(token_data['token']), "X-Access-Id":
    # str(token_data['accesses'][0]['id'])})

    #     print(req.content)
