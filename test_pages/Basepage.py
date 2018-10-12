from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Factory

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
