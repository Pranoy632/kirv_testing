from pathlib import Path
import csv

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from pages.basepage import *
from locators.buyer_locators.homepage_locators import HomePageLocators,AllProductsLocators


def get_csv_data():
    p = str(Path(__file__).parents[2])

    with open(p + "/test_data/search_parameters.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        categories = []
        for row in csv_reader:
            categories.append(row['categories'])
    categories = list(filter(None, categories))
    print(categories)
    print(type(categories))
    return categories


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

    def search_categories_valid(self):
        category_data = get_csv_data()
        for data in category_data:
            self.driver.find_element(*HomePageLocators.search).clear()
            self.driver.find_element(*HomePageLocators.search).send_keys(data)
            self.driver.find_element(*HomePageLocators.search).send_keys(Keys.ENTER)
            self.wait_for_element(AllProductsLocators.loader)
            self.wait_for_element(AllProductsLocators.sorting_by_price)
