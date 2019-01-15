from abc import ABC
from pages.basepage import *
from locators.buyer_locators.account_locator import AccountLocators, UserProfileLocators, BrandLocators
from selenium.webdriver.common.keys import Keys


class AbstractClass(ABC):

    ''' Abstract Class '''

    def sub_navbar_list(self):
        self.wait_for_element(UserProfileLocators.sub_navbar_link)
        navbar_sub = self.driver.find_element(
            *UserProfileLocators.sub_navbar_link)
        navbar_sub_li = navbar_sub.find_elements_by_tag_name("li")
        return navbar_sub_li


class Account(BasePage):  # Account class

    ''' Account functionality '''

    def navbar_list(self):
        self.wait_for_element(AccountLocators.account_link)
        navbar_right = self.driver.find_element(*AccountLocators.account_link)
        navbar_li = navbar_right.find_elements_by_tag_name("li")
        return navbar_li

    def go_to_account(self):
        list_li = self.navbar_list()
        for item in list_li:
            if item.text == 'Account':
                item.click()

    def check_account_active(self):
        li_active = self.navbar_list()
        for active_item in li_active:
            is_active = "active" in active_item.get_attribute("class")
            if is_active:
                if active_item.text == 'Account':
                    print("Success: %s is active." % (active_item.text))

    def check_title_in_account(self):
        self.wait_for_element(AccountLocators.my_account_title)
        title = self.driver.find_element(
            *AccountLocators.my_account_title)
        try:
            assert title.is_displayed() == True
            print("Success: %s title found." % (title.text))
        except:
            print("No result found for My Account title.")


class UserProfile(BasePage, AbstractClass):  # user-profile class

    ''' User-profile functionality '''

    def full_name_error(self):
        return self.driver.find_element(
            *UserProfileLocators.full_name_err).is_displayed()

    def email_error(self):
        return self.driver.find_element(
            *UserProfileLocators.email_err).is_displayed()

    def phone_error(self):
        return self.driver.find_element(
            *UserProfileLocators.phone_err).is_displayed()

    def other_phone_error(self):
        return self.driver.find_element(
            *UserProfileLocators.other_phn_err).is_displayed()

    def go_to_user_profile(self):
        sub_list_li = self.sub_navbar_list()
        for sub_item in range(1, (len(sub_list_li) + 1)):
            menus = self.driver.find_element_by_css_selector(
                '.sub-navigation > li:nth-child({0})'.format(sub_item))
            if menus.text == 'User Profile':
                menus.click()

    def check_user_profile_active(self):
        sub_active = self.sub_navbar_list()
        for active_item in sub_active:
            is_active = "active" in active_item.get_attribute("class")
            if is_active:
                if active_item.text == 'User Profile':
                    print("Success: %s is active." % (active_item.text))

    def check_title_on_user_profile(self):
        self.wait_for_element(UserProfileLocators.customer_profile_title)
        title = self.driver.find_element(
            *UserProfileLocators.customer_profile_title)
        try:
            assert title.is_displayed() == True
            print("Success: %s title found." % (title.text))
        except:
            print("No result found for Customer Profile title.")

    def customer_profile_edit_btn(self):
        self.wait_for_element(UserProfileLocators.customer_pro_edit_btn)
        self.driver.find_element(
            *UserProfileLocators.customer_pro_edit_btn).click()

    def customer_profile_save_btn(self):
        self.wait_for_element(UserProfileLocators.cust_pro_save_btn)
        save = self.driver.find_element(
            *UserProfileLocators.cust_pro_save_btn)
        save.click()

    def customer_profile_cancel_btn(self):
        self.wait_for_element(UserProfileLocators.cust_pro_cancel_btn)
        cancel = self.driver.find_element(
            *UserProfileLocators.cust_pro_cancel_btn)
        cancel.click()

    def clear_put_value(self, locator):
        """
        clears and puts input in input box
        """
        time.sleep(2)
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    def check_fields(self):
        # Full name
        self.customer_profile_edit_btn()
        self.clear_put_value(UserProfileLocators.full_name)
        self.customer_profile_save_btn()
        try:
            assert self.full_name_error() == True
            print("Success: Full Name blank error found.")
        except:
            print("No result found for blank Full Name.")
        time.sleep(1)
        self.driver.find_element(
            *UserProfileLocators.full_name).send_keys('Test')
        self.customer_profile_save_btn()

        # Email
        self.customer_profile_edit_btn()
        self.clear_put_value(UserProfileLocators.email)
        self.customer_profile_save_btn()
        try:
            assert self.email_error() == True
            print("Success: Email blank error found.")
        except:
            print("No result found for blank Email.")
        time.sleep(1)
        self.driver.find_element(
            *UserProfileLocators.email).send_keys('Test@')
        self.customer_profile_save_btn()
        try:
            assert self.email_error() == True
            print("Success: Invalid Email error found.")
        except:
            print("No result found for Invalid Email.")
        time.sleep(1)
        self.clear_put_value(UserProfileLocators.email)
        self.driver.find_element(
            *UserProfileLocators.email).send_keys('shashank.n@amazatic.com')
        self.customer_profile_save_btn()

        # phone
        self.customer_profile_edit_btn()
        self.clear_put_value(UserProfileLocators.phone)
        self.customer_profile_save_btn()
        try:
            assert self.phone_error() == True
            print("Success: Phone number blank error found.")
        except:
            print("No result found for blank Phone number.")
        time.sleep(1)
        self.driver.find_element(
            *UserProfileLocators.phone).send_keys('5566')
        self.customer_profile_save_btn()
        try:
            assert self.phone_error() == True
            print("Success: Invalid Phone number error found.")
        except:
            print("No result found for Invalid Phone number.")
        time.sleep(1)
        self.clear_put_value(UserProfileLocators.phone)
        self.driver.find_element(
            *UserProfileLocators.phone).send_keys('+12102102101')
        self.customer_profile_save_btn()

        # other-phone
        self.customer_profile_edit_btn()
        self.clear_put_value(UserProfileLocators.other_phone)
        self.driver.find_element(
            *UserProfileLocators.other_phone).send_keys('5566')
        self.customer_profile_save_btn()
        try:
            assert self.other_phone_error() == True
            print("Success: Invalid Other Phone number error found.")
        except:
            print("No result found for Invalid Other Phone number.")
        time.sleep(1)
        self.clear_put_value(UserProfileLocators.other_phone)
        self.customer_profile_save_btn()

        # cancel
        self.customer_profile_edit_btn()
        self.customer_profile_cancel_btn()


class Brands(BasePage, AbstractClass):

    def check_brand_active(self):
        sub_active = self.sub_navbar_list()
        for active_item in sub_active:
            is_active = "active" in active_item.get_attribute("class")
            if is_active:
                if active_item.text == 'Brands':
                    print("Success: %s is active." % (active_item.text))

    def click_image(self):
        time.sleep(3)
        self.driver.find_element(*BrandLocators.brand_img).click()
