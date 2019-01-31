from random import randrange
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

    def check_headers(self, form_head):
        for head in self.driver.find_elements_by_xpath('//h3'):
            if head.text == form_head:
                try:
                    assert head.text == form_head
                except:
                    print("Form %s header does not found." % (form_head))

    def click_on_continue_button(self):
        self.driver.find_element(
            *CompanyInfoLocators.continue_btn).click()

    def company_info_page_element(self):
        try:
            assert self.check_kirv_logo() == True
        except:
            print("No result found for kirv logo in company Info page.")

        try:
            assert self.check_quit_sign_up_title() == 'Quit sign up'
        except:
            print("No result found for contact info quit sign-up title.")

        try:
            assert self.check_step() == 'Step 1 of 5 - Company information'
        except:
            print("No result found for step 1 of 5 title found.")

        try:
            assert self.check_welcome_title() == 'Welcome to Kirv!'
        except:
            print("No result found for welcome to kirv title.")

        try:
            assert self.check_company_signup_note_para(
            ) == 'We are pleased to confirm your account has been successfully created. Next up, please tell us a little about your company.'
        except:
            print("No result found for tell me about comapny para.")

        self.check_headers('Company address')

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        self.driver.execute_script(
            "window.scrollTo(document.body.scrollHeight, 0);")
        time.sleep(1)

        self.driver.find_element(*CompanyInfoLocators.address_input).send_keys(
            fake.building_number() + " " + fake.street_name())

        self.driver.find_element(
            *CompanyInfoLocators.city_input).send_keys(fake.city())

        self.driver.find_element(
            *CompanyInfoLocators.state_input).click()
        time.sleep(1)
        dropdown_values = self.driver.find_element(
            *CompanyInfoLocators.dropdown_values)
        states_list = dropdown_values.find_elements_by_tag_name('li')
        random.choice(states_list[1:]).click()

        self.driver.find_element(
            *CompanyInfoLocators.zip_code_input).send_keys(fake.postcode())

        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        self.check_headers('Reseller ID & website')

        self.driver.find_element(
            *CompanyInfoLocators.reseller_id_input).send_keys(fake.random_int(min=0, max=9999))

        self.driver.find_element(
            *CompanyInfoLocators.company_website_input).send_keys(fake.domain_name())

        self.check_headers('Contact info')

        self.driver.find_element(
            *CompanyInfoLocators.email_input).send_keys(fake.company_email())

        self.driver.find_element(
            *CompanyInfoLocators.phone_number).send_keys(self.create_phone_number())

        self.driver.find_element(
            *CompanyInfoLocators.alter_phone_number).send_keys(self.create_phone_number())

        self.click_on_continue_button()
        time.sleep(1)
