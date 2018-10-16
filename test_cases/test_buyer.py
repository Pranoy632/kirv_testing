import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

import sys
sys.path.append('../test_pages')
import time


from page_buyer_supplier_signin import MainSigninPage
from Buyer_Pages.page_header import HeaderPage
from Buyer_Pages.page_home import HomePage


class kirvBuyerTest(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def test_buyer(self):
        user = 'amztest18+20181010142126@gmail.com'
        pwd = 'amazatic'

        # Sign In

        signin_page = MainSigninPage(self.driver)
        signin_page.fill_fields(user, pwd)

        # header

        header = HeaderPage(self.driver)
        header.check_img_labels()

        # home-page

        home = HomePage(self.driver)
        home.check_labels_prodlist()


if __name__ == "__main__":
    unittest.main()
