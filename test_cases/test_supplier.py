import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import logging

import sys
sys.path.append('../test_pages')

from Supplier_Pages.pageSignIn import SignIn
from Supplier_Pages.pageHomepage import SupplierHomepage

class Supplier_Test(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def check_table_header(self):
        supplier_homepage = SupplierHomepage(self.driver)
        assert supplier_homepage.check_customer_name_table_header()
        assert supplier_homepage.check_state_table_header()
        assert supplier_homepage.check_no_of_locations_table_header()
        assert supplier_homepage.check_main_contact_table_header()
        assert supplier_homepage.check_phone_number_table_header()
        assert supplier_homepage.check_account_status_table_header()

    def test_supplier(self):
        sign_in = SignIn(self.driver)
        sign_in.sign_in_credentials()

        supplier_homepage = SupplierHomepage(self.driver)
        # Following try block checks homepage of supplier
        try:
            assert supplier_homepage.check_supplier_kirv_logo()
            assert supplier_homepage.check_products_link() == 'Products'
            assert supplier_homepage.check_customers_link() == 'Customers'
            assert supplier_homepage.check_search_input_box()
            assert supplier_homepage.check_search_button()
            assert supplier_homepage.check_logout_button()
            assert supplier_homepage.check_customers_title() == 'Customers'
            assert supplier_homepage.get_all_customer_tab().is_displayed()
            assert supplier_homepage.get_pending_tab().is_displayed()
            assert supplier_homepage.get_active_tab().is_displayed()
            assert supplier_homepage.get_inactive_tab().is_displayed()
        except:
            print ("AssertionError --------> Element not found on Contract page")

        # Following try block checks All Customers tab
        try:
            supplier_homepage.click_all_customers_tab()
            self.check_table_header()
        except:
            print ("AssertionError --------> Element not found on All Customers tab")
        
if __name__ == "__main__":
    unittest.main()
