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
import time
from selenium.webdriver.common.keys import Keys

#contactInfo = {'company_name': 'Brown Inc', 'contact_name': 'John Dominguez', 'phone_no': '+12345678900'}
#companyInfo = {'reseller_id': '4378', 'street_address': '359 Lisa Tunnel', 'city': 'North Gabrielburgh', 'state': 'Alabama', 'post_code': '53015', 'domain': 'ryan.com', 'email': 'fphillips@garcia.com', 'phone_no': '12345678901', 'other_phone_no': '12345678902'}
#locationInfo = {'name1': 'Jennifer Mountains', 'email1': 'sarah98@gmail.com', 'phone_no1': '12345678904', 'name2': 'Preston Ridges', 'street2': '46347 Garcia Land', 'city2': 'Tylerburgh', 'state2': 'Alabama', 'street1': '8726 Debra Mission', 'city1': 'South Jeffreyport', 'state1': 'Alabama', 'post_code1': '87863', 'other_phone_no1': '12345678905', 'post_code2': '26124', 'email2': 'jamesmayer@mcgee.org', 'phone_no2': '12345678906'}


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


    def check_pending_customer_company_detail(self):
        """
            checks first customer detail information
        """
        #try:
        self.get_first_view_tab().click()
        print ("^^^^^^^^^")
        self.driver.find_element(*SupplierPageLocators.edit_company_information).click()
        assert self.driver.find_element(*SupplierPageLocators.company_name_input).get_attribute('value') == contactInfo['company_name']
        assert self.driver.find_element(*SupplierPageLocators.company_address_input).get_attribute('value') == companyInfo['street_address']
        assert self.driver.find_element(*SupplierPageLocators.company_city_input).get_attribute('value') == companyInfo['city']
        assert self.driver.find_element(*SupplierPageLocators.company_state_input).get_attribute('value') == companyInfo['state']
        assert self.driver.find_element(*SupplierPageLocators.company_post_code_input).get_attribute('value') == companyInfo['post_code']
        assert self.driver.find_element(*SupplierPageLocators.company_reseller_id_input).get_attribute('value') == companyInfo['reseller_id']
        print (self.driver.find_element(*SupplierPageLocators.company_account_no_input).get_attribute('value'))
        assert self.driver.find_element(*SupplierPageLocators.company_phone_input).get_attribute('value') == companyInfo['phone_no']
        assert self.driver.find_element(*SupplierPageLocators.company_other_phone_input).get_attribute('value') == companyInfo['other_phone_no']
        assert self.driver.find_element(*SupplierPageLocators.company_email_input).get_attribute('value') == companyInfo['email']
        assert self.driver.find_element(*SupplierPageLocators.company_website_input).get_attribute('value') == companyInfo['domain']
        self.driver.find_element(*SupplierPageLocators.company_cancel_button).click()
        #self.driver.find_element(*SupplierPageLocators.company_save_button).click()

        self.driver.find_element(*SupplierPageLocators.edit_contact_information).click()
        assert self.driver.find_element(*SupplierPageLocators.contact_name_input).get_attribute('value') == contactInfo['contact_name']
        assert self.driver.find_element(*SupplierPageLocators.contact_phone_input).get_attribute('value') == contactInfo['phone_no']
        assert self.driver.find_element(*SupplierPageLocators.contact_email_input).get_attribute('value') == signupLogin['email']
        #self.driver.find_element(*SupplierPageLocators.contact_cancel_button).click()
        self.driver.find_element(*SupplierPageLocators.contact_save_button).click()

        self.driver.find_element(*SupplierPageLocators.edit_location_information).click()
        body = self.driver.find_element(*SupplierPageLocators.body)
        body.send_keys(Keys.PAGE_DOWN)
        assert self.driver.find_element(*SupplierPageLocators.location_name1_input).get_attribute('value') == locationInfo['name1']
        assert self.driver.find_element(*SupplierPageLocators.location_address1_input).get_attribute('value') == locationInfo['street1']
        assert self.driver.find_element(*SupplierPageLocators.location_city1_input).get_attribute('value') == locationInfo['city1']
        assert self.driver.find_element(*SupplierPageLocators.location_state1_input).get_attribute('value') == locationInfo['state1']
        assert self.driver.find_element(*SupplierPageLocators.location_post_code1_input).get_attribute('value') == locationInfo['post_code1']
        assert self.driver.find_element(*SupplierPageLocators.location_email1_input).get_attribute('value') == locationInfo['email1']
        assert self.driver.find_element(*SupplierPageLocators.location_phone1_input).get_attribute('value') == locationInfo['phone_no1']
        assert self.driver.find_element(*SupplierPageLocators.location_name2_input).get_attribute('value') == locationInfo['name2']
        assert self.driver.find_element(*SupplierPageLocators.location_address2_input).get_attribute('value') == locationInfo['street2']
        assert self.driver.find_element(*SupplierPageLocators.location_city2_input).get_attribute('value') == locationInfo['city2']
        assert self.driver.find_element(*SupplierPageLocators.location_state2_input).get_attribute('value') == locationInfo['state2']
        assert self.driver.find_element(*SupplierPageLocators.location_post_code2_input).get_attribute('value') == locationInfo['post_code2']
        assert self.driver.find_element(*SupplierPageLocators.location_email2_input).get_attribute('value') == locationInfo['email2']
        assert self.driver.find_element(*SupplierPageLocators.location_phone2_input).get_attribute('value') == locationInfo['phone_no2']
        #self.driver.find_element(*SupplierPageLocators.location_cancel_button).click()
        self.driver.find_element(*SupplierPageLocators.location_save_button).click()

        self.driver.find_element(*SupplierPageLocators.edit_ship_information).click()
        body.send_keys(Keys.PAGE_DOWN)
        assert self.driver.find_element(*SupplierPageLocators.ship_name1_input).get_attribute('value') == locationInfo['name1']
        assert self.driver.find_element(*SupplierPageLocators.ship_address1_input).get_attribute('value') == locationInfo['street1']
        assert self.driver.find_element(*SupplierPageLocators.ship_city1_input).get_attribute('value') == locationInfo['city1']
        assert self.driver.find_element(*SupplierPageLocators.ship_state1_input).get_attribute('value') == locationInfo['state1']
        assert self.driver.find_element(*SupplierPageLocators.ship_post_code1_input).get_attribute('value') == locationInfo['post_code1']
        assert self.driver.find_element(*SupplierPageLocators.ship_email1_input).get_attribute('value') == locationInfo['email1']
        assert self.driver.find_element(*SupplierPageLocators.ship_phone1_input).get_attribute('value') == locationInfo['phone_no1']
        assert self.driver.find_element(*SupplierPageLocators.ship_start_time1_input).get_attribute('value') == locationInfo['start_time1']
        assert self.driver.find_element(*SupplierPageLocators.ship_end_time1_input).get_attribute('value') == locationInfo['end_time1']
        assert self.driver.find_element(*SupplierPageLocators.ship_name2_input).get_attribute('value') == shippingInfo['name2']
        assert self.driver.find_element(*SupplierPageLocators.ship_address2_input).get_attribute('value') == shippingInfo['street2']
        assert self.driver.find_element(*SupplierPageLocators.ship_city2_input).get_attribute('value') == shippingInfo['city2']
        assert self.driver.find_element(*SupplierPageLocators.ship_state2_input).get_attribute('value') == shippingInfo['state2']
        assert self.driver.find_element(*SupplierPageLocators.ship_post_code2_input).get_attribute('value') == shippingInfo['post_code2']
        assert self.driver.find_element(*SupplierPageLocators.ship_email2_input).get_attribute('value') == shippingInfo['email2']
        assert self.driver.find_element(*SupplierPageLocators.ship_phone2_input).get_attribute('value') == shippingInfo['phone_no2']
        assert self.driver.find_element(*SupplierPageLocators.ship_start_time2_input).get_attribute('value') == shippingInfo['start_time2']
        assert self.driver.find_element(*SupplierPageLocators.ship_end_time2_input).get_attribute('value') == shippingInfo['end_time2']
        #self.driver.find_element(*SupplierPageLocators.ship_cancel_button).click()
        self.driver.find_element(*SupplierPageLocators.ship_save_button).click()

        self.driver.find_element(*SupplierPageLocators.edit_categories_information).click()
        assert self.driver.find_element(*SupplierPageLocators.categories_microwave).get_attribute('value') == categoriesInfo['microwave']
        assert self.driver.find_element(*SupplierPageLocators.categories_oven).get_attribute('value') == categoriesInfo['oven']
        assert self.driver.find_element(*SupplierPageLocators.categories_hood).get_attribute('value') == categoriesInfo['hood']
        assert self.driver.find_element(*SupplierPageLocators.categories_stove).get_attribute('value') == categoriesInfo['stove']
        assert self.driver.find_element(*SupplierPageLocators.categories_dishwasher).get_attribute('value') == categoriesInfo['dishwasher']
        body.send_keys(Keys.PAGE_DOWN)
        assert self.driver.find_element(*SupplierPageLocators.categories_washer).get_attribute('value') == categoriesInfo['laundry_washer']
        assert self.driver.find_element(*SupplierPageLocators.categories_pedestal).get_attribute('value') == categoriesInfo['laundry_pedestal']
        assert self.driver.find_element(*SupplierPageLocators.categories_combo).get_attribute('value') == categoriesInfo['laundry_combo']
        assert self.driver.find_element(*SupplierPageLocators.categories_dryer).get_attribute('value') == categoriesInfo['laundry_dryer']
        assert self.driver.find_element(*SupplierPageLocators.categories_garbage_cabinet).get_attribute('value') == categoriesInfo['garbage_cabinet']
        assert self.driver.find_element(*SupplierPageLocators.categories_compactor).get_attribute('value') == categoriesInfo['compactor']
        assert self.driver.find_element(*SupplierPageLocators.categories_icemaker).get_attribute('value') == categoriesInfo['icemaer']
        assert self.driver.find_element(*SupplierPageLocators.categories_freezer).get_attribute('value') == categoriesInfo['freezer']
        assert self.driver.find_element(*SupplierPageLocators.categories_refrigerator).get_attribute('value') == categoriesInfo['refrigerator']
        #self.driver.find_element(*SupplierPageLocators.categories_cancel_button).click()
        self.driver.find_element(*SupplierPageLocators.categories_save_button).click()

        self.driver.find_element(*SupplierPageLocators.edit_volume_information).click()
        assert self.driver.find_element(*SupplierPageLocators.volume_q1_quarter_trucks).get_attribute('value') == volumeInfo['q1_quarterTruck']
        assert self.driver.find_element(*SupplierPageLocators.volume_q1_half_trucks).get_attribute('value') == volumeInfo['q1_halfTruck']
        assert self.driver.find_element(*SupplierPageLocators.volume_q1_full_trucks).get_attribute('value') == volumeInfo['q1_fullTruck']
        assert self.driver.find_element(*SupplierPageLocators.volume_q2_quarter_trucks).get_attribute('value') == volumeInfo['q2_quarterTruck']
        assert self.driver.find_element(*SupplierPageLocators.volume_q2_half_trucks).get_attribute('value') == volumeInfo['q2_halfTruck']
        assert self.driver.find_element(*SupplierPageLocators.volume_q2_full_trucks).get_attribute('value') == volumeInfo['q2_fullTruck']
        assert self.driver.find_element(*SupplierPageLocators.volume_q3_quarter_trucks).get_attribute('value') == volumeInfo['q2_quarterTruck']
        assert self.driver.find_element(*SupplierPageLocators.volume_q3_half_trucks).get_attribute('value') == volumeInfo['q2_halfTruck']
        assert self.driver.find_element(*SupplierPageLocators.volume_q3_full_trucks).get_attribute('value') == volumeInfo['q2_fullTruck']
        assert self.driver.find_element(*SupplierPageLocators.volume_q4_quarter_trucks).get_attribute('value') == volumeInfo['q2_quarterTruck']
        assert self.driver.find_element(*SupplierPageLocators.volume_q4_half_trucks).get_attribute('value') == volumeInfo['q2_halfTruck']
        assert self.driver.find_element(*SupplierPageLocators.volume_q4_full_trucks).get_attribute('value') == volumeInfo['q2_fullTruck']
        #self.driver.find_element(*SupplierPageLocators.volume_cancel_button).click()
        self.driver.find_element(*SupplierPageLocators.volume_save_button).click()

        
        #except:
        #    print ("AssertionError --------> Customer details not found")
