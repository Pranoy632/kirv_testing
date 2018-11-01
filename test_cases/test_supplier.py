import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import logging
import time

import sys
sys.path.append('../test_pages')

from Supplier_Pages.pageSignIn import SignIn
from Supplier_Pages.pageHomepage import SupplierHomepage
from Supplier_Pages.pageCustomers import SupplierCustomers
from page_buyer_supplier_signin import MainSigninPage
#from test_signup import kirvSignupTest
from SignUp_Pages.pageSignUpContact import contactInfo
from SignUp_Pages.pageSignUpCompanyInfo import companyInfo
from SignUp_Pages.pageSignUpLocation import locationInfo


class Supplier_Test(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def check_home_page(self):
        """
            Checks home page contents.
        """
        supplier_homepage = SupplierHomepage(self.driver)
        try:
            assert supplier_homepage.get_supplier_kirv_logo().is_displayed()
            assert supplier_homepage.check_products_link().text == 'Products'
            assert supplier_homepage.check_customers_link().text == 'Customers'
            assert supplier_homepage.check_orders_link().text == 'Orders'
            assert supplier_homepage.get_search_input_box().is_displayed()
            assert supplier_homepage.get_search_button().is_displayed()
            assert supplier_homepage.get_logout_button().is_displayed()
            assert supplier_homepage.check_customers_title().text == 'Customers'
            assert supplier_homepage.get_all_customer_tab().is_displayed()
            assert supplier_homepage.get_pending_tab().is_displayed()
            assert supplier_homepage.get_active_tab().is_displayed()
            assert supplier_homepage.get_inactive_tab().is_displayed()
            self.check_tab_is_active("Customers")
            print ("Success -> check_home_page")
        except:
            print ("AssertionError --------> Element not found on Home page of supplier")


    def check_table_header(self, status_tab_name):
        """
            Checks header line of table.
        """
        supplier_homepage = SupplierHomepage(self.driver)
        try:
            if supplier_homepage.get_total_table_records() != 0:
                assert supplier_homepage.check_customer_name_table_header().is_displayed()
                assert supplier_homepage.check_state_table_header().is_displayed()
                assert supplier_homepage.check_no_of_locations_table_header().is_displayed()
                assert supplier_homepage.check_main_contact_table_header().is_displayed()
                assert supplier_homepage.check_phone_number_table_header().is_displayed()
                assert supplier_homepage.check_account_status_table_header().is_displayed()
            else:
                assert supplier_homepage.get_search_message().is_displayed()
            print ("Success -> check table header of %s tab"%(status_tab_name))
        except:
            print ("AssertionError --------> %s tab table header error"%(status_tab_name))


    def check_tab_is_active(self, status_tab_name):
        """
            Checks status tab is active or not
        """
        supplier_homepage = SupplierHomepage(self.driver)
        try:
            assert supplier_homepage.is_tab_active(status_tab_name) == 'active'
            print ("Success -> check tab is active for %s tab"%(status_tab_name))
        except:
            print ("AssertionError --------> %s tab is_active error"%(status_tab_name))


    def check_customers_count(self, status_tab_name):
        """
            Checks total customers with count of records after applying filter on the account status
        """
        supplier_homepage = SupplierHomepage(self.driver)
        try:
            if supplier_homepage.get_total_table_records() != 0:
                assert supplier_homepage.get_required_status_count(status_tab_name) == supplier_homepage.get_single_page_records_count()
            else:
                assert supplier_homepage.get_search_message().is_displayed()
            print ("Success -> Checks total customer count of %s tab"%(status_tab_name))
        except:
            print ("AssertionError --------> %s tab total count mismatch"%(status_tab_name))


    def check_pagination(self, status_tab_name):               ##### Pagination still in progress -> check if no of pages matches with page line below #####
        """
            Checks if pagination tab works or not
        """
        supplier_homepage = SupplierHomepage(self.driver)
        try:
            total_table_records = supplier_homepage.get_total_table_records()
            pages=0 if total_table_records==0 else int(total_table_records/50) if total_table_records%50==0 else int((total_table_records/50)+1)
            print (pages)
            if pages == 0:
                assert supplier_homepage.get_search_message().is_displayed()
            if pages > 1:
                supplier_homepage.scroll_down_window()
                assert supplier_homepage.get_total_pages() == pages
                self.check_tab_is_active("1")
                supplier_homepage.click_button(supplier_homepage.get_second_pagination_tab())
                self.check_tab_is_active(status_tab_name)
                supplier_homepage.scroll_down_window()
                self.check_tab_is_active("2")
                supplier_homepage.scroll_up_window()
            print ("Success -> check pagination of %s tab"%(status_tab_name))
        except:
            supplier_homepage.scroll_up_window()
            print ("AssertionError --------> %s pagination error"%(status_tab_name))


    def check_search_functionallity(self, status_tab_name):     #### Search functionallity have some things to implement by dev (like after searching empty string it should remain on same page) ####
        """
            Checks search customers without any text, with valid text and with invalid text
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
            print ("Success -> check search functionallity of %s tab"%(status_tab_name))
        except:
            print ("AssertionError --------> %s tab search customers error"%(status_tab_name))


    def goto_homepage(self):
        """
            Clicks Kirv Logo and checks the homepage
        """
        try:
            supplier_homepage = SupplierHomepage(self.driver)
            supplier_homepage.click_button(supplier_homepage.get_supplier_kirv_logo())
            self.check_home_page()
            print ("Success -> goto homepage")
        except:
            print ("AssertionError --------> Failed to Goto Homepage")

    '''    
    def check_pending_customer_first_record(self):
        """
            checks first customer partial information
        """
        supplier_customer = SupplierCustomers(self.driver)
        try:
            assert supplier_customer.get_first_customer_name().text == contactInfo['company_name']
            assert supplier_customer.get_first_state().text == companyInfo['state']
            total_locations = 0 if not bool(locationInfo) else 2 if 'name1' in locationInfo and 'name2' in locationInfo else 1
            assert supplier_customer.get_first_no_of_location().text == str(total_locations)
            assert supplier_customer.get_first_main_contact().text == contactInfo['contact_name']
            assert supplier_customer.get_first_phone_number().text == contactInfo['phone_no']
            assert supplier_customer.get_first_account_status().text == 'Pending'
        except:
            print ("AssertionError --------> Customer details not found")
    '''

    def check_status_tab(self, status_tab_name):
        """
            Checks given status tab of page, filters respective account status and compares total count with it, Checks Search functionallity
        """
        supplier_homepage = SupplierHomepage(self.driver)
        supplier_homepage.goto_required_status_tab(status_tab_name)
        self.check_table_header(status_tab_name)
        self.check_tab_is_active(status_tab_name)
        self.check_customers_count(status_tab_name)
        self.check_pagination(status_tab_name)
        #self.check_search_functionallity(status_tab_name)         # Search Functionallity yet to complete by dev
        self.goto_homepage()


    def check_all_status_tab(self, status_tab):
        """
            Checks all status tab of page
        """
        for status_tab_name in status_tab:
            self.check_status_tab(status_tab_name)


    def logout(self):
        """
            Logouts from current user
        """
        try:
            supplier_homepage = SupplierHomepage(self.driver)
            supplier_homepage.click_button(supplier_homepage.get_logout_button())
            supplier_homepage.get_signin_button().is_displayed()
            print ("Success -> logout")
        except:
            print ("AssertionError --------> Failed to logout")


    def test_supplier(self):
        sign_in = SignIn(self.driver)
        sign_in.sign_in_credentials()
        
        #signupTest = kirvSignupTest()
        #signupTest.test_signUp()
        
        #username = 'w@kirv.co'
        #password = 'qwerty123'
        #signin_page = MainSigninPage(self.driver)
        #signin_page.fill_fields(username, password)

        supplier_homepage = SupplierHomepage(self.driver)
        supplier_customer = SupplierCustomers(self.driver)
        #self.check_home_page()

        status_tab = ["all_customers", "Pending", "Active", "Inactive"]
        #self.check_all_status_tab(status_tab)

        #supplier_customer.check_pending_customer_first_record()
        supplier_customer.get_first_view_tab().click()
        supplier_customer.check_edited_pending_customer_company_detail()
        #supplier_customer.check_edited_pending_customer_contact_detail()
        #supplier_customer.check_pending_customer_company_detail()

        #self.logout()
        #print (contactInfo)
        #print (companyInfo)
        #unittest.main(module=test_signup).signUpJourney()
        #self.driver.close()


if __name__ == "__main__":
    unittest.main()
