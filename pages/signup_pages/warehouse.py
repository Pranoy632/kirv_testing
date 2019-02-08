from pages.basepage import *
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import WareHouseLocators
from .location import cities, retail_address_lookup

warehouse_city = []


class WareHouse(BasePage):

    retail_address_lookup = 'boston'

    def elements_of_warehouse(self):
        try:
            self.subset_assert(self.driver.find_element(
                *WareHouseLocators.check_first_retail_location).text, cities)
        except:
            self.equality_assert(self.driver.find_element(
                *WareHouseLocators.check_first_retail_location).text, self.retail_address_lookup)

        try:
            self.equality_assert(self.driver.find_element(
                *WareHouseLocators.check_second_retail_location).text, self.retail_address_lookup)
        except:
            self.subset_assert(self.driver.find_element(
                *WareHouseLocators.check_second_retail_location).text, cities)

        self.negative_retail_checklist_test()
        self.positive_retail_checklist_test()

    def negative_retail_checklist_test(self):
        """
            checks all combiations of retail location checklist
        """
        self.driver.find_element(
            *WareHouseLocators.check_none_retail_location).click()

        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.check_none_retail_location_id).is_selected(), True)

        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.check_first_retail_location_id).is_selected(), False)

        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.check_second_retail_location_id).is_selected(), False)

        self.driver.find_element(
            *WareHouseLocators.confirm_btn).click()
        time.sleep(1)

        self.driver.find_element(
            *WareHouseLocators.back_a_step).click()
        time.sleep(1)

        self.driver.find_element(
            *WareHouseLocators.check_first_retail_location).click()

        self.driver.find_element(
            *WareHouseLocators.check_second_retail_location).click()

        time.sleep(2)
        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.check_first_retail_location_id).is_selected(), True)

        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.check_second_retail_location_id).is_selected(), True)

        self.driver.find_element(
            *WareHouseLocators.confirm_btn).click()
        time.sleep(2)

        self.driver.find_element(
            *WareHouseLocators.no_additional_warehouse_btn).click()
        time.sleep(2)

        self.subset_assert("Step 4 of 5 - Purchasing preferences",
                           self.driver.find_element(*WareHouseLocators.purchasing_preferences).text)

        self.driver.find_element(
            *WareHouseLocators.back_a_step).click()
        time.sleep(2)

        self.equality_assert(
            self.driver.find_element(*WareHouseLocators.no_additional_warehouse_btn).is_displayed(), True)

        self.driver.find_element(
            *WareHouseLocators.back_a_step).click()
        time.sleep(2)

    def positive_retail_checklist_test(self):
        """
            selects one of the retail location
        """
        self.driver.find_element(
            *WareHouseLocators.check_first_retail_location).click()

        self.driver.find_element(
            *WareHouseLocators.confirm_btn).click()

        time.sleep(1)
        self.driver.find_element(
            *WareHouseLocators.warehouse_num2).click()

        time.sleep(1)
        self.backStep_warehouse_locations_count_page()

        self.add_warehouse()

    def backStep_warehouse_locations_count_page(self):
        """
            goes back one step and checks expected page
        """
        self.driver.find_element(
            *WareHouseLocators.back_a_step).click()
        self.equality_assert(
            self.driver.find_element(*WareHouseLocators.kirv_logo).is_displayed(), True)
        self.equality_assert(
            self.driver.find_element(*WareHouseLocators.step3).is_displayed(), True)
        self.equality_assert(
            self.driver.find_element(*WareHouseLocators.warehouse_num2).is_displayed(), True)
        self.driver.find_element(
            *WareHouseLocators.warehouse_num2).click()

    def backStep_warehouse_location(self):
        """
            goes back one step and checks expected page
        """
        time.sleep(2)
        self.driver.find_element(
            *WareHouseLocators.back_a_step).click()
        self.equality_assert(
            self.driver.find_element(*WareHouseLocators.kirv_logo).is_displayed(), True)
        self.equality_assert(
            self.driver.find_element(*WareHouseLocators.step3).is_displayed(), True)
        self.equality_assert(
            self.driver.find_element(*WareHouseLocators.warehouse_location).is_displayed(), True)

    def add_warehouse(self):
        """
            add warehouse location
        """
        self.negative_add_warehouse_by_lookup_test()
        self.positive_add_warehouse_by_lookup_test()
        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.google_map).is_displayed(), True)
        self.edit_address()
        self.negative_confirm_location_test()
        self.positive_confirm_location_test()
        self.backStep_confirm_location()
        self.negative_same_warehouse_address_test()
        self.driver.find_element(*WareHouseLocators.manual_link).click()
        #self.backStep_warehouse_location()
        #self.driver.find_element(*WareHouseLocators.manual_link).click()
        time.sleep(1)
        self.negative_add_warehouse_manually_test()
        self.positive_add_warehouse_manually_test()
        self.edit_address_manually()
        self.negative_confirm_location_test()
        self.positive_confirm_location_test()

    def negative_add_warehouse_by_lookup_test(self):
        """
            negative test -> add location using lookup
        """
        self.enter_text(WareHouseLocators.warehouse_name_input,
                        fake.street_name())

        self.enter_text(WareHouseLocators.warehouse_address_input, 23)
        time.sleep(1)
        self.driver.find_element(*WareHouseLocators.warehouse_dropdown).click()
        time.sleep(1)

        self.clear_input(WareHouseLocators.warehouse_name_input)
        self.clear_input(WareHouseLocators.warehouse_address_input)

        time.sleep(1)
        self.driver.find_element(*WareHouseLocators.add_loc_btn).click()
        time.sleep(1)
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_name_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_address_error).get_attribute('class').split())

        self.driver.find_element(
            *WareHouseLocators.manual_address_link).click()
        self.driver.find_element(*WareHouseLocators.lookup_link).click()

    def negative_same_warehouse_address_test(self):
        """
            negative test -> tests same address for lookup
        """
        time.sleep(1)
        self.enter_text(WareHouseLocators.warehouse_name_input,
                        fake.street_name())
        self.enter_text(WareHouseLocators.warehouse_address_input, 77)
        time.sleep(1)
        self.driver.find_element(*WareHouseLocators.warehouse_dropdown).click()
        time.sleep(2)
        self.driver.find_element(*WareHouseLocators.add_loc_btn).click()
        time.sleep(2)
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_address_error).get_attribute('class').split())

    def positive_add_warehouse_by_lookup_test(self):
        """
            positive test -> add location using lookup
        """
        global warehouse_name
        global warehouse_address

        warehouse_name = fake.street_name()
        self.enter_text(WareHouseLocators.warehouse_name_input, warehouse_name)

        self.enter_text(WareHouseLocators.warehouse_address_input, 23)
        time.sleep(1)
        self.driver.find_element(*WareHouseLocators.warehouse_dropdown).click()
        time.sleep(1)
        warehouse_address = self.driver.find_element(
            *WareHouseLocators.warehouse_address_input).get_attribute('value')

        self.driver.find_element(*WareHouseLocators.add_loc_btn).click()
        self.backStep_warehouse_location()
        self.driver.find_element(
            *WareHouseLocators.update_location_btn).click()

    def edit_address(self):
        """
            Edit warehouse address
        """
        global warehouse_address

        self.driver.find_element(*WareHouseLocators.edit_address).click()
        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.warehouse_name_input).get_attribute('value'), warehouse_name)
        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.warehouse_address_input).get_attribute('value'), warehouse_address)

        self.clear_input(WareHouseLocators.warehouse_address_input)

        self.enter_text(WareHouseLocators.warehouse_address_input, 77)
        time.sleep(1)
        self.driver.find_element(*WareHouseLocators.warehouse_dropdown).click()
        time.sleep(1)
        warehouse_address = self.driver.find_element(
            *WareHouseLocators.warehouse_address_input).get_attribute('value')

        self.driver.find_element(
            *WareHouseLocators.update_location_btn).click()

    def negative_confirm_location_test(self):
        """
            negative test -> confirm location of warehouse
        """
        invalid_email_id = ['abc', 'abc@gmail', 'abc.com', '.abc@gmail.com',
                            'abc.@gmail.com', 'abc@.gmail.com', 'abc@gmail.com.', 'abc ef@gmail.com']
        invalid_phone_number = ['abc', 12345]

        time.sleep(1)
        body = self.driver.find_element(*WareHouseLocators.body)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.confirm_and_continue_btn).is_enabled(), False)

        self.clear_put_input_value(
            WareHouseLocators.warehouse_email_input, 'abc')
        self.clear_put_input_value(
            WareHouseLocators.warehouse_phone_no_input, 'abc')
        self.clear_put_input_value(
            WareHouseLocators.warehouse_alt_phone_no_input, 'abc')

        self.driver.find_element(*WareHouseLocators.from_time_btn).click()
        time.sleep(1)
        self.driver.find_element(*WareHouseLocators.from_time).click()
        self.driver.find_element(*WareHouseLocators.ok_btn).click()

        time.sleep(1)
        self.driver.find_element(*WareHouseLocators.until_time_btn).click()
        time.sleep(1)
        self.driver.find_element(*WareHouseLocators.until_time).click()
        self.driver.find_element(*WareHouseLocators.ok_btn).click()

        time.sleep(1)
        self.driver.find_element(
            *WareHouseLocators.confirm_and_continue_btn).click()
        time.sleep(2)
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_email_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_phone_no_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_alt_phone_no_error).get_attribute('class').split())

        self.clear_put_input_value(
            WareHouseLocators.warehouse_email_input, 'abc@gmail')
        self.clear_put_input_value(
            WareHouseLocators.warehouse_phone_no_input, '12345')
        self.clear_put_input_value(
            WareHouseLocators.warehouse_alt_phone_no_input, '12345')
        self.driver.find_element(
            *WareHouseLocators.confirm_and_continue_btn).click()
        time.sleep(2)
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_email_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_phone_no_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_alt_phone_no_error).get_attribute('class').split())

    def positive_confirm_location_test(self):
        """
            positive test -> confirm location of warehouse
        """
        self.clear_put_input_value(
            WareHouseLocators.warehouse_email_input, fake.email())
        self.clear_put_input_value(
            WareHouseLocators.warehouse_phone_no_input, self.create_phone_number())
        self.clear_put_input_value(
            WareHouseLocators.warehouse_alt_phone_no_input, self.create_phone_number())

        self.driver.find_element(*WareHouseLocators.from_time_btn).click()
        time.sleep(1)
        self.driver.find_element(*WareHouseLocators.from_time).click()
        self.driver.find_element(*WareHouseLocators.ok_btn).click()

        time.sleep(1)
        self.driver.find_element(*WareHouseLocators.until_time_btn).click()
        time.sleep(1)
        self.driver.find_element(*WareHouseLocators.until_time).click()
        self.driver.find_element(*WareHouseLocators.ok_btn).click()

        time.sleep(1)
        self.driver.find_element(
            *WareHouseLocators.confirm_and_continue_btn).click()

    def negative_add_warehouse_manually_test(self):
        """
            negative test -> Add warehouse manually
        """

        self.driver.find_element(*WareHouseLocators.add_loc_btn).click()
        time.sleep(2)

        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_name_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_address_line_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_city_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_state_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_zipcode_error).get_attribute('class').split())

        self.clear_put_input_value(
            WareHouseLocators.warehouse_zipcode_input, 'abc')

        self.driver.find_element(*WareHouseLocators.add_loc_btn).click()
        time.sleep(1)

        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_zipcode_error).get_attribute('class').split())

        self.clear_put_input_value(
            WareHouseLocators.warehouse_zipcode_input, 1234567)

        self.driver.find_element(*WareHouseLocators.add_loc_btn).click()
        time.sleep(1)

        self.subset_assert('has-danger', self.driver.find_element(
            *WareHouseLocators.warehouse_zipcode_error).get_attribute('class').split())
        self.clear_input(WareHouseLocators.warehouse_zipcode_input)

    def positive_add_warehouse_manually_test(self):
        """
            positive test -> Add warehouse manually
        """
        global name
        global address
        global unit_number
        global city
        global state
        global zipcode

        name = fake.street_name()
        self.enter_text(WareHouseLocators.warehouse_name_input, name)

        address = fake.address()
        self.enter_text(
            WareHouseLocators.warehouse_address_line_input, address)

        unit_number = fake.random_int()
        self.enter_text(
            WareHouseLocators.warehouse_unit_number_input, unit_number)

        city = fake.city()
        self.enter_text(WareHouseLocators.warehouse_city_input, city)

        self.driver.find_element(
            *WareHouseLocators.warehouse_state_input).click()
        time.sleep(1)
        dropdown_values = self.driver.find_element(
            *WareHouseLocators.warehouse_dropdown_values)
        states_list = dropdown_values.find_elements_by_tag_name('li')
        random.choice(states_list[1:]).click()

        state = self.driver.find_element(
            *WareHouseLocators.warehouse_state_input).get_attribute('value')

        zipcode = fake.zipcode()
        self.enter_text(WareHouseLocators.warehouse_zipcode_input, zipcode)

        time.sleep(1)
        self.driver.find_element(*WareHouseLocators.add_loc_btn).click()

    def edit_address_manually(self):
        """
            Edits address of retail location.
        """
        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.edit_address).is_displayed(), True)
        self.driver.find_element(*WareHouseLocators.edit_address).click()
        time.sleep(2)

        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.warehouse_name_input).get_attribute('value'), name)
        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.warehouse_address_line_input).get_attribute('value'), address.replace('\n', ''))
        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.warehouse_unit_number_input).get_attribute('value'), str(unit_number))
        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.warehouse_city_input).get_attribute('value'), city)
        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.warehouse_state_input).get_attribute('value'), state)
        self.equality_assert(self.driver.find_element(
            *WareHouseLocators.warehouse_zipcode_input).get_attribute('value'), zipcode)

        self.clear_input(WareHouseLocators.warehouse_city_input)
        new_city = fake.city()
        self.clear_put_input_value(
            WareHouseLocators.warehouse_city_input, new_city)
        warehouse_city.append(new_city)

        time.sleep(1)
        self.driver.find_element(
            *WareHouseLocators.update_location_btn).click()

    def backStep_confirm_location(self):
        """
            goes back and checks expected page
        """
        time.sleep(2)
        self.driver.find_element(
            *WareHouseLocators.back_a_step).click()
        self.equality_assert(
            self.driver.find_element(*WareHouseLocators.kirv_logo).is_displayed(), True)
        self.equality_assert(
            self.driver.find_element(*WareHouseLocators.step3).is_displayed(), True)
        self.equality_assert(
            self.driver.find_element(*WareHouseLocators.confirm_location_title).is_displayed(), True)
        self.driver.find_element(
            *WareHouseLocators.confirm_and_continue_btn).click()
