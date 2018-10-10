import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

import sys
sys.path.append('../test_pages')
import time


from Buyer_Pages.pageSignin import MainSigninPage


class kirvBuyerTest(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def test_buyer(self):
        signin_page = MainSigninPage(self.driver)
        try:
            signin_page.check_signin_img() == True
            print("Success: Kirv image found.")
        except:
            print("No result for kirv image.")

        try:
            signin_page.check_signin_title() == True
            print("Success: sign in title found.")
        except:
            print("No result found for kirv title.")

        signin_page.fill_fields()


if __name__ == "__main__":
    unittest.main()
