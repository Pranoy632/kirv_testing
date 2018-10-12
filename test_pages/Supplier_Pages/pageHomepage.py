import sys
sys.path.append('../test_locators')

from Basepage import BasePage
from SignUp_Locators.locatorSignup import SigninPageLocators
from Supplier_Locators.locatorSupplier import SupplierPageLocators

class SupplierHomepage(BasePage):

    def click_button(self, get_button):
        get_button.click()

    def get_supplier_kirv_logo(self):
        return self.driver.find_element(*SupplierPageLocators.kirv_logo)

    def check_products_link(self):
        return self.driver.find_element(*SupplierPageLocators.products_link)

    def check_customers_link(self):
        return self.driver.find_element(*SupplierPageLocators.customers_link)

    def check_orders_link(self):
        return self.driver.find_element(*SupplierPageLocators.orders_link)

    def get_search_input_box(self):
        return self.driver.find_element(*SupplierPageLocators.input_search_customers)

    def get_search_button(self):
        return self.driver.find_element(*SupplierPageLocators.search_button)

    def get_logout_button(self):
        return self.driver.find_element(*SupplierPageLocators.logout_button)

    def check_customers_title(self):
        return self.driver.find_element(*SupplierPageLocators.customers_title)

    def get_all_customer_tab(self):
        return self.driver.find_element(*SupplierPageLocators.all_customer_link)

    def get_pending_tab(self):
        return self.driver.find_element(*SupplierPageLocators.pending_link)

    def get_active_tab(self):
        return self.driver.find_element(*SupplierPageLocators.active_link)

    def get_inactive_tab(self):
        return self.driver.find_element(*SupplierPageLocators.inactive_link)

    def check_customer_name_table_header(self):
        return self.driver.find_element(*SupplierPageLocators.customer_name)

    def check_state_table_header(self):
        return self.driver.find_element(*SupplierPageLocators.state)

    def check_no_of_locations_table_header(self):
        return self.driver.find_element(*SupplierPageLocators.no_of_locations)

    def check_main_contact_table_header(self):
        return self.driver.find_element(*SupplierPageLocators.main_contact)

    def check_phone_number_table_header(self):
        return self.driver.find_element(*SupplierPageLocators.phone_number)

    def check_account_status_table_header(self):
        return self.driver.find_element(*SupplierPageLocators.account_status)

    def goto_required_status_tab(self, status_tab_name):
        required_status_tab = {
                'all_customers': self.get_all_customer_tab,
                'Pending': self.get_pending_tab,
                'Active': self.get_active_tab,
                'Inactive': self.get_inactive_tab
        }
        required_status_tab[status_tab_name]().click()
        
    def get_row_values(self):
        return self.driver.find_elements(*SupplierPageLocators.table_rows)

    def get_required_status_count(self, status_name):
        status_list = ['Pending', 'Active', 'Inactive']
        table_rows = self.get_row_values()
        if status_name != 'all_customers':
            return ((list(filter (lambda value: value == status_name ,[row.text.rsplit(' ',2)[1] for row in table_rows][1:]))).count(status_name))
        else:
            return len(list(filter (lambda value: value in status_list,[row.text.rsplit(' ',2)[1] for row in table_rows][1:])))

    def get_single_page_records_count(self):
        total_record_text = self.driver.find_element(*SupplierPageLocators.total_table_records).text
        return int(total_record_text.split()[0])

    def get_total_table_records(self):
        total_record_text = self.driver.find_element(*SupplierPageLocators.total_table_records).text
        return int(total_record_text.split()[2])

    def is_tab_active(self, status_tab_name):
        required_status_tab = {
                'Customers': self.check_customers_link,
                'all_customers': self.get_all_customer_tab,
                'Pending': self.get_pending_tab,
                'Active': self.get_active_tab,
                'Inactive': self.get_inactive_tab,
                '1': self.get_first_pagination_tab,
                '2': self.get_second_pagination_tab
        }
        tab_class = required_status_tab[status_tab_name]().get_attribute("class")
        return "active" if "active" in tab_class.split() else None

    def get_first_table_record(self):
        first_record = self.get_row_values()[1].text
        return first_record.split(' ', 1)[0]

    def send_keys_to_search(self):
        self.get_search_input_box().send_keys(self.get_first_table_record())

    def search_record(self):
        self.send_keys_to_search()
        self.click_button(self.get_search_button())

    def clear_search_text(self):
        self.get_search_input_box().clear()

    def search_invalid_record(self):
        self.get_search_input_box().send_keys("[]")
        self.click_button(self.get_search_button())

    def get_search_message(self):
        return self.driver.find_element(*SupplierPageLocators.search_message)

    def get_first_pagination_tab(self):
        return self.driver.find_element(*SupplierPageLocators.page_number1)
        
    def get_second_pagination_tab(self):
        return self.driver.find_element(*SupplierPageLocators.page_number2)

    def scroll_down_window(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up_window(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

    def get_signin_button(self):
        return self.driver.find_element(*SupplierPageLocators.signin)

'''
    def get_pagination(self):
        a= self.driver.find_elements(*SupplierPageLocators.page_number1)
        print (len(a))
        for i in a:
            #print (i.find_element(*SupplierPageLocators.page_number1).get_attribute("class"))
            #print (i.find_element(*SupplierPageLocators.page_number1).text)
            print (i.get_attribute("class"))
'''
