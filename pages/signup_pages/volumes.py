from random import randrange
from pages.basepage import *
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import CompanyInfoLocators, ContactInfoLocators, VolumesLocators


class Volumes(BasePage):
    def check_kirv_logo(self):
        return self.driver.find_element(*CompanyInfoLocators.step_kirv_logo).is_displayed()

    def check_quit_sign_up_title(self):
        return self.driver.find_element(*ContactInfoLocators.quit_sign_up).text

    def check_volumes_step(self):
        return self.driver.find_element(*VolumesLocators.volume_step).text

    def check_volumes_title(self):
        return self.driver.find_element(*VolumesLocators.volumes_title).text

    def check_element_in_volumes_page(self):
        try:
            assert self.check_kirv_logo() == True
            print("Success: volumes kirv logo found.")
        except:
            print("No result found for volumes kirv logo.")

        try:
            assert self.check_quit_sign_up_title() == 'Quit sign up'
            print("Success: volumes quit sign up title found.")
        except:
            print("No result found volumes quit sign up title.")

        try:
            assert self.check_volumes_step() == 'Step 5 of 5 - Purchasing volumes'
            print("Success: Volume Step 5 of 5 - Purchasing volumes found.")
        except:
            print("No result found for Step 5 of 5 - Purchasing volumes title. ")

        try:
            assert self.check_volumes_title(
            ) == 'Last step - how many trucks of product do you typically order over a calendar year?'
            print("Success: volumes title found.")
        except:
            print("No result for volumes title.")

    def fill_fields(self):

        quater_list = []
        hdrs = self.driver.find_elements(*VolumesLocators.headers)

        for qutr_loop in range(len(hdrs)):
            print("-----itrations----->", qutr_loop)
            for header in hdrs:
                print("header ---->", header.text)

            list_trucks = self.driver.find_elements(
                *VolumesLocators.trucks_list)

            click_random = list_trucks[randrange(0, len(list_trucks))]

            click_random.find_element_by_xpath(
                './/div[2]/div/button[2]').click()

            click_random.find_element_by_xpath(
                './/div[2]/div/button[1]').click()

            click_random.find_element_by_xpath(
                './/div[2]/div/button[2]').click()

            self.driver.find_element_by_xpath(
                '//button[contains(text(),"Continue")]').click()
            time.sleep(1)

            self.check_complete_button()

    def check_complete_button(self):

        complete_btn = self.driver.find_elements_by_xpath(
            '//div[contains(@class, "complete-btnd")]')
        k = 0
        if len(complete_btn) >= 1:
            for comp_btn in complete_btn:
                k = k + 1
                print(k, "complete button found.")
        else:
            print("No result found for completebutton list")
