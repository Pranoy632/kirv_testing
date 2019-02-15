import time
import random

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

from pages.basepage import BasePage
from pages.buyer_pages.load_building import BuildLoad
from locators.buyer_locators.homepage_locators import HomePageLocators, AllProductsLocators, ProductDetailsLocator


class Checkout(BasePage):

    def select_single_warehouse(self):

        # select ronkonkoma warehouse from 'sort by warehouse' dropdown
        self.driver.find_element(*AllProductsLocators.sorting_by_warehouse).click()
        self.wait_for_element(AllProductsLocators.warehouse_dropdown)
        self.driver.find_element(*AllProductsLocators.warehouse_apply_button).click()
        self.wait_for_element(AllProductsLocators.loader)
        self.wait_for_element(AllProductsLocators.page_menu)

    def get_each_category(self):
        product_description = []
        # click on categories menu
        BuildLoad(self.driver).go_to_categories()

        # get all categories in a variable
        categories = self.driver.find_element(*HomePageLocators.total_categories)
        categories_list = categories.find_elements(*HomePageLocators.single_category)

        # click on each category one by one
        for category in categories_list:
            try:
                category.click()
                time.sleep(1)
            except ElementNotVisibleException:
                # click on categories dropdown when loop you enter the loop for second time
                BuildLoad(self.driver).go_to_categories()
                category.click()
                time.sleep(1)

            self.wait_for_element(AllProductsLocators.sorting_by_warehouse)
            self.select_single_warehouse()

            # Collect all the sub-categories in a variable
            #all_menus = self.driver.find_element(*AllProductsLocators.page_menu)
            #menu_list = all_menus.find_elements(*AllProductsLocators.all_menus)

            # select any product from the matrix of product
            #sub_category = random.choice(menu_list)
            #sub_category.click()
            #self.wait_for_element(AllProductsLocators.loader)
            #self.wait_for_element(AllProductsLocators.sorting_by_warehouse)

            # if there are "no products" found under a particular category, then skip it and go to next category
            try:
                self.driver.find_element(*AllProductsLocators.no_products)
            except NoSuchElementException:
                # select any random product
                product_matrix = self.driver.find_elements(*AllProductsLocators.product_cell)
                selected_product = random.choice(product_matrix).click()
                #selected_product.click()
                self.wait_for_element(ProductDetailsLocator.purchase_box)

                # select "ronkonkoma warehouse"
                warehouse_tabs = self.driver.find_element(*ProductDetailsLocator.warehouse_locations_tabs)
                warehouses_list = warehouse_tabs.find_elements_by_tag_name('li')
                for x in warehouses_list:
                    try:
                        x.find_element(*ProductDetailsLocator.warehouse_tab_link).click()
                    except NoSuchElementException:
                        break

                # select quantity of that product
                self.driver.find_element(*ProductDetailsLocator.product_quantity_dropdown).click()
                time.sleep(1)
                dropdown_values = self.driver.find_element(*ProductDetailsLocator.product_quantity)
                li_list = dropdown_values.find_elements_by_tag_name('li')
                li_list[-1].click()

                # Add to load
                product_name = self.driver.find_element(*ProductDetailsLocator.selected_product_name).text
                self.driver.find_element(*ProductDetailsLocator.add_to_load).click()
                time.sleep(1)
                try:
                    truck_size = self.driver.find_element(*ProductDetailsLocator.truck_types)
                    random.choice(truck_size.find_elements(*ProductDetailsLocator.truck)).click()
                    time.sleep(1)
                except ElementNotVisibleException:
                    pass
                try:
                    self.driver.find_element(*ProductDetailsLocator.confirmation_load).click()
                    time.sleep(1)
                    self.wait_for_element(ProductDetailsLocator.add_to_load_loader)
                except ElementNotVisibleException:
                    pass

                product_basket = self.driver.find_element(*ProductDetailsLocator.added_products)
                list_of_products = product_basket.find_elements(*ProductDetailsLocator.product_single)
                number_of_products = len(list_of_products)
                flag = 0
                for x in range(1,number_of_products+1):
                    pro_name = self.driver.find_element_by_css_selector(
                        '.load-scroll > div:nth-child({0}) > div:nth-child(1) > div:nth-child(2) > h4:nth-child(1)'.format(x)).text
                    if pro_name in product_name:
                        flag = 1
                if flag == 0:
                    print('product not in cart')
                else:
                    print('product was found')
