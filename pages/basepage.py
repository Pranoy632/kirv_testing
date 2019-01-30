# import sys
# sys.path.append('../locators')
import time
import random


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Factory
from locators.sign_in_page_locators.signin_buyer_supplier_locator import SignInLocators
from selenium.webdriver.common.keys import Keys


fake = Factory.create()


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, *locator):
        " Performs wait for time provided"
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(*locator))

    def wait_for_element_clickable(self, *locator):
        " wait for element to be clickable "
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(*locator))

    def wait_for_element_presence(self, *locator):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(*locator))

    def wait_for_text_in_element(self, *locator, actual_text):
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(*locator), actual_text)

    def create_phone_number(self):
        phn_num = ['(870) 735-3842', '+1 870-735-3842', '+1 512-900-2778', '512-900-2778', '407.650.1811', '407.374.3333',
                   '+1 407-650-8022', '+1 702-558-5127', '(702) 558-5127', '+1 732-491-2240', '+1 908-859-6292', '(201) 333-8844', '+1 304-881-4400', '+1 270-781-4770', '502-477-5448']
        return random.choice(phn_num)

    def get_chat(self):
        return self.driver.find_element(*SignInLocators.chat)

    def close_chat_popup(self):
        self.driver.switch_to.frame(self.get_chat())
        time.sleep(1.5)
        self.driver.find_element(*SignInLocators.close_chat1).click()
        self.driver.switch_to.default_content()
        time.sleep(2)

    def close_chat_popup_while_button_click(self, button):
        try:
            button.click()
        except:
            self.close_chat_popup()
            button.click()
            '''
            try:
                button.click()
            except:
                self.close_chat_popup()
                button.click()
            '''

    def equality_assert(self, first_arg, second_arg):
        """
            assertion for equality of two arguments
        """
        assert first_arg == second_arg

    def subset_assert(self, first_arg, second_arg):
        """
            assertion for subset of object
        """
        assert first_arg in second_arg

    def clear_put_input_value(self, locator, input_value):
        """
            clears and puts input in input box
        """
        time.sleep(1)
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(input_value)

    def clear_input(self, locator):
        """
            clears input box
        """
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    def put_input(self, locator, value):
        """
            puts input in input box
        """
        time.sleep(1)
        element = self.driver.find_element(*locator)
        element.send_keys(value) 
