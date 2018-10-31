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

signupLogin = {'email': 'amztest18+20181030154540@gmail.com', 'password': 'amazatic'}
contactInfo = {'company_name': 'Marquez-Gallagher', 'contact_name': 'Joshua Russell', 'phone_no': '12345678900'}
companyInfo = {'reseller_id': '2251', 'street_address': '56897 Roman Crossroad', 'city': 'Francesstad', 'state': 'Alabama', 'post_code': '24711', 'domain': 'kelley.com', 'email': 'karenschroeder@miller.net', 'phone_no': '12345678901', 'other_phone_no': '12345678902'}
locationInfo = {'name2': 'Ryan Pine', 'email2': 'lidavid@gmail.com', 'phone_no2': '12345678904', 'name1': 'David Trail', 'street1': '12286 Brandy Trail', 'city1': 'Haroldfort', 'state2': 'Alabama', 'street2': '363 Norton Mount', 'city2': 'Garretthaven', 'state1': 'Alabama', 'post_code2': '31753', 'other_phone_no2': '12345678905', 'post_code1': '42965', 'email1': 'santiagolaura@gmail.com', 'phone_no1': '12345678906'}
shippingInfo = {'start_time1': '01:00', 'end_time1': '07:00', 'name2': 'Robinson Ports', 'state2': 'Alabama', 'start_time2': '02:00', 'end_time2': '06:00', 'street2': '40544 Sabrina Roads', 'city2': 'South Johnville', 'post_code2': '47353', 'email2': 'haley01@willis-reed.info', 'phone_no2': '12345678907', 'other_phone_no2': '12345678908'}
categoriesInfo = {'microwave': 'Often', 'oven': 'All The Time', 'hood': 'All The Time', 'dishwasher': 'Often', 'laundry_washer': 'Often', 'laundry_pedestal': 'Often', 'garbage_cabinet': 'Often', 'refrigerator': 'All The Time', 'stove': 'Often', 'laundry_combo': 'Often', 'laundry_dryer': 'Often', 'compactor': 'Often', 'icemaker': 'All The Time', 'freezer': 'All The Time'}
volumeInfo = {'q1_quarterTruck': '2', 'q1_halfTruck': '3', 'q2_quarterTruck': '2', 'q1_fullTruck': '4', 'q2_halfTruck': '2', 'q2_fullTruck': '3'}


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

    def get_company_name_input(self):
        return self.driver.find_element(*SupplierPageLocators.company_name_input)

    def get_company_name_error(self):
        return self.driver.find_element(*SupplierPageLocators.company_name_error)

    def get_company_address_input(self):
        return self.driver.find_element(*SupplierPageLocators.company_address_input)

    def get_company_address_error(self):
        return self.driver.find_element(*SupplierPageLocators.company_address_error)

    def get_company_city_input(self):
        return self.driver.find_element(*SupplierPageLocators.company_city_input)

    def get_company_city_error(self):
        return self.driver.find_element(*SupplierPageLocators.company_city_error)

    def get_company_state_input(self):
        return self.driver.find_element(*SupplierPageLocators.company_state_input)

    def get_company_state_error(self):
        return self.driver.find_element(*SupplierPageLocators.company_state_error)

    def get_company_post_code_input(self):
        return self.driver.find_element(*SupplierPageLocators.company_post_code_input)

    def get_company_post_code_error(self):
        return self.driver.find_element(*SupplierPageLocators.company_post_code_error)

    def get_company_reseller_id_input(self):
        return self.driver.find_element(*SupplierPageLocators.company_reseller_id_input)

    def get_company_reseller_id_error(self):
        return self.driver.find_element(*SupplierPageLocators.company_reseller_id_error)

    def get_company_account_no_input(self):
        return self.driver.find_element(*SupplierPageLocators.company_account_no_input)

    def get_company_account_no_error(self):
        return self.driver.find_element(*SupplierPageLocators.company_account_no_error)

    def get_company_phone_input(self):
        return self.driver.find_element(*SupplierPageLocators.company_phone_input)

    def get_company_phone_error(self):
        return self.driver.find_element(*SupplierPageLocators.company_phone_error)

    def get_company_other_phone_input(self):
        return self.driver.find_element(*SupplierPageLocators.company_other_phone_input)

    def get_company_other_phone_error(self):
        return self.driver.find_element(*SupplierPageLocators.company_other_phone_error)

    def get_company_email_input(self):
        return self.driver.find_element(*SupplierPageLocators.company_email_input)

    def get_company_email_error(self):
        return self.driver.find_element(*SupplierPageLocators.company_email_error)

    def get_company_website_input(self):
        return self.driver.find_element(*SupplierPageLocators.company_website_input)

    def get_company_website_error(self):
        return self.driver.find_element(*SupplierPageLocators.company_website_error)

    def get_company_cancel_button(self):
        return self.driver.find_element(*SupplierPageLocators.company_cancel_button)

    def get_company_save_button(self):
        return self.driver.find_element(*SupplierPageLocators.company_save_button)
    
    def get_edit_company_information(self):
        return self.driver.find_element(*SupplierPageLocators.edit_company_information)

    def get_success_message(self):
        return self.driver.find_element(*SupplierPageLocators.success_popup)

    def get_error_message(self):
        return self.driver.find_element(*SupplierPageLocators.error_popup)

    def page_down(self):
        body = self.driver.find_element(*SupplierPageLocators.body)
        body.send_keys(Keys.PAGE_DOWN)

    def check_pending_customer_first_record(self):
        """
            checks first customer partial information
        """
        #try:
        #time.sleep(1)
        assert self.get_first_customer_name().text == contactInfo['company_name']
        assert self.get_first_state().text == companyInfo['state']
        total_locations = 0 if not bool(locationInfo) else 2 if 'name1' in locationInfo and 'name2' in locationInfo else 1
        assert self.get_first_no_of_location().text == str(total_locations)
        assert self.get_first_main_contact().text == contactInfo['contact_name']
        assert self.get_first_phone_number().text == contactInfo['phone_no'] if contactInfo['phone_no'][0] == '+' else '+' + contactInfo['phone_no']
        assert self.get_first_account_status().text == 'Pending'
        #    print ("Success -> Pending Customer partial first record")
        #except:
        #    print ("AssertionError --------> Customer partial details not found")


    def check_pending_customer_company_detail(self):
        """
            checks first customer detail information
        """
        #try:
        print (signupLogin)
        print (contactInfo)
        print (companyInfo)
        print (locationInfo)
        print (shippingInfo)
        print (categoriesInfo)
        print (volumeInfo)
        self.get_edit_company_information().click()
        print (self.get_company_name_input().get_attribute('value'))
        print (contactInfo['company_name'])
        assert self.get_company_name_input().get_attribute('value') == contactInfo['company_name']
        assert self.get_company_address_input().get_attribute('value') == companyInfo['street_address']
        assert self.get_company_city_input().get_attribute('value') == companyInfo['city']
        assert self.get_company_state_input().get_attribute('value').lower() == companyInfo['state'].lower()
        assert self.get_company_post_code_input().get_attribute('value') == companyInfo['post_code']
        assert self.get_company_reseller_id_input().get_attribute('value') == companyInfo['reseller_id']
        print (self.get_company_account_no_input().get_attribute('value')) # yet to decide by dev (to keep or not)
        assert self.get_company_phone_input().get_attribute('value') == companyInfo['phone_no'] if companyInfo['phone_no'][0] == '+' else '+' + companyInfo['phone_no']
        assert self.get_company_other_phone_input().get_attribute('value') == companyInfo['other_phone_no'] if companyInfo['other_phone_no'][0] == '+' else '+' + companyInfo['other_phone_no']
        assert self.get_company_email_input().get_attribute('value') == companyInfo['email']
        assert self.get_company_website_input().get_attribute('value') == companyInfo['domain']
        self.get_company_cancel_button().click()
        #self.driver.find_element(*SupplierPageLocators.company_save_button).click()

    def check_edited_pending_customer_company_detail(self):
        companyInfo_testcase_input = {
                'company_name': {'invalid': [''], 'valid': ['John'], 'input': self.get_company_name_input(), 'error': self.get_company_name_error()}, 
                'street_address': {'invalid': [''], 'valid': ['234 China Town'], 'input': self.get_company_address_input(), 'error': self.get_company_address_error()}, 
                'city': {'invalid': [''], 'valid': ['Swe'], 'input': self.get_company_city_input(), 'error': self.get_company_city_error()},
                'post_code': {'invalid': ['1234567','123sd','abcd',''], 'valid': ['32145'], 'input': self.get_company_post_code_input(), 'error': self.get_company_post_code_error()},
                #'reseller_id': {'invalid': ['abcd',''],'valid':['ab123','1233'], 'input': self.get_company_reseller_id_input(), 'error': self.get_company_reseller_id_error()},
                #'account_no': {'invalid': ['abcd'], 'valid': ['ab123','2345',''], 'input': self.get_company_account_no_input(), 'error': self.get_company_account_no_error()},
                'phone_no': {'invalid': ['12345','abcd','12345678909abe','123456789009',''], 'valid': ['12345678911'], 'input': self.get_company_phone_input(), 'error': self.get_company_phone_error()},
                'other_phone_no': {'invalid': ['12345','abcd','12345678900acs','123456789098'], 'valid': ['12312345645',''], 'input': self.get_company_other_phone_input(), 'error': self.get_company_other_phone_error()},
                'email': {'invalid': ['abc','abc@gmail','abc.com','.abc@gmail.com','abc.@gmail.com','abc@.gmail.com','abc@gmail.com.','abc ef@gmail.com',''], 'valid': ['abc@gmail.com'], 'input': self.get_company_email_input(), 'error': self.get_company_email_error()},
                'domain': {'invalid': ['abc','.com',''], 'valid': ['abc.com'], 'input': self.get_company_website_input(), 'error': self.get_company_website_error()}
            }
        
        self.get_edit_company_information().click()
        for key, value in companyInfo_testcase_input.items():
            for input_value in value['invalid']:
                value['input'].send_keys(Keys.CONTROL+'a')
                value['input'].send_keys(Keys.DELETE)
                value['input'].send_keys(input_value)
                self.get_company_save_button().click()
                time.sleep(2)
                print (self.driver.find_element(*SupplierPageLocators.error_popup).get_attribute('class'))
                if (key == 'account_no' or key == 'other_phone_no') and input_value == '':
                    pass
                else:
                    assert 'has-danger' in value['error'].get_attribute('class').split()
        self.get_company_cancel_button().click()
        #self.check_pending_customer_company_detail()

        for key, value in companyInfo_testcase_input.items():
            for input_value in value['valid']:
                self.get_edit_company_information().click()
                value['input'].send_keys(Keys.CONTROL+'a')
                value['input'].send_keys(Keys.DELETE)
                value['input'].send_keys(input_value)
                self.get_company_save_button().click()
                time.sleep(2)
                print (self.driver.find_element(*SupplierPageLocators.success_popup).get_attribute('class'))
                assert 'success' in self.get_success_message().get_attribute('class').split()
                if key == 'company_name':
                    contactInfo[key] = input_value
                else:
                    companyInfo[key] = input_value
        self.check_pending_customer_company_detail()
                

    def check_pending_customer_contact_detail(self):
        self.driver.find_element(*SupplierPageLocators.edit_contact_information).click()
        assert self.driver.find_element(*SupplierPageLocators.contact_name_input).get_attribute('value') == contactInfo['contact_name']
        assert self.driver.find_element(*SupplierPageLocators.contact_phone_input).get_attribute('value') == contactInfo['phone_no'] if contactInfo['phone_no'][0] == '+' else '+' + contactInfo['phone_no']
        assert self.driver.find_element(*SupplierPageLocators.contact_email_input).get_attribute('value') == signupLogin['email']
        #self.driver.find_element(*SupplierPageLocators.contact_cancel_button).click()
        self.driver.find_element(*SupplierPageLocators.contact_save_button).click()

    def check_pending_customer_location_detail(self):
        self.driver.find_element(*SupplierPageLocators.edit_location_information).click()
        self.page_down()
        assert self.driver.find_element(*SupplierPageLocators.location_name1_input).get_attribute('value') == locationInfo['name1']
        assert self.driver.find_element(*SupplierPageLocators.location_address1_input).get_attribute('value') == locationInfo['street1']
        assert self.driver.find_element(*SupplierPageLocators.location_city1_input).get_attribute('value') == locationInfo['city1']
        assert self.driver.find_element(*SupplierPageLocators.location_state1_input).get_attribute('value').lower() == locationInfo['state1'].lower()
        assert self.driver.find_element(*SupplierPageLocators.location_post_code1_input).get_attribute('value') == locationInfo['post_code1']
        assert self.driver.find_element(*SupplierPageLocators.location_email1_input).get_attribute('value') == locationInfo['email1']
        assert self.driver.find_element(*SupplierPageLocators.location_phone1_input).get_attribute('value') == locationInfo['phone_no1'] if locationInfo['phone_no1'][0] == '+' else '+' + locationInfo['phone_no1']
        assert self.driver.find_element(*SupplierPageLocators.location_name2_input).get_attribute('value') == locationInfo['name2']
        assert self.driver.find_element(*SupplierPageLocators.location_address2_input).get_attribute('value') == locationInfo['street2']
        assert self.driver.find_element(*SupplierPageLocators.location_city2_input).get_attribute('value') == locationInfo['city2']
        assert self.driver.find_element(*SupplierPageLocators.location_state2_input).get_attribute('value').lower() == locationInfo['state2'].lower()
        assert self.driver.find_element(*SupplierPageLocators.location_post_code2_input).get_attribute('value') == locationInfo['post_code2']
        assert self.driver.find_element(*SupplierPageLocators.location_email2_input).get_attribute('value') == locationInfo['email2']
        assert self.driver.find_element(*SupplierPageLocators.location_phone2_input).get_attribute('value') == locationInfo['phone_no2'] if locationInfo['phone_no2'][0] == '+' else '+' + locationInfo['phone_no2']
        #self.driver.find_element(*SupplierPageLocators.location_cancel_button).click()
        self.driver.find_element(*SupplierPageLocators.location_save_button).click()

    def check_pending_shipping_detail(self):
        self.driver.find_element(*SupplierPageLocators.edit_ship_information).click()
        self.page_down()
        assert self.driver.find_element(*SupplierPageLocators.ship_name1_input).get_attribute('value') == locationInfo['name1']
        assert self.driver.find_element(*SupplierPageLocators.ship_address1_input).get_attribute('value') == locationInfo['street1']
        assert self.driver.find_element(*SupplierPageLocators.ship_city1_input).get_attribute('value') == locationInfo['city1']
        assert self.driver.find_element(*SupplierPageLocators.ship_state1_input).get_attribute('value').lower() == locationInfo['state1'].lower()
        assert self.driver.find_element(*SupplierPageLocators.ship_post_code1_input).get_attribute('value') == locationInfo['post_code1']
        assert self.driver.find_element(*SupplierPageLocators.ship_email1_input).get_attribute('value') == locationInfo['email1']
        assert self.driver.find_element(*SupplierPageLocators.ship_phone1_input).get_attribute('value') == locationInfo['phone_no1'] if locationInfo['phone_no1'][0] == '+' else '+' + locationInfo['phone_no1']
        assert self.driver.find_element(*SupplierPageLocators.ship_start_time1_input).get_attribute('value') == shippingInfo['start_time1']
        assert self.driver.find_element(*SupplierPageLocators.ship_end_time1_input).get_attribute('value') == shippingInfo['end_time1']
        assert self.driver.find_element(*SupplierPageLocators.ship_name2_input).get_attribute('value') == shippingInfo['name2']
        assert self.driver.find_element(*SupplierPageLocators.ship_address2_input).get_attribute('value') == shippingInfo['street2']
        assert self.driver.find_element(*SupplierPageLocators.ship_city2_input).get_attribute('value') == shippingInfo['city2']
        assert self.driver.find_element(*SupplierPageLocators.ship_state2_input).get_attribute('value').lower() == shippingInfo['state2'].lower()
        assert self.driver.find_element(*SupplierPageLocators.ship_post_code2_input).get_attribute('value') == shippingInfo['post_code2']
        assert self.driver.find_element(*SupplierPageLocators.ship_email2_input).get_attribute('value') == shippingInfo['email2']
        assert self.driver.find_element(*SupplierPageLocators.ship_phone2_input).get_attribute('value') == shippingInfo['phone_no2'] if shippingInfo['phone_no2'][0] == '+' else '+' + shippingInfo['phone_no2']
        assert self.driver.find_element(*SupplierPageLocators.ship_start_time2_input).get_attribute('value') == shippingInfo['start_time2']
        assert self.driver.find_element(*SupplierPageLocators.ship_end_time2_input).get_attribute('value') == shippingInfo['end_time2']
        #self.driver.find_element(*SupplierPageLocators.ship_cancel_button).click()
        self.driver.find_element(*SupplierPageLocators.ship_save_button).click()

    def check_pending_customer_categories_detail(self):
        self.driver.find_element(*SupplierPageLocators.edit_categories_information).click()
        assert self.driver.find_element(*SupplierPageLocators.categories_microwave).get_attribute('value') == categoriesInfo['microwave']
        assert self.driver.find_element(*SupplierPageLocators.categories_oven).get_attribute('value') == categoriesInfo['oven']
        assert self.driver.find_element(*SupplierPageLocators.categories_hood).get_attribute('value') == categoriesInfo['hood']
        assert self.driver.find_element(*SupplierPageLocators.categories_stove).get_attribute('value') == categoriesInfo['stove']
        assert self.driver.find_element(*SupplierPageLocators.categories_dishwasher).get_attribute('value') == categoriesInfo['dishwasher']
        self.page_down()
        assert self.driver.find_element(*SupplierPageLocators.categories_washer).get_attribute('value') == categoriesInfo['laundry_washer']
        assert self.driver.find_element(*SupplierPageLocators.categories_pedestal).get_attribute('value') == categoriesInfo['laundry_pedestal']
        assert self.driver.find_element(*SupplierPageLocators.categories_combo).get_attribute('value') == categoriesInfo['laundry_combo']
        assert self.driver.find_element(*SupplierPageLocators.categories_dryer).get_attribute('value') == categoriesInfo['laundry_dryer']
        assert self.driver.find_element(*SupplierPageLocators.categories_garbage_cabinet).get_attribute('value') == categoriesInfo['garbage_cabinet']
        assert self.driver.find_element(*SupplierPageLocators.categories_compactor).get_attribute('value') == categoriesInfo['compactor']
        assert self.driver.find_element(*SupplierPageLocators.categories_icemaker).get_attribute('value') == categoriesInfo['icemaker']
        assert self.driver.find_element(*SupplierPageLocators.categories_freezer).get_attribute('value') == categoriesInfo['freezer']
        assert self.driver.find_element(*SupplierPageLocators.categories_refrigerator).get_attribute('value') == categoriesInfo['refrigerator']
        #self.driver.find_element(*SupplierPageLocators.categories_cancel_button).click()
        self.driver.find_element(*SupplierPageLocators.categories_save_button).click()

    def check_pending_customer_volume_detail(self):
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
