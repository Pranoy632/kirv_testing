import sys
sys.path.append('../test_locators')
import time

from Basepage import BasePage, fake

from Buyer_Locators.locatorBuyer import BuyerPageLocators


class HeaderPage(BasePage):

    def check_img_labels(self):

        self.wait_for_element(BuyerPageLocators.kirv_image)

        kirv_img = self.driver.find_element(
            *BuyerPageLocators.kirv_image)

        try:
            assert kirv_img.is_displayed() == True
            print("Success: header kirv-image found.")
        except:
            print("No result found for kirv-image")

        label_categories = self.driver.find_element(
            *BuyerPageLocators.categories_label)

        try:
            assert label_categories.is_displayed() == True
            print("Success: header categories label found.")
        except:
            print("No result found for categories label.")

        label_brand = self.driver.find_element(
            *BuyerPageLocators.brand_label)

        try:
            assert label_brand.is_displayed() == True
            print("Success: header brand label found.")
        except:
            print("No result found for brand label.")

        input_search = self.driver.find_element(
            *BuyerPageLocators.search_input)

        try:
            assert input_search.is_displayed() == True
            print("Success: header search-input found.")
        except:
            print("No result found for search-input label.")

        btn_search = self.driver.find_element(
            *BuyerPageLocators.search_btn)

        try:
            assert btn_search.is_displayed() == True
            print("Success: header  search-button found.")
        except:
            print("No result found for search-button label.")

        label_load = self.driver.find_element(
            *BuyerPageLocators.load_label)

        try:
            assert label_load.is_displayed() == True
            print("Success: header load label found.")
        except:
            print("No result found for load label.")

        circle_pop_load = self.driver.find_element(
            *BuyerPageLocators.load_circle_pop)

        try:
            assert circle_pop_load.is_displayed() == True
            print("Success: header circle_pop_load  found.")
        except:
            print("No result found for circle_pop_load.")

        label_favourites = self.driver.find_element(
            *BuyerPageLocators.favourites_label)

        try:
            assert label_favourites.is_displayed() == True
            print("Success: header favourites label  found.")
        except:
            print("No result found for favourites label.")

        label_account = self.driver.find_element(
            *BuyerPageLocators.account_label)

        try:
            assert label_account.is_displayed() == True
            print("Success: header account label  found.")
        except:
            print("No result found for account label.")

        label_logout = self.driver.find_element(
            *BuyerPageLocators.logout_label)

        try:
            assert label_logout.is_displayed() == True
            print("Success: header logout label  found.")
        except:
            print("No result found for logout label.")
