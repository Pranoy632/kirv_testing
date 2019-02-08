from pages.basepage import *
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import LocationLocators

cities = []
retail_address_lookup = ''


class Location(BasePage):

    def element_in_location_page(self):
        self.driver.find_element(
            *LocationLocators.location_num2).click()
        time.sleep(1)
        self.backStep_retail_location_count_page()

        time.sleep(2)
        self.equality_assert(self.driver.find_element(
            *LocationLocators.add_loc_btn).is_enabled(), False)

        self.add_retail_location()

    def backStep_retail_location_count_page(self):
        """
            goes back one step and checks expected page
        """
        self.driver.find_element(
            *LocationLocators.back_a_step).click()
        self.equality_assert(
            self.driver.find_element(*LocationLocators.kirv_logo).is_displayed(), True)
        self.equality_assert(
            self.driver.find_element(*LocationLocators.step2).is_displayed(), True)
        self.equality_assert(
            self.driver.find_element(*LocationLocators.location_num2).is_displayed(), True)
        self.driver.find_element(
            *LocationLocators.location_num2).click()

    def backStep_retail_location(self):
        """
            goes back one step and checks expected page
        """
        time.sleep(2)
        self.driver.find_element(*LocationLocators.back_a_step).click()
        self.equality_assert(
            self.driver.find_element(*LocationLocators.kirv_logo).is_displayed(), True)
        self.equality_assert(
            self.driver.find_element(*LocationLocators.step2).is_displayed(), True)
        self.equality_assert(
            self.driver.find_element(*LocationLocators.retail_location).is_displayed(), True)

    def add_retail_location(self):
        """
            adds given number of locations
        """
        self.negative_retail_location_by_lookup()
        self.positive_retail_location_by_lookup()
        self.equality_assert(self.driver.find_element(
            *LocationLocators.google_map).is_displayed(), True)
        self.edit_address_lookup()
        self.negative_confirmation_location()
        self.positive_confirmation_location()
        self.backStep_confirm_location()
        self.negative_retail_location_by_lookup()
        cities = []
        self.driver.find_element(
            *LocationLocators.enter_manually).click()
        self.backStep_retail_location()
        self.driver.find_element(
            *LocationLocators.enter_manually).click()
        self.negative_retail_location_test()
        self.positive_retail_location_test()
        self.edit_address()
        self.negative_confirmation_location()
        self.positive_confirmation_location()

    def negative_retail_location_by_lookup(self):
        """
            negative test for retail location form using lookup
        """
        self.enter_text(LocationLocators.loc_name_input, fake.street_name())

        self.enter_text(LocationLocators.loc_address_input, 98)
        time.sleep(1)
        self.driver.find_element(*LocationLocators.retail_dropdown).click()
        time.sleep(1)

        self.clear_input(LocationLocators.loc_name_input)
        self.clear_input(LocationLocators.loc_address_input)

        time.sleep(1)
        self.driver.find_element(*LocationLocators.add_loc_btn).click()
        time.sleep(1)
        self.subset_assert('has-danger', self.driver.find_element(*
                                                                  LocationLocators.loc_name_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(*
                                                                  LocationLocators.loc_address_error).get_attribute('class').split())

        if '2' in self.driver.find_element(*LocationLocators.retail_location_count).text:
            self.enter_text(LocationLocators.loc_name_input,
                            fake.street_name())
            self.enter_text(LocationLocators.loc_address_input, 98)
            time.sleep(1)
            self.driver.find_element(*LocationLocators.retail_dropdown).click()
            time.sleep(2)
            self.driver.find_element(*LocationLocators.add_loc_btn).click()
            time.sleep(2)
            self.subset_assert('has-danger', self.driver.find_element(
                *LocationLocators.loc_address_error).get_attribute('class').split())

    def positive_retail_location_by_lookup(self):
        """
            positive test for retail location form using lookup
        """
        global retail_loc_name
        global retail_address

        retail_loc_name = fake.street_name()
        self.enter_text(LocationLocators.loc_name_input, retail_loc_name)

        self.enter_text(LocationLocators.loc_address_input, 23)
        time.sleep(1)
        self.driver.find_element(*LocationLocators.retail_dropdown).click()
        time.sleep(1)
        retail_address = self.driver.find_element(
            *LocationLocators.loc_address_input).get_attribute('value')

        self.driver.find_element(*LocationLocators.add_loc_btn).click()
        self.backStep_retail_location()
        self.driver.find_element(*LocationLocators.update_loc_btn).click()

    def edit_address_lookup(self):
        """
            Edit Retail location form
        """
        global retail_address

        self.driver.find_element(*LocationLocators.edit_address_btn).click()
        self.equality_assert(self.driver.find_element(
            *LocationLocators.loc_name_input).get_attribute('value'), retail_loc_name)
        self.equality_assert(self.driver.find_element(
            *LocationLocators.loc_address_input).get_attribute('value'), retail_address)

        self.clear_input(LocationLocators.loc_address_input)

        self.enter_text(LocationLocators.loc_address_input, 98)
        time.sleep(1)
        self.driver.find_element(*LocationLocators.retail_dropdown).click()
        time.sleep(1)

        self.driver.find_element(*LocationLocators.update_loc_btn).click()
        time.sleep(1)
        self.driver.find_element(*LocationLocators.edit_address_btn).click()
        time.sleep(1)
        self.driver.find_element(*LocationLocators.enter_manually).click()
        time.sleep(1)

        retail_address_lookup = self.driver.find_element(
            *LocationLocators.city_input).get_attribute('value')
        self.driver.find_element(*LocationLocators.update_loc_btn).click()

    def negative_retail_location_test(self):
        """
            negative testing of retail location form
        """
        time.sleep(1)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', self.driver.find_element(
            *LocationLocators.add_loc_btn))

        self.driver.find_element(
            *LocationLocators.add_loc_btn).click()
        time.sleep(2)

        self.subset_assert('has-danger', self.driver.find_element(*
                                                                  LocationLocators.loc_name_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(*
                                                                  LocationLocators.address_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(*
                                                                  LocationLocators.city_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(*
                                                                  LocationLocators.state_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(*
                                                                  LocationLocators.zip_code_error).get_attribute('class').split())

        self.clear_put_input_value(LocationLocators.zip_code_input, 'abc')

        self.driver.find_element(
            *LocationLocators.add_loc_btn).click()
        time.sleep(1)

        self.subset_assert('has-danger', self.driver.find_element(*
                                                                  LocationLocators.zip_code_error).get_attribute('class').split())

        self.clear_put_input_value(LocationLocators.zip_code_input, 1234567)

        self.driver.find_element(
            *LocationLocators.add_loc_btn).click()
        time.sleep(1)

        self.subset_assert('has-danger', self.driver.find_element(*
                                                                  LocationLocators.zip_code_error).get_attribute('class').split())
        self.clear_input(LocationLocators.zip_code_input)

    def positive_retail_location_test(self):
        """
            positive testing of retail location form
        """

        global location_name
        global address
        global unit_number
        global city
        global state
        global zipcode

        location_name = fake.street_name()
        self.enter_text(LocationLocators.loc_name_input, location_name)

        address = fake.address()
        self.enter_text(LocationLocators.address_input, address)

        unit_number = fake.random_int()
        self.enter_text(LocationLocators.unit_no_input, unit_number)

        city = fake.city()
        self.enter_text(LocationLocators.city_input, city)

        self.driver.find_element(
            *LocationLocators.state_input).click()
        time.sleep(1)
        dropdown_values = self.driver.find_element(
            *LocationLocators.loc_dropdown_values)
        states_list = dropdown_values.find_elements_by_tag_name('li')
        random.choice(states_list[1:]).click()

        state = self.driver.find_element(
            *LocationLocators.state_input).get_attribute('value')

        zipcode = fake.zipcode()
        self.enter_text(LocationLocators.zip_code_input, zipcode)

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.add_loc_btn).click()

    def edit_address(self):
        """
            Edits address of retail location.
        """
        self.equality_assert(self.driver.find_element(
            *LocationLocators.edit_address_btn).is_displayed(), True)
        self.driver.find_element(*LocationLocators.edit_address_btn).click()
        time.sleep(2)

        self.equality_assert(self.driver.find_element(
            *LocationLocators.loc_name_input).get_attribute('value'), location_name)
        self.equality_assert(self.driver.find_element(
            *LocationLocators.address_input).get_attribute('value'), address.replace('\n', ''))
        self.equality_assert(self.driver.find_element(
            *LocationLocators.unit_no_input).get_attribute('value'), str(unit_number))
        self.equality_assert(self.driver.find_element(
            *LocationLocators.city_input).get_attribute('value'), city)
        self.equality_assert(self.driver.find_element(
            *LocationLocators.state_input).get_attribute('value'), state)
        self.equality_assert(self.driver.find_element(
            *LocationLocators.zip_code_input).get_attribute('value'), zipcode)

        self.clear_input(LocationLocators.city_input)
        new_city = fake.city()
        self.clear_put_input_value(LocationLocators.city_input, new_city)
        cities.append(new_city)

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.update_loc_btn).click()

    def negative_confirmation_location(self):
        """
            negative testing of confirm location form
        """
        invalid_email_id = ['abc', 'abc@gmail', 'abc.com', '.abc@gmail.com',
                            'abc.@gmail.com', 'abc@.gmail.com', 'abc@gmail.com.', 'abc ef@gmail.com']
        invalid_phone_number = ['abc', 12345]

        self.driver.find_element(*LocationLocators.next_btn).click()
        time.sleep(2)
        self.subset_assert('has-danger', self.driver.find_element(
            *LocationLocators.email_address_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(*
                                                                  LocationLocators.phone_number_error).get_attribute('class').split())

        for current in invalid_email_id:
            self.clear_put_input_value(
                LocationLocators.email_address_input, current)
            self.driver.find_element(
                *LocationLocators.next_btn).click()
            time.sleep(1)
            self.subset_assert('has-danger', self.driver.find_element(
                *LocationLocators.email_address_error).get_attribute('class').split())
        self.clear_input(LocationLocators.email_address_input)

        for current in invalid_phone_number:
            self.clear_put_input_value(
                LocationLocators.phone_number_input, current)
            self.clear_put_input_value(
                LocationLocators.alt_phone_number_input, current)
            self.driver.find_element(
                *LocationLocators.next_btn).click()
            time.sleep(1)
            self.subset_assert('has-danger', self.driver.find_element(
                *LocationLocators.phone_number_error).get_attribute('class').split())
            self.subset_assert('has-danger', self.driver.find_element(
                *LocationLocators.alt_phone_number_error).get_attribute('class').split())
        self.clear_input(LocationLocators.phone_number_input)
        self.clear_input(LocationLocators.alt_phone_number_input)

    def positive_confirmation_location(self):
        """
            positive testing of confirm location form
        """
        self.enter_text(LocationLocators.email_address_input, fake.email())
        self.enter_text(LocationLocators.phone_number_input,
                        self.create_phone_number())
        self.enter_text(LocationLocators.alt_phone_number_input,
                        self.create_phone_number())
        self.driver.find_element(
            *LocationLocators.next_btn).click()

    def backStep_confirm_location(self):
        """
            goes back and checks expected page
        """
        time.sleep(2)
        self.driver.find_element(*LocationLocators.back_a_step).click()
        self.equality_assert(
            self.driver.find_element(*LocationLocators.kirv_logo).is_displayed(), True)
        self.equality_assert(
            self.driver.find_element(*LocationLocators.step2).is_displayed(), True)
        self.equality_assert(
            self.driver.find_element(*LocationLocators.confirm_location_title).is_displayed(), True)
        self.driver.find_element(
            *LocationLocators.next_btn).click()
