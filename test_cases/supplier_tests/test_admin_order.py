import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
#from pages.landing_page.page_buyer_supplier_signin import MainSigninPage
#from pages.Supplier_Pages.pageHomepage import SupplierHomepage
from pages.Supplier_Pages.pageAdminOrder import HomePage
from pages.Supplier_Pages.servicePage import Services
import time


class Admin_Order_Test(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        #options.add_argument("--headless")
        #options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://kirv-accounts-staging.herokuapp.com/login/")

    def check_name(self):
        print("ganpati bappa")
        return



    def test_admin_order(self):
        username = 'w@kirv.co'
        password = 'qwerty123'
        B2B_Service = HomePage(self.driver)
        #loginCredintials.login(username,password)
        Service = Services(self.driver)
        Service.login(username,password)
        assert(Service.click_on_service()==1)
        assert(B2B_Service.check_admin_home_page()==1)
        B2B_Service.check_for_order_homepage()


if __name__ == "__main__":
    unittest.main()
