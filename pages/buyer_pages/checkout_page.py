import time
import random

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

from pages.basepage import BasePage
from pages.buyer_pages.load_building import BuildLoad
from locators.buyer_locators.homepage_locators import HomePageLocators, AllProductsLocators, ProductDetailsLocator


class Checkout(BasePage):

    # def select_single_warehouse(self):
    #     self.driver.find_element(*AllProductsLocators.sorting_by_warehouse).click()
    #     self.driver.find_element(*AllProductsLocators.)

    def get_each_category(self):
        BuildLoad(self.driver).go_to_categories()
        categories = self.driver.find_element(*HomePageLocators.total_categories)
        categories_list = categories.find_elements(*HomePageLocators.single_category)
        print(categories_list)
        print(len(categories_list))
        for category in categories_list:
            print('loop entered')
            try:
                category.click()
                time.sleep(1)
            except ElementNotVisibleException:
                BuildLoad(self.driver).go_to_categories()
                category.click()
                time.sleep(1)
            self.wait_for_element(AllProductsLocators.sorting_by_warehouse)
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
                #self.driver.find_element(ProductDetailsLocator.)