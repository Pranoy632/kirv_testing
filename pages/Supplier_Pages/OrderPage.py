import time
from locators.supplier_locators.locatorSupplier import SupplierPageLocators
from pages.basepage import BasePage


class OrderPage(BasePage):

    def tab_click(self):
            time.sleep(1)
            self.driver.find_element(*SupplierPageLocators.orders_link).click()
