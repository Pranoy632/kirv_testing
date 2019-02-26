import time
from locators.supplier_locators.locatorSupplier import SupplierPageLocators
from pages.basepage import BasePage
from locators.supplier_locators.add_product_locators import AddProduct


class ProductPage(BasePage):

    def product_tab_click(self):
        time.sleep(2)
        self.driver.find_element(*SupplierPageLocators.products_link).click()

    def add_product(self):

        self.driver.find_element(*AddProduct.products_link).click()
        self.driver.find.element(*AddProduct.product_search_bar).sendkeys('LG Fridge')
        self.driver.find.element(*AddProduct.product_type).click()
        self.driver.find_element(*AddProduct.sku_number).sendkeys('MKAD2664A')
        self.driver.find.element(*AddProduct.brand).click()
        self.driver.find.element(*AddProduct.sub_category).click()
        self.driver.find.element(*AddProduct.color).click()
        self.driver.find.element(*AddProduct.brand).click()
        self.driver.find.element(*AddProduct.model_number).sendkeys('ADA11AAA')
        self.driver.find_element(*AddProduct.dim_uom).click()

