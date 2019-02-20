from random import randrange
from pages.basepage import *
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import CompanyInfoLocators, CategoriesLocators,  ContactInfoLocators

purchasing_preferences = {}

class Categories(BasePage):

    def check_kirv_logo(self):
        return self.driver.find_element(*CompanyInfoLocators.step_kirv_logo).is_displayed()

    def check_quit_sign_up_title(self):
        return self.driver.find_element(*ContactInfoLocators.quit_sign_up).text

    def check_categories_step(self):
        return self.driver.find_element(*CategoriesLocators.categories_step).text

    def check_often_do_you_purchase_title(self):
        return self.driver.find_element(*CategoriesLocators.often_purchase_title).text

    def elements_of_categories(self):
        try:
            assert self.check_kirv_logo() == True
        except:
            print("No result found for categories kirv logo.")

        try:
            assert self.check_quit_sign_up_title() == 'Quit sign up'
        except:
            print("No result found categories quit sign up title.")

        try:
            assert self.check_categories_step() == 'Step 4 of 5 - Purchasing preferences'
        except:
            print("No result found for Step 4 of 5 - Purchasing preferences title.")

        try:
            assert self.check_often_do_you_purchase_title(
            ) == 'How often do you purchase these types of product?'
        except:
            print("No result found for categories often purchase title.")

    def fill_fields(self):

        title_check = None

        categories_title_itr = self.driver.find_elements(
            *CategoriesLocators.categories_title)

        for itr in range(len(categories_title_itr)):
            for category in categories_title_itr:
                links = category.find_elements_by_tag_name('li')
                if len(links) > 1:
                    title_check = links[0].text
                #     for l in links:
                #         print("------->", l.text)
                # else:
                #     for l in links:
                #         print(l.text)

            for sub_category in self.driver.find_elements(*CategoriesLocators.categories_ul):
                sub_links = sub_category.find_elements_by_tag_name('li')
                rand_no = randrange(1, len(sub_links))
                sub_links[rand_no].find_element_by_tag_name(
                    'div').find_element_by_tag_name('label').click()
                purchasing_preferences[sub_links[0].text] = 'often' if rand_no == 1 else 'sometimes' if rand_no == 2 else 'all_the_time' if rand_no == 3 else 'never'

            self.driver.find_element_by_xpath(
                '//button[contains(text(), "Continue")]').click()

            self.check_complete_button()
        print (purchasing_preferences)

    def check_complete_button(self):

        complete_btn = self.driver.find_elements_by_xpath(
            '//div[@class="complete-a-darrow"]/div[contains(@class, "complete-btnd")]')
        k = 0
        if len(complete_btn) >= 1:
            for comp_btn in complete_btn:
                k = k + 1
                #print(k, "complete button found.")
        else:
            print("No result found for completebutton list")
