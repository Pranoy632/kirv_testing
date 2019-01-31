from pages.basepage import *
from locators.sign_up_locators.locatorSignup import CompanyInfoLocators, ContactInfoLocators, AcknowledgementLocator


class Acknowledgement(BasePage):
    def check_kirv_logo(self):
        return self.driver.find_element(*CompanyInfoLocators.step_kirv_logo).is_displayed()

    def check_quit_sign_up_title(self):
        return self.driver.find_element(*ContactInfoLocators.quit_sign_up).text

    def check_title_header(self, locator):
        return self.driver.find_element(*locator).text

    def check_submit_button(self):
        return self.driver.find_element(*AcknowledgementLocator.submit_app_button)

    def check_elements_in_acknowledgement(self):
        try:
            assert self.check_kirv_logo() == True
        except:
            print("No result found for acknowledgement kirv logo.")

        try:
            assert self.check_quit_sign_up_title() == 'Quit sign up'
        except:
            print("No result found acknowledgement quit sign up title.")

        try:
            assert self.check_title_header(
                AcknowledgementLocator.Great_everything_title) == "Great, that’s everything we need!"
        except:
            print(
                "No result found for acknowledgement Great, that’s everything we need! title.")

        try:
            assert self.check_title_header(
                AcknowledgementLocator.submit_application_title) == "Please read and accept the disclaimer below to submit your application."
        except:
            print(
                "No result found for acknowledgement please read and accept the disclaimer below to submit your application title.")

        try:
            assert self.check_title_header(
                AcknowledgementLocator.disclaimer_header) == "Disclaimer"
        except:
            print(
                "No result found for acknowledgement Disclaimer title.")

        try:
            assert self.check_title_header(
                AcknowledgementLocator.disclaimer_label) == "I acknowledge that the information on this application is true and correct to the best of my knowledge, and hereby authorize Kirv to process this application and release this information to Kirv for their review. I also understand that submitting this application does not guarantee account approval."
        except:
            print("No result found for acknowledgement para")

        try:
            assert self.check_submit_button().is_displayed() == True
        except:
            print("No result found for acknowledgement submit application button.")

        # def inner_check_button_func(toggle):
        #     if self.check_submit_button().is_enabled():
        #         print("Submit button is enabled by %s." % (toggle))
        #     else:
        #         print("Submit button is disabled by %s." % (toggle))

        #inner_check_button_func('1st check')

        try:
            assert self.check_submit_button().is_enabled() == False
        except:
            print("Acknowlegement button disable error found on 1st check")

        self.driver.find_element(
            *AcknowledgementLocator.disclaimer_label).click()

        # inner_check_button_func('label')

        try:
            assert self.check_submit_button().is_enabled() == True
        except:
            print("Acknowlegement button enable error found on label")

        self.driver.find_element(
            *AcknowledgementLocator.disclaimer_label).click()

        # inner_check_button_func('label')

        try:
            assert self.check_submit_button().is_enabled() == False
        except:
            print("Acknowlegement button disable error found on label")

        self.driver.find_element(
            *AcknowledgementLocator.disclaimer_check_box).click()

        # inner_check_button_func('checkbox')

        try:
            assert self.check_submit_button().is_enabled() == True
        except:
            print("Acknowlegement button enable error found on checkbox")

        self.driver.find_element(
            *AcknowledgementLocator.disclaimer_check_box).click()

        # inner_check_button_func('checkbox')

        try:
            assert self.check_submit_button().is_enabled() == False
        except:
            print("Acknowlegement button disable error found on checkbox")

        self.driver.find_element(
            *AcknowledgementLocator.disclaimer_check_box).click()

        # inner_check_button_func('checkbox')

        try:
            assert self.check_submit_button().is_enabled() == True
        except:
            print("Acknowlegement button enable error found on checkbox lastcheck")

        ''' Submit appplication button'''
        self.driver.find_element(
            *AcknowledgementLocator.submit_app_button).click()
