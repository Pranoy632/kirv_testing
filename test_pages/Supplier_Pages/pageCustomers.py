import sys
sys.path.append('../test_locators')

from Basepage import BasePage
from Supplier_Locators.locatorSupplier import SupplierPageLocators

from SignUp_Pages.pageSignUpLogin import signupLogin
from SignUp_Pages.pageSignUpContact import contactInfo
from SignUp_Pages.pageSignUpCompanyInfo import companyInfo
from SignUp_Pages.pageSignUpLocation import locationInfo
from SignUp_Pages.pageSignUpShip import shippingInfo
from SignUp_Pages.pageSignUpCategories import categoriesInfo
from SignUp_Pages.pageSignUpVolumes import volumeInfo

contactInfo = {'company_name': 'Brown Inc', 'contact_name': 'John Dominguez', 'phone_no': '+12345678900'}
companyInfo = {'reseller_id': '4378', 'street_address': '359 Lisa Tunnel', 'city': 'North Gabrielburgh', 'state': 'Alabama', 'post_code': '53015', 'domain': 'ryan.com', 'email': 'fphillips@garcia.com', 'phone_no': '12345678901', 'other_phone_no': '12345678902'}
locationInfo = {'name1': 'Jennifer Mountains', 'email1': 'sarah98@gmail.com', 'phone_no1': '12345678904', 'name2': 'Preston Ridges', 'street2': '46347 Garcia Land', 'city2': 'Tylerburgh', 'state2': 'Alabama', 'street1': '8726 Debra Mission', 'city1': 'South Jeffreyport', 'state1': 'Alabama', 'post_code1': '87863', 'other_phone_no1': '12345678905', 'post_code2': '26124', 'email2': 'jamesmayer@mcgee.org', 'phone_no2': '12345678906'}


class SupplierCustomers(BasePage):

    def get_first_customer_name(self):
        return self.driver.find_element(*SupplierPageLocators.first_record_customer_name)

    def get_first_state(self):
        return self.driver.find_element(*SupplierPageLocators.first_record_state)

    def get_first_no_of_location(self):
        return self.driver.find_element(*SupplierPageLocators.first_record_no_of_location)

    def get_first_main_contact(self):
        return self.driver.find_element(*SupplierPageLocators.first_record_main_contact)

    def get_first_phone_number(self):
        return self.driver.find_element(*SupplierPageLocators.first_record_phone_number)

    def get_first_account_status(self):
        return self.driver.find_element(*SupplierPageLocators.first_record_account_status)

    def get_first_view_tab(self):
        return self.driver.find_element(*SupplierPageLocators.view)

    def check_pending_customer_first_record(self):
        """
            checks first customer partial information
        """
        try:
            assert self.get_first_customer_name().text == contactInfo['company_name']
            assert self.get_first_state().text == companyInfo['state']
            total_locations = 0 if not bool(locationInfo) else 2 if 'name1' in locationInfo and 'name2' in locationInfo else 1
            assert self.get_first_no_of_location().text == str(total_locations)
            assert self.get_first_main_contact().text == contactInfo['contact_name']
            assert self.get_first_phone_number().text == contactInfo['phone_no']
            assert self.get_first_account_status().text == 'Pending'
            print ("Success -> Pending Customer partial first record")
        except:
            print ("AssertionError --------> Customer partial details not found")


    def check_pending_customer_first_record_detail(self):
        """
            checks first customer detail information
        """
        #try:
        self.get_first_view_tab().click()
        print ("^^^^^^^^^")
        self.driver.find_element(*SupplierPageLocators.edit_company_information).click()
        print (self.driver.find_element(*SupplierPageLocators.company_name_input).get_attribute('value'))
        #except:
        #    print ("AssertionError --------> Customer details not found")
