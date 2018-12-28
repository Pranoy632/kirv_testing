import yaml
from pathlib import Path
from pages.basepage import *
from locators.buyer_locators.landing_page_locators import LoginLocators
from locators.buyer_locators.homepage_locators import HomePageLocators

p = str(Path(__file__).parents[2])

with open(p + "/test_data/credentials.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


class Login(BasePage):

    def enter_credentials_existing_buyer(self):
        self.driver.find_element(*LoginLocators.email).send_keys(cfg['existing_buyer']['username'])
        self.driver.find_element(*LoginLocators.password).send_keys(cfg['existing_buyer']['password'])

    def click_sign_in_button(self):
        self.driver.find_element(*LoginLocators.sign_in).click()

    def wait_for_home_page(self):
        self.wait_for_element(HomePageLocators.search_bar)
