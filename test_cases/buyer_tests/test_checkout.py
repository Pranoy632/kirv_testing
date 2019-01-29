import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

from pages.buyer_pages.checkout_page import Checkout
from common.login_buyer import LoginBuyer


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def test_checkout(self):
        LoginBuyer().sign_in_existing_buyer(self)
        Checkout(self.driver).get_each_category()
