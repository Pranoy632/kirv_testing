from pages.basepage import *
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from locators.sign_up_locators.locatorSignup import LocationLocators


class Location(BasePage):

    def element_in_location_page(self):
        self.driver.find_element(
            *LocationLocators.location_num2).click()

        time.sleep(1)
        self.equality_assert(self.is_button_enabled(LocationLocators.add_loc_btn), False)

        self.add_retail_location(2)


    def is_button_enabled(self, button):
        """
            checks if givenn button is enabled or not
        """
        return self.driver.find_element(*button).is_enabled()

    def equality_assert(self, first_arg, second_arg):
        """
            assertion for equality of two arguments
        """
        assert first_arg == second_arg

    def subset_assert(self, first_arg, second_arg):
        """
            assertion for subset of object
        """
        assert first_arg in second_arg

    def clear_put_input_value(self, locator, input_value):
        """
            clears and puts input in input box
        """
        time.sleep(2)
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(input_value)

    def clear_input(self, locator):
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    def negative_retail_location_test(self):
        """
            negative testing of retail location form
        """
        self.driver.find_element(
            *LocationLocators.enter_manually).click()

        time.sleep(1)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', self.driver.find_element(
            *LocationLocators.add_loc_btn))

        self.driver.find_element(
            *LocationLocators.add_loc_btn).click()
        time.sleep(2)

        self.subset_assert('has-danger', self.driver.find_element(*LocationLocators.loc_name_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(*LocationLocators.address_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(*LocationLocators.city_error).get_attribute('class').split())
        # self.subset_assert('has-danger', self.driver.find_element(*LocationLocators.state_error).get_attribute('class').split())
        self.subset_assert('has-danger', self.driver.find_element(*LocationLocators.zip_code_error).get_attribute('class').split())

        self.clear_put_input_value(LocationLocators.zip_code_input, 'abc')
        self.driver.find_element(
            *LocationLocators.add_loc_btn).click()
        time.sleep(1)
        self.subset_assert('has-danger', self.driver.find_element(*LocationLocators.zip_code_error).get_attribute('class').split())
        self.clear_put_input_value(LocationLocators.zip_code_input, 1234567)
        self.driver.find_element(
            *LocationLocators.add_loc_btn).click()
        time.sleep(1)
        self.subset_assert('has-danger', self.driver.find_element(*LocationLocators.zip_code_error).get_attribute('class').split())
        self.clear_input(LocationLocators.zip_code_input)
        
    def positive_retail_location_test(self):
        """
            positive testing of retail location form
        """

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.loc_name_input).send_keys(fake.street_name())

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.address_input).send_keys(fake.address())

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.city_input).send_keys(fake.city())

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.state_input).click()
        time.sleep(1)
        action = action_chains.ActionChains(self.driver)
        action.send_keys(Keys.DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.zip_code_input).send_keys(fake.zipcode())

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.add_loc_btn).click()

    def negative_confirmation_location(self):
        """
            negative testing of confirm location form
        """
        invalid_email_id = ['abc', 'abc@gmail', 'abc.com', '.abc@gmail.com', 'abc.@gmail.com', 'abc@.gmail.com', 'abc@gmail.com.', 'abc ef@gmail.com']
        invalid_phone_number = ['abc', 12345]
        
        self.driver.find_element(*LocationLocators.next_btn).click()
        time.sleep(2)
        self.subset_assert('has-danger', self.driver.find_element(*LocationLocators.email_address_error).get_attribute('class').split())
        # self.subset_assert('has-danger', self.driver.find_element(*LocationLocators.phone_number_error).get_attribute('class').split())

        for current in invalid_email_id:
            self.clear_put_input_value(LocationLocators.email_address_input, current)
            self.driver.find_element(
                *LocationLocators.next_btn).click()
            time.sleep(1)
            self.subset_assert('has-danger', self.driver.find_element(*LocationLocators.email_address_error).get_attribute('class').split())
        self.clear_input(LocationLocators.email_address_input)

        for current in invalid_phone_number:
            self.clear_put_input_value(LocationLocators.phone_number_input, current)
            self.clear_put_input_value(LocationLocators.alt_phone_number_input, current)
            self.driver.find_element(
                *LocationLocators.next_btn).click()
            time.sleep(1)
            self.subset_assert('has-danger', self.driver.find_element(*LocationLocators.phone_number_error).get_attribute('class').split())
            self.subset_assert('has-danger', self.driver.find_element(*LocationLocators.alt_phone_number_error).get_attribute('class').split())
        self.clear_input(LocationLocators.phone_number_input)
        self.clear_input(LocationLocators.alt_phone_number_input)

    def positive_confirmation_location(self):
        """
            positive testing of confirm location form
        """
        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.email_address_input).send_keys(fake.email())

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.phone_number_input).send_keys(self.create_phone_number())

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.alt_phone_number_input).send_keys(self.create_phone_number())

        time.sleep(1)
        self.driver.find_element(
            *LocationLocators.next_btn).click()

    def add_retail_location(self, no_of_locations):
        for current in range(no_of_locations):
            self.negative_retail_location_test()
            self.positive_retail_location_test()
            self.negative_confirmation_location()
            self.positive_confirmation_location()
