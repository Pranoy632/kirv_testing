from pages.basepage import *
from locators.sign_up_locators.locatorSignup import BackAStep
import time

class BackStep(BasePage):

    def check_back_step(self):
        time.sleep(1)
        self.check_application()
        self.driver.find_element(
            *BackAStep.back_a_step).click()

        self.check_purchasing_volumes()
        self.driver.find_element(
            *BackAStep.back_a_step).click()

        self.check_purchasing_preferences()
        self.driver.find_element(
            *BackAStep.back_a_step).click()

        self.check_warehouse_location()
        self.driver.find_element(
            *BackAStep.back_a_step).click()

        self.check_location_confirmation()
        self.driver.find_element(
            *BackAStep.back_a_step).click()

        self.check_retail_location()
        self.driver.find_element(
            *BackAStep.back_a_step).click()

        self.check_company_information()
        time.sleep(1)
        self.goto_application()

    def check_application(self):
        self.equality_assert(
                self.driver.find_element(*BackAStep.kirv_logo).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.disclaimer).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.submit_application).is_displayed(), True)

    def check_purchasing_volumes(self):
        self.equality_assert(
                self.driver.find_element(*BackAStep.kirv_logo).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.step5).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.question1).is_displayed(), True)

    def check_purchasing_preferences(self):
        self.equality_assert(
                self.driver.find_element(*BackAStep.kirv_logo).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.step4).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.cooking).is_displayed(), True)

    def check_warehouse_location(self):
        self.equality_assert(
                self.driver.find_element(*BackAStep.kirv_logo).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.step3).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.num1).is_displayed(), True)

    def check_location_confirmation(self):
        self.equality_assert(
                self.driver.find_element(*BackAStep.kirv_logo).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.step3).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.retail_location).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.confirm_btn).is_displayed(), True)

    def check_retail_location(self):
        self.equality_assert(
                self.driver.find_element(*BackAStep.kirv_logo).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.step2).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.num1).is_displayed(), True)

    def check_company_information(self):
        self.equality_assert(
                self.driver.find_element(*BackAStep.kirv_logo).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.step1).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.welcome).is_displayed(), True)
        self.equality_assert(
                self.driver.find_element(*BackAStep.company_address).is_displayed(), True)

    def goto_application(self):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', self.driver.find_element(
            *BackAStep.continue_btn))
        self.driver.find_element(*BackAStep.continue_btn).click()
        time.sleep(1)
        self.driver.find_element(*BackAStep.num1).click()
        self.driver.find_element(*BackAStep.update_location).click()
        self.driver.find_element(*BackAStep.next_btn).click()
        self.driver.find_element(*BackAStep.confirm_btn).click()
        time.sleep(1)
        self.driver.find_element(*BackAStep.num1).click()
        self.driver.find_element(*BackAStep.update_location).click()
        self.driver.execute_script('arguments[0].scrollIntoView(true);', self.driver.find_element(
            *BackAStep.confirm_btn))
        self.driver.find_element(*BackAStep.confirm_btn).click()
        time.sleep(1)
        self.driver.find_element(*BackAStep.continue_btn).click()
        time.sleep(1)
        self.driver.find_element(*BackAStep.continue_btn).click()
        self.driver.find_element(*BackAStep.continue_btn).click()
        self.driver.find_element(*BackAStep.continue_btn).click()
        self.driver.find_element(*BackAStep.continue_btn).click()
        
