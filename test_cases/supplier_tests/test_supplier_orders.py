import time

import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from pages.landing_page.page_buyer_supplier_signin import MainSigninPage
from pages.supplier_pages.order_page import OrderPage


class SupplierOrder(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def test_supplier_order(self):
        username = 'w@kirv.co'
        password = 'qwerty123'
        signin_page = MainSigninPage(self.driver)
        signin_page.fill_fields(username, password)

        order = OrderPage(self.driver)
        order.elements_of_order()


if __name__ == "__main__":
    unittest.main()
