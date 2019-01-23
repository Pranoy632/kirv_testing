from pages.basepage import *
from locators.sign_up_locators.locatorSignup import CompanyInfoLocators, ContactInfoLocators, CongratulationLocators


class Cogratulations(BasePage):

    def check_kirv_logo(self):
        return self.driver.find_element(*CompanyInfoLocators.step_kirv_logo).is_displayed()

    def check_title_congratulations(self, locator):
        return self.driver.find_element(*locator).text

    def check_elements_in_congratulation_page(self):
        try:
            assert self.check_kirv_logo() == True
            print("Success: congratulation kirv logo found.")
        except:
            print("No result found for congratulation kirv logo.")

        try:
            assert self.check_title_congratulations(
                CongratulationLocators.congratulations_title) == 'Congratulations!'
            print("Success: Congratulations title found.")
        except:
            print("No result found for congratulations title.")

        print(self.check_title_congratulations(
            CongratulationLocators.application_successfully_sub_head))
