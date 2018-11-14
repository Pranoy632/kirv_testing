import sys
sys.path.append('../test_locators')

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Factory
from signin_buyer_supplier_locator import SignInLocators
import time

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

    def get_chat(self):
        return self.driver.find_element(*SignInLocators.chat)

    def close_chat_popup(self):
        self.driver.switch_to.frame(self.get_chat())
        self.driver.find_element(*SignInLocators.close_chat).click()
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
