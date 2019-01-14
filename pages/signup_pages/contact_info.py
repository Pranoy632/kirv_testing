from pages.basepage import *
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import SignupPageLocators, CreateAccountLocators,  ContactInfoLocators


class ContactInfo(BasePage):

    def check_kirv_logo(self):
        return self.driver.find_element(*SignupPageLocators.kirv_logo).is_displayed()

    def check_create_acc_title(self):
        return self.driver.find_element(*CreateAccountLocators.create_account_title).text

    def check_quit_sign_up_title(self):
        return self.driver.find_element(*ContactInfoLocators.quit_sign_up).text

    def check_tell_us_about_para(self):
        return self.driver.find_element(*ContactInfoLocators.tell_us_about_para).text

    def click_create_account_btn(self):
        self.driver.find_element(
            *ContactInfoLocators.create_account_button).click()

    def company_name_error(self):
        return self.driver.find_element(*ContactInfoLocators.comapany_name_err).text

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
        try:
            assert self.check_kirv_logo() == True
            print("Success: kirv logo found on contact Info page.")
        except:
            print("No result found for kirv logo in contact Info page.")

        try:
            assert self.check_quit_sign_up_title() == 'Quit sign up'
            print("Success: contact info quit sign-up title found.")
        except:
            print("No result found for contact info quit sign-up title.")

        try:
            assert self.check_create_acc_title() == "Create your account"
            print("Success: create account title found in contact Info page.")
        except:
            print("No result found for create account title in contact Info page..")

        try:
            assert self.check_tell_us_about_para(
            ) == "Tell us about you and your company and lets get your Kirv platform account created."
            print("Success: Tell us about title found in contact info page.")
        except:
            print("No result found for tell us about title in contact info page.")

        self.click_create_account_btn()
        time.sleep(3)

        try:
            assert self.company_name_error() == "This field is required."
            print("Success: contact info comapany name feild is required error found.")
        except:
            print("No result found for contact info company name feild is required.")

        comapany_name_feild = self.driver.find_element(
            *ContactInfoLocators.comapany_name_input)

        comapany_name_feild.send_keys(fake.company())

        self.click_create_account_btn()
        time.sleep(3)

        try:
            assert self.contact_name_error() == "This field is required."
            print("Success: contact info contact name feild is required error found.")
        except:
            print("No result found for contact info contact name feild is required.")

        try:
            assert self.phone_error() == "This field is required."
            print("Success: contact info phone number feild is required error found.")
        except:
            print("No result found for contact info phone number feild is required.")

        contact_name_feild = self.driver.find_element(
            *ContactInfoLocators.contact_name_input)

        phone_num_feild = self.driver.find_element(
            *ContactInfoLocators.phone_input)

        contact_name_feild.send_keys(fake.name())

        phone_num_feild.send_keys(self.create_phone_number())

        self.clear_put_value(ContactInfoLocators.comapany_name_input)

        self.click_create_account_btn()
        time.sleep(3)

        try:
            assert self.company_name_error() == "This field may not be blank."
            print("Success: contact info comapany name feild blank error found.")
        except:
            print("No result found for contact info company name feild blank.")

        comapany_name_feild.send_keys(fake.company())

        self.clear_put_value(ContactInfoLocators.phone_input)

        phone_num_feild.send_keys('54667')

        self.click_create_account_btn()
        time.sleep(3)

        try:
            assert self.phone_error() == "The phone number entered is not valid."
            print("Success: contact info phone number is not valid error found.")
        except:
            print("No result found for contact info phone number is not valid.")

        self.clear_put_value(ContactInfoLocators.phone_input)

        phone_num_feild.send_keys(self.create_phone_number())

        self.click_create_account_btn()
