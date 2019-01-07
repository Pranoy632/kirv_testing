import random

from pages.basepage import *
from locators.buyer_locators.homepage_locators import HomePageLocators, AllProductsLocators


class BuildLoad(BasePage):

    def go_to_categories(self):
        self.driver.find_element(*HomePageLocators.categories_link).click()
        self.wait_for_element(HomePageLocators.category_dropdpwn)
        time.sleep(2)

    def select_any_category(self):
        categories = self.driver.find_element(
            *HomePageLocators.total_categories)
        categories_list = categories.find_elements(
            *HomePageLocators.single_category)
        random_category = random.choice(categories_list)
        selected_category_name = random_category.find_element(
            *HomePageLocators.category_name).text
        selected_category_count = random_category.find_element(
            *HomePageLocators.no_of_products_categories_list).text
        random_category.click()
        time.sleep(1)
        self.wait_for_element(HomePageLocators.cart)
        return selected_category_name, selected_category_count

    def check_panel(self):
        category_name = self.driver.find_element(
            *AllProductsLocators.panel_title).text
        category_total = self.driver.find_element(
            *AllProductsLocators.panel_no_of_products).text
        return category_name, category_total

    def check_breadcrumb(self):
        breadcrumb = self.driver.find_element(*AllProductsLocators.breadcrumb)
        total_breadcrumbs = breadcrumb.find_elements(
            *AllProductsLocators.breadcrumb_links_total)
        links = []
        for single_breadcrumb in total_breadcrumbs:
            links.append(single_breadcrumb.text)
        expected_output = ' / '.join(links)
        print(expected_output)

    def total_of_sub_categories(self):
        all_menus = self.driver.find_element(*AllProductsLocators.page_menu)
        menu_list = all_menus.find_elements(*AllProductsLocators.all_menus)
        link_total = []
        for menu in menu_list[1:]:
            menu.click()
            self.wait_for_element(AllProductsLocators.sorting_by_warehouse)
            time.sleep(1)
            link_total.append(self.driver.find_element(
                *AllProductsLocators.panel_no_of_products).text)
        total = sum(link_total)
        print(total)
        return total

    def click_on_sort_by_price(self):
        self.driver.find_element(*AllProductsLocators.sorting_by_price).click()

    def sort_by_higher(self):
        self.driver.find_element(*AllProductsLocators.sort_higher).click()
        time.sleep(1)

    def sort_by_lower(self):
        self.driver.find_element(*AllProductsLocators.sort_lower).click()
        time.sleep(1)

    def apply_sorting(self):
        self.driver.find_element(
            *AllProductsLocators.sort_apply_button).click()
        self.wait_for_element(*AllProductsLocators.loader)
        self.wait_for_element(AllProductsLocators.product_column)

    def get_price(self):
        product_matrix = self.driver.find_element(
            *AllProductsLocators.product_column)
        all_products = product_matrix.find_elements(
            *AllProductsLocators.product_cell_price)
        return all_products

    def check_higher_sorting(self):
        all_products = self.get_price()
        return all(all_products[i].text <= all_products[i + 1].text for i in range(len(all_products) - 1))

    def check_lower_sorting(self):
        all_products = self.get_price()
        return all(all_products[i].text >= all_products[i + 1].text for i in range(len(all_products) - 1))
