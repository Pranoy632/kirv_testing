import sys
sys.path.append('../test_locators')

from Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators
from Supplier_Locators.locatorSupplier import SupplierPageLocators
import time

class SupplierHomepage(BasePage):

    def get_web_element(self,locator):
        return self.driver.find_element(locator)

    def check_supplier_kirv_logo(self):
        kirv_logo = self.driver.find_element(*SupplierPageLocators.kirv_logo)
        return kirv_logo.is_displayed()
        # return self.get_web_element(*SupplierPageLocators.kirv_logo).is_displayed()

    def check_products_link(self):
        # self.wait_for_element(*SupplierPageLocators.products)
        time.sleep(5)
        products_link = self.driver.find_element(*SupplierPageLocators.products_link)
        return products_link.text

    def check_customers_link(self):
        # time.sleep(2)
        customers_link = self.driver.find_element(*SupplierPageLocators.customers_link)
        return customers_link.text

    def check_search_input_box(self):
        customer_search_input_box = self.driver.find_element(*SupplierPageLocators.input_search_customers)
        return customer_search_input_box.is_displayed()

    def check_search_button(self):
        search_button = self.driver.find_element(*SupplierPageLocators.search_button)
        return search_button.is_displayed()

    def check_logout_button(self):
        logout_button = self.driver.find_element(*SupplierPageLocators.logout_button)
        return logout_button.is_displayed()

    def check_customers_title(self):
        customers_title = self.driver.find_element(*SupplierPageLocators.customers_title)
        return customers_title.text

    def get_all_customer_tab(self):
        all_customer_link = self.driver.find_element(*SupplierPageLocators.all_customer_link)
        return all_customer_link

    def get_pending_tab(self):
        pending_link = self.driver.find_element(*SupplierPageLocators.pending_link)
        return pending_link
        # return pending_link.get_attribute("class")

    def get_active_tab(self):
        active_link = self.driver.find_element(*SupplierPageLocators.active_link)
        return active_link

    def get_inactive_tab(self):
        inactive_link = self.driver.find_element(*SupplierPageLocators.inactive_link)
        return inactive_link

    def check_customer_name_table_header(self):
        customer_name_header = self.driver.find_element(*SupplierPageLocators.customer_name)
        return customer_name_header.is_displayed()

    def check_state_table_header(self):
        state_header = self.driver.find_element(*SupplierPageLocators.state)
        return state_header.is_displayed()

    def check_no_of_locations_table_header(self):
        no_of_locations_header = self.driver.find_element(*SupplierPageLocators.no_of_locations)
        return no_of_locations_header.is_displayed()

    def check_main_contact_table_header(self):
        main_contact_header = self.driver.find_element(*SupplierPageLocators.main_contact)
        return main_contact_header.is_displayed()

    def check_phone_number_table_header(self):
        phone_number_header = self.driver.find_element(*SupplierPageLocators.phone_number)
        return phone_number_header.is_displayed()

    def check_account_status_table_header(self):
        account_status_header = self.driver.find_element(*SupplierPageLocators.account_status)
        return account_status_header.is_displayed()

    def click_all_customers_tab(self):
        self.get_all_customer_tab().click()
        time.sleep(5)

    def click_pending_tab(self):
        self.get_pending_tab().click()
        time.sleep(5)

    def click_active_tab(self):
        self.get_active_tab().click()
        time.sleep(5)

    def click_inactive_tab(self):
        self.get_inactive_tab().click()
        time.sleep(5)
