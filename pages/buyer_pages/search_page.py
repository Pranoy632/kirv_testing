import random

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException

from pages.basepage import *
from locators.buyer_locators.homepage_locators import *
from common.check_broken_images import verify_image


class Search(BasePage):

    def search_blank(self):
        self.driver.find_element(*HomePageLocators.search).send_keys(Keys.ENTER)
        try:
            self.wait_for_element(AllProductsLocators.sorting_by_price)
        except TimeoutException:
            print('Not working yet')

    def search_invalid_data(self):
        self.driver.find_element(*HomePageLocators.search).send_keys('qazwsx')
        self.driver.find_element(*HomePageLocators.search_button).click()
        self.wait_for_element(AllProductsLocators.sorting_by_price)

    def find_no_results_page(self):
        no_products_confirmation = self.driver.find_element(*AllProductsLocators.no_products).text
        print(no_products_confirmation)
        return no_products_confirmation

    def get_all_categories(self):
        categories = self.driver.find_element(*HomePageLocators.total_categories)
        categories_list = categories.find_elements(*HomePageLocators.single_category)
        category_displayed = []
        for cat in categories_list:
            category_name = cat.find_element(*HomePageLocators.category_name)
            category_displayed.append(category_name.text)
        print(category_displayed)
        return category_displayed

    def all_brands(self):
        try:
            self.driver.find_element(*HomePageLocators.brands_menu)
            brands_list = self.driver.find_elements(*HomePageLocators.brands_menu_list)
        except NoSuchElementException:
            self.driver.find_element(*HomePageLocators.brands_link).click()
            self.wait_for_element(HomePageLocators.brands_menu)
            time.sleep(3)
            brands_list = self.driver.find_elements(*HomePageLocators.brands_menu_list)
        return brands_list

    def check_brands_menu_images(self):
        brands_list = self.all_brands()

        for brands in brands_list:
            image_element = brands.find_element(*HomePageLocators.brands_images)

            if image_element.get_attribute('src') != '':
                verify_image(image_element)
            else:
                print('src is blank')

    def check_brand_numbers(self):
        brands = self.all_brands()
        selected_brand = random.choice(brands)
        brands_dict = {}
        brand_name = selected_brand.find_element(*HomePageLocators.brand_name).text
        brand_number = selected_brand.find_element(*HomePageLocators.brand_numbers).text
        brand_number = (brand_number.split(' '))[0]
        # brands_dict.update({brand_name: brand_number})
        selected_brand.click()
        self.wait_for_element(ResultsPageLocators.brands_category_page)
        time.sleep(1)
        categories_list = self.driver.find_elements(*ResultsPageLocators.products_rows)
        cat_sum = []
        for category in categories_list:
            no_of_products = ((category.find_element(*HomePageLocators.brand_numbers).text).split(' '))[0]
            cat_sum.append(int(no_of_products))
        print(sum(cat_sum), brand_number)

    def search_brand_name(self):
        brands = self.all_brands()
        selected_brand = random.choice(brands)

        brand_name = selected_brand.find_element(*HomePageLocators.brand_name).text
        brand_number = selected_brand.find_element(*HomePageLocators.brand_numbers).text
        brand_number = (brand_number.split(' '))[0]

        self.driver.find_element(*HomePageLocators.search).clear()
        self.driver.find_element(*HomePageLocators.search).send_keys(brand_name)
        self.driver.find_element(*HomePageLocators.search).send_keys(Keys.ENTER)
        self.wait_for_element(AllProductsLocators.loader)
        self.wait_for_element(AllProductsLocators.sorting_by_price)
        flag = 0
        try:
            all_results = self.driver.find_elements(*AllProductsLocators.product_cell)

            for product_info in all_results:
                print(product_info.text)
                if (brand_name.lower() + ' - ') not in product_info.text.lower():
                    flag = 1
                    break

        except NoSuchElementException:
            self.driver.find_element(*AllProductsLocators.no_products)
            flag = 2

        print(flag, '=flag')
        return flag

    def search_categories_valid(self):
        category_data = self.get_all_categories()
        flag = 0
        for data in category_data:
            print(data)
            self.driver.find_element(*HomePageLocators.search).clear()
            self.driver.find_element(*HomePageLocators.search).send_keys(data)
            self.driver.find_element(*HomePageLocators.search).send_keys(Keys.ENTER)
            time.sleep(5)
            #self.wait_for_element(AllProductsLocators.loader)
            self.wait_for_element(AllProductsLocators.sorting_by_price)
            try:
                all_results = self.driver.find_element(*AllProductsLocators.product_list)
                names_list = all_results.find_elements(*HomePageLocators.category_name)
                for product_name in names_list:
                    print(product_name.text)
                    if data not in product_name.text:
                        flag = 1
                        break
            except NoSuchElementException:
                self.driver.find_element(*AllProductsLocators.no_products)
        return flag
