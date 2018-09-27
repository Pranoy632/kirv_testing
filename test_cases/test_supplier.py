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
        assert supplier_homepage.check_customer_name_table_header().is_displayed()
        assert supplier_homepage.check_state_table_header().is_displayed()
        assert supplier_homepage.check_no_of_locations_table_header().is_displayed()
        assert supplier_homepage.check_main_contact_table_header().is_displayed()
        assert supplier_homepage.check_phone_number_table_header().is_displayed()
        assert supplier_homepage.check_account_status_table_header().is_displayed()

    def check_status_tab(self, status_tab_name):
        supplier_homepage = SupplierHomepage(self.driver)
        try:
            supplier_homepage.goto_required_status_tab(status_tab_name)
            self.check_table_header()
            assert supplier_homepage.is_tab_active(status_tab_name) == 'active'
            if status_tab_name != 'all_customers':
                assert supplier_homepage.get_required_status_count(status_tab_name) == supplier_homepage.get_total_table_records()
            else:
                assert supplier_homepage.get_all_customers_status_count() == supplier_homepage.get_total_table_records()
        except:
            print ("AssertionError --------> Element not found on %s tab"%(status_tab_name))
    
    def check_all_status_tab(self, status_tab):
        for status_tab_name in status_tab:
            self.check_status_tab(status_tab_name)

    def test_supplier(self):
        sign_in = SignIn(self.driver)
        sign_in.sign_in_credentials()

        supplier_homepage = SupplierHomepage(self.driver)
        # Following try block checks homepage of supplier
        try:
            assert supplier_homepage.check_supplier_kirv_logo().is_displayed()
            assert supplier_homepage.check_products_link().text == 'Products'
            assert supplier_homepage.check_customers_link().text == 'Customers'
            assert supplier_homepage.check_search_input_box().is_displayed()
            assert supplier_homepage.check_search_button().is_displayed()
            assert supplier_homepage.check_logout_button().is_displayed()
            assert supplier_homepage.check_customers_title().text == 'Customers'
            assert supplier_homepage.get_all_customer_tab().is_displayed()
            assert supplier_homepage.get_pending_tab().is_displayed()
            assert supplier_homepage.get_active_tab().is_displayed()
            assert supplier_homepage.get_inactive_tab().is_displayed()
        except:
            print ("AssertionError --------> Element not found on Home page of supplier")

        status_tab = ["all_customers", "Pending", "Active", "Inactive"]
        self.check_all_status_tab(status_tab)

if __name__ == "__main__":
    unittest.main()
