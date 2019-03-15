import time
from pages.basepage import BasePage
from locators.supplier_locators.admin_order_locators import Admin_Locators
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys


class Services(BasePage):


    def login(self, username, password):
        self.driver.find_element(*Admin_Locators.name).send_keys(username)
        self.driver.find_element(*Admin_Locators.password).send_keys(password)
        self.driver.find_element(*Admin_Locators.submitButton).click()
        return

    def click_on_service(self):
        Kirv_Logo = self.driver.find_element(*Admin_Locators.kirv_services_logo)
        Customer_Service = self.driver.find_element(*Admin_Locators.customer_dashboard_locator)
        Kirv_Service = self.driver.find_element(*Admin_Locators.kirv_service_locator)
        B2B_Service = self.driver.find_element(*Admin_Locators.B2B)
        Super_admin = self.driver.find_element(*Admin_Locators.super_admin_locator)
        sso_super_admin = self.driver.find_element(*Admin_Locators.sso_super_admin_locator)
        try:
            assert(Kirv_Logo.is_displayed())
            assert(Customer_Service.is_displayed())
            assert(Customer_Service.is_enabled())
            assert(Kirv_Service.is_displayed())
            assert(Kirv_Service.is_enabled())
            assert(B2B_Service.is_displayed())
            assert(B2B_Service.is_enabled())
            assert(Super_admin.is_displayed())
            assert(Super_admin.is_enabled())
            assert(sso_super_admin.is_displayed())
            assert(sso_super_admin.is_enabled())
            B2B_Service.click()
            print("Success ->  services are displayed")
        except:
            print("Error -> services are not displayed")
        return 1




