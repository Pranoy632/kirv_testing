import time
import random

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

from pages.basepage import BasePage
from pages.buyer_pages.load_building import BuildLoad
from locators.buyer_locators.homepage_locators import HomePageLocators, AllProductsLocators, ProductDetailsLocator


class Checkout(BasePage):

    def select_single_warehouse(self):
        self.driver.find_element(*AllProductsLocators.sorting_by_warehouse).click()
        self.wait_for_element(AllProductsLocators.select_ronkonkoma).click()
        self.driver.find_element(*AllProductsLocators.warehouse_apply_button).click()
        self.wait_for_element(AllProductsLocators.loader)
        self.wait_for_element(AllProductsLocators.page_menu)

    def get_each_category(self):
        BuildLoad(self.driver).go_to_categories()
        categories = self.driver.find_element(*HomePageLocators.total_categories)
        categories_list = categories.find_elements(*HomePageLocators.single_category)
        for category in categories_list:
            try:
                category.click()
                time.sleep(1)
            except ElementNotVisibleException:
                BuildLoad(self.driver).go_to_categories()
                category.click()
                time.sleep(1)
            self.wait_for_element(AllProductsLocators.sorting_by_warehouse)
            self.select_single_warehouse()
            all_menus = self.driver.find_element(*AllProductsLocators.page_menu)
            menu_list = all_menus.find_elements(*AllProductsLocators.all_menus)
            sub_category = random.choice(menu_list)
            sub_category.click()
            self.wait_for_element(AllProductsLocators.loader)
            self.wait_for_element(AllProductsLocators.sorting_by_warehouse)
            try:
                self.driver.find_element(*AllProductsLocators.no_products)
            except NoSuchElementException:
                product_matrix = self.driver.find_elements(*AllProductsLocators.product_cell)
                selected_product = random.choice(product_matrix)
                print(selected_product)
                selected_product.click()
                self.wait_for_element(ProductDetailsLocator.purchase_box)
                self.driver.find_element(*ProductDetailsLocator.product_quantity_dropdown).click()
                time.sleep(1)
                dropdown_values = self.driver.find_element(*ProductDetailsLocator.product_quantity)
                li_list = dropdown_values.find_elements_by_tag_name('li')
                li_list[-1].click()
