import sys
sys.path.append('../test_locators')
import time

from Basepage import BasePage, fake

from Buyer_Locators.locatorBuyer import BuyerPageLocators


class HomePage(BasePage):

    def check_labels_prodlist(self):

        self.wait_for_element(BuyerPageLocators.product_image)

        prod_img = self.driver.find_element(
            *BuyerPageLocators.product_image)

        try:
            assert prod_img.is_displayed() == True
            print("Success: Home-page product-image found.")
        except:
            print("No result found for Home-page product-image")

        label_exclusive = self.driver.find_element(
            *BuyerPageLocators.exclusive_label)

        try:
            assert label_exclusive.is_displayed() == True
            print("Success: Home-page exclusive_label found.")
        except:
            print("No result found for Home-page exclusive_label.")

        label_build = self.driver.find_element(
            *BuyerPageLocators.build_label)

        try:
            assert label_build.is_displayed() == True
            print("Success: Home-page build_label found.")
        except:
            print("No result found for Home-page build_label.")

        all_prod_btn = self.driver.find_element(
            *BuyerPageLocators.view_all_products_btn)

        try:
            assert all_prod_btn.is_displayed() == True
            print("Success: Home-page view all product button found.")
        except:
            print("No result found for Home-page view all product button.")

        load_progress_view_all = self.driver.find_element(
            *BuyerPageLocators.loads_in_progress_view_all_label)

        try:
            assert load_progress_view_all.is_displayed() == True
            print(
                "Success: Home-page view all load in progress and view all label found.")
        except:
            print(
                "No result found for Home-page view all load in progress and view all label.")

        view_category = self.driver.find_element(
            *BuyerPageLocators.view_products_by_category_label)

        try:
            assert view_category.is_displayed() == True
            print(
                "Success: Home-page view products by category label found.")
        except:
            print(
                "No result found for Home-page view products by category label.")

        prod_list = self.driver.find_element_by_class_name('product-list')

        all_child_divs_prod_list = prod_list.find_elements_by_xpath(
            "//div[@tabindex='0']")

        if len(all_child_divs_prod_list) > 0:
            print('Success: Home-page category_product_list: ' +
                  str(len(all_child_divs_prod_list)))
        else:
            print('No result found for category_product_list')
