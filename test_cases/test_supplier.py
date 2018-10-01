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

    def check_home_page(self):
        """
            Checks home page contents.
        """
        supplier_homepage = SupplierHomepage(self.driver)
        try:
            assert supplier_homepage.check_supplier_kirv_logo().is_displayed()
            assert supplier_homepage.check_products_link().text == 'Products'
            assert supplier_homepage.check_customers_link().text == 'Customers'
            assert supplier_homepage.get_search_input_box().is_displayed()
            assert supplier_homepage.get_search_button().is_displayed()
            assert supplier_homepage.check_logout_button().is_displayed()
            assert supplier_homepage.check_customers_title().text == 'Customers'
            assert supplier_homepage.get_all_customer_tab().is_displayed()
            assert supplier_homepage.get_pending_tab().is_displayed()
            assert supplier_homepage.get_active_tab().is_displayed()
            assert supplier_homepage.get_inactive_tab().is_displayed()
        except:
            print ("AssertionError --------> Element not found on Home page of supplier")

    def check_table_header(self):
        """
            Checks header line of table.
        """

        supplier_homepage = SupplierHomepage(self.driver)
        try:
            assert supplier_homepage.check_customer_name_table_header().is_displayed()
            assert supplier_homepage.check_state_table_header().is_displayed()
            assert supplier_homepage.check_no_of_locations_table_header().is_displayed()
            assert supplier_homepage.check_main_contact_table_header().is_displayed()
            assert supplier_homepage.check_phone_number_table_header().is_displayed()
            assert supplier_homepage.check_account_status_table_header().is_displayed()
        except:
            print ("AssertionError --------> %s tab table header error"%(status_tab_name))


    def check_tab_is_active(self, status_tab_name):
        """
            Checks status tab is active or not
        """

        supplier_homepage = SupplierHomepage(self.driver)
        try:
            assert supplier_homepage.is_tab_active(status_tab_name) == 'active'
        except:
            print ("AssertionError --------> %s tab is_active error"%(status_tab_name))

    def check_customers_count(self, status_tab_name):
        """
            Checks total customers with count of records after applying filter on the account status
        """

        supplier_homepage = SupplierHomepage(self.driver)
        try:
            if status_tab_name != 'all_customers':
                assert supplier_homepage.get_required_status_count(status_tab_name) == supplier_homepage.get_total_table_records()
            else:
                assert supplier_homepage.get_all_customers_status_count() == supplier_homepage.get_total_table_records()
        except:
            print ("AssertionError --------> %s tab total count mismatch"%(status_tab_name))

    def check_pagination(self, status_tab_name):
        supplier_homepage = SupplierHomepage(self.driver)
        try:
            if (supplier_homepage.get_total_table_records == 50):
                if (supplier_homepage.get_first_pagination_tab().is_displayed()):      # is_enabled() for buttons or clickable buttons
                    self.check_tab_is_active("1")
                    supplier_homepage.click_button(supplier_homepage.get_second_pagination_tab())
                    self.check_tab_is_active(status_tab_name)
                    self.check_tab_is_active("2")
                    self.check_customers_count()           # supplier_homepage -> get_first_pagination_tab(), get_second_pagination_tab(), add 1 and 2 to list of tab in supplier_homepage 

    def check_search_functionallity(self, status_tab_name):
        """
            Checks search customers functionllity
        """

        supplier_homepage = SupplierHomepage(self.driver)
        try:
            supplier_homepage.clear_search_text()
            supplier_homepage.click_button(supplier_homepage.get_search_button())
            self.check_tab_is_active(status_tab_name)
            self.check_customers_count(status_tab_name)

            search_key = supplier_homepage.get_first_table_record()
            supplier_homepage.search_record()
            search_result = supplier_homepage.get_first_table_record()
            self.check_tab_is_active(status_tab_name)
            assert search_key == search_result

            supplier_homepage.clear_search_text()
            supplier_homepage.search_invalid_record()
            self.check_tab_is_active(status_tab_name)
            assert supplier_homepage.get_search_message().is_displayed()
        except:
            print ("AssertionError --------> %s tab search customers error"%(status_tab_name))

    def check_status_tab(self, status_tab_name):
        """
            Checks given status tab of page, filters respective account status and compares total count with it, Checks Search functionallity
        """

        supplier_homepage = SupplierHomepage(self.driver)
        supplier_homepage.goto_required_status_tab(status_tab_name)
        self.check_table_header()
        self.check_tab_is_active(status_tab_name)
        self.check_customers_count(status_tab_name)
        self.check_pagination(status_tab_name)
        #self.check_search_functionallity(status_tab_name)
    
    def check_all_status_tab(self, status_tab):
        """
            Checks all status tab of page
        """
        for status_tab_name in status_tab:
            self.check_status_tab(status_tab_name)

    def test_supplier(self):
        sign_in = SignIn(self.driver)
        sign_in.sign_in_credentials()

        supplier_homepage = SupplierHomepage(self.driver)
        self.check_home_page()

        status_tab = ["all_customers", "Pending", "Active", "Inactive"]
        self.check_all_status_tab(status_tab)

if __name__ == "__main__":
    unittest.main()
