from pages.basepage import *
from locators.sign_up_locators.locatorSignup import CompanyInfoLocators, ContactInfoLocators, CongratulationLocators


class Cogratulations(BasePage):

    def check_kirv_logo(self):
        return self.driver.find_element(*CompanyInfoLocators.step_kirv_logo).is_displayed()

    def check_title_congratulations(self, locator):
        return self.driver.find_element(*locator).text

    def check_button_back_website(self):
        return self.driver.find_element(CongratulationLocators.back_to_wesite_button)

    def check_elements_in_congratulation_page(self):
        time.sleep(2)

        try:
            assert self.check_kirv_logo() == True
        except:
            print("No result found for congratulation kirv logo.")

        try:
            assert self.check_title_congratulations(
                CongratulationLocators.congratulations_title) == 'Congratulations!'
        except:
            print("No result found for congratulations title.")

        try:
            self.check_title_congratulations(
                CongratulationLocators.application_successfully_sub_head) == 'Your application has been successfully submitted. We’re now in the process of reviewing it. Once approved, you’ll receive a digital contract from us that you’ll need to sign before getting full access to the Kirv Marketplace, so you can start placing orders!'
        except:
            print(
                "No result found for congratulations application successfully sub head.")

        try:
            self.driver.find_element(
                *CongratulationLocators.back_to_wesite_button).is_displayed() == True
        except:
            print("No result found for back to website button.")

        self.driver.find_element(
            *CongratulationLocators.back_to_wesite_button).click()
