import time
import random

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

from pages.basepage import BasePage
from pages.buyer_pages.load_building import BuildLoad
from locators.buyer_locators.homepage_locators import HomePageLocators, AllProductsLocators, ProductDetailsLocator


class Checkout(BasePage):

    def select_single_warehouse(self):
        self.driver.find_element(*AllProductsLocators.sorting_by_warehouse).click()
        self.wait_for_element(AllProductsLocators.page_menu)
        dropdown = self.driver.find_element(*AllProductsLocators.warehouse_dropdown)
        dropdown_list = dropdown.find_elements(*AllProductsLocators.warehouse_drop_down_values)
        for warehouse in dropdown_list[:-1]:
            warehouse.click()
        self.driver.find_element(*AllProductsLocators.warehouse_apply_button).click()
        self.wait_for_element(AllProductsLocators.loader)
        self.wait_for_element(AllProductsLocators.page_menu)

    def get_each_category(self):
        BuildLoad(self.driver).go_to_categories()
        categories = self.driver.find_element(*HomePageLocators.total_categories)
        categories_list = categories.find_elements(*HomePageLocators.single_category)
        flag = 0
        for category in categories_list:
            category.click()
            time.sleep(1)
            self.wait_for_element(AllProductsLocators.page_menu)
            if flag == 0:
                self.select_single_warehouse()
                flag=1

            all_menus = self.driver.find_element(*AllProductsLocators.page_menu)
            menu_list = all_menus.find_elements(*AllProductsLocators.all_menus)

            for x in range(1, len(menu_list)+1):
                self.driver.find_element_by_css_selector('.page-title-menu > li:nth-child({0})'.format(x)).click()
                self.wait_for_element(AllProductsLocators.loader)
                self.wait_for_element(AllProductsLocators.page_menu)

                try:
                    product_matrix = self.driver.find_elements(*AllProductsLocators.product_cell)
                    selected_product = random.choice(product_matrix)
                    # print(product)
                    selected_product.click()
                    self.wait_for_element(ProductDetailsLocator.purchase_box)
                    self.driver.find_element(*ProductDetailsLocator.product_quantity_dropdown).click()
                    time.sleep(1)
                    dropdown_values = self.driver.find_element(*ProductDetailsLocator.product_quantity)
                    li_list = dropdown_values.find_elements_by_tag_name('li')
                    li_list[-1].click()
                    self.driver.find_element(*ProductDetailsLocator.add_to_load).click()
                    self.wait_for_element(ProductDetailsLocator.truck_size_modal)
                    self.driver.find_element(*ProductDetailsLocator.truck_size_modal)
                    random.choice(self.driver.find_elements(*ProductDetailsLocator.truck_sizes)).click()

                except NoSuchElementException:
                    self.driver.find_element(*AllProductsLocators.no_products)
