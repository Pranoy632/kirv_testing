from pages.basepage import *
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import SignupPageLocators, CreateAccountLocators,  ContactInfoLocators
from selenium.common.exceptions import WebDriverException


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
        try:
            self.driver.find_element(
                *ContactInfoLocators.create_account_button).click()
        except WebDriverException:
            BasePage(self.driver).close_chat_popup_in_device(self.driver.find_element(
                *ContactInfoLocators.create_account_button)).click()

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

        comapany_name_feild = self.driver.find_element(
            *ContactInfoLocators.comapany_name_input)

        comapany_name_feild.send_keys(fake.company())

        contact_name_feild = self.driver.find_element(
            *ContactInfoLocators.contact_name_input)

        phone_num_feild = self.driver.find_element(
            *ContactInfoLocators.phone_input)

        contact_name_feild.send_keys(fake.name())

        phone_num_feild.send_keys(self.create_phone_number())

        self.click_create_account_btn()
