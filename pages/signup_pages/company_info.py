from pages.basepage import *
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import SignupPageLocators, ContactInfoLocators, CompanyInfoLocators


class CompanyInfo(BasePage):

    def check_kirv_logo(self):
        return self.driver.find_element(*CompanyInfoLocators.step_kirv_logo).is_displayed()

    def check_quit_sign_up_title(self):
        return self.driver.find_element(*ContactInfoLocators.quit_sign_up).text

    def check_step(self):
        return self.driver.find_element(*CompanyInfoLocators.steps).text

    def check_welcome_title(self):
        return self.driver.find_element(*CompanyInfoLocators.welcome_title).text

    def check_company_signup_note_para(self):
        return self.driver.find_element(*CompanyInfoLocators.company_signup_note_para).text

    def company_info_page_element(self):
        try:
            assert self.check_kirv_logo() == True
            print("Success: kirv logo found on company Info page.")
        except:
            print("No result found for kirv logo in company Info page.")

        try:
            assert self.check_quit_sign_up_title() == 'Quit sign up'
            print("Success: contact info quit sign-up title found.")
        except:
            print("No result found for contact info quit sign-up title.")

        try:
            assert self.check_step() == 'Step 1 of 5 - Company information'
            print("Success: company info step 1 of 5 title found.")
        except:
            print("No result found for step 1 of 5 title found.")

        try:
            assert self.check_welcome_title() == 'Welcome to Kirv!'
            print("Success: company info welcome to kirv title found.")
        except:
            print("No result found for welcome to kirv title.")

        try:
            assert self.check_company_signup_note_para(
            ) == 'We are pleased to confirm your account has been successfully created. Next up, please tell us a little about your company.'
            print("Success: company info tell me about company para found.")
        except:
            print("No result found for tell me about comapny para.")

        time.sleep(1)
        self.driver.find_element(
            *CompanyInfoLocators.address_input).send_keys('address')

        time.sleep(1)
        self.driver.find_element(
            *CompanyInfoLocators.unit_num_input).send_keys('786')

        time.sleep(1)
        self.driver.find_element(
            *CompanyInfoLocators.city_input).send_keys('test city')

        time.sleep(1)
        self.driver.find_element(
            *CompanyInfoLocators.state_input).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        time.sleep(1)
        self.driver.find_element(
            *CompanyInfoLocators.zip_code_input).send_keys('123')

        time.sleep(1)
        self.driver.find_element(
            *CompanyInfoLocators.reseller_id_input).send_keys('786')

        time.sleep(1)
        self.driver.find_element(
            *CompanyInfoLocators.company_website_input).send_keys('test.com')

        time.sleep(1)
        self.driver.find_element(
            *CompanyInfoLocators.email_input).send_keys('test@test.com')

        time.sleep(1)
        self.driver.find_element(
            *CompanyInfoLocators.phone_number).send_keys('12345678912')

        time.sleep(1)
        self.driver.find_element(
            *CompanyInfoLocators.continue_btn).click()
