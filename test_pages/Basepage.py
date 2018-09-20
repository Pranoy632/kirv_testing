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
