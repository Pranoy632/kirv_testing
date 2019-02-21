import time
import random
from pages.basepage import BasePage
from locators.supplier_locators.locatorSupplierOrder import OrderPageLocators


class OrderPage(BasePage):

    def home_tabs(self):

        self.wait_for_element(OrderPageLocators.homepege_tabs)

        tab_list = self.driver.find_element(*OrderPageLocators.homepege_tabs)
        items = tab_list.find_elements_by_tag_name("li")
        return items

    def tabs_order(self):
        self.wait_for_element(OrderPageLocators.order_tabs)

        order_tab_list = self.driver.find_element(
            *OrderPageLocators.order_tabs)
        li_items = order_tab_list.find_elements_by_tag_name("li")
        return li_items

    def goto_order_tab(self):
        list_li = self.home_tabs()
        for item in list_li:
            if item.text == 'Orders':
                item.click()

    def check_order_active(self):
        item_li = self.home_tabs()
        for item in item_li:
            is_active = "active" in item.get_attribute("class")
            if is_active:
                if item.text == 'Orders':
                    pass
                else:
                    print("Order tab is not active.")

    def check_order_title(self):
        return self.driver.find_element(*OrderPageLocators.order_title).text

    def goto_pending_tab(self):
        order_tabs_li = self.tabs_order()
        for tab_item in range(1, (len(order_tabs_li) + 1)):
            time.sleep(1)
            menus_item = self.driver.find_element_by_css_selector(
                '.sub-navigation > li:nth-child({0})'.format(tab_item))
            if menus_item.text == 'Pending':
                menus_item.click()

    def check_order_tabs_active(self):
        active_tabs_li = self.tabs_order()
        for active_tab in active_tabs_li:
            is_active = "active" in active_tab.get_attribute("class")
            if is_active:
                if active_tab.text == 'Pending':
                    pass
                else:
                    print("Pending tab is not active.")

    def new_order_button_click(self):
        order_btn = self.driver.find_element(
            *OrderPageLocators.new_order_button)
        order_btn.click()

    def check_back_click_title(self):
        self.wait_for_element(OrderPageLocators.bck_to_all_order_btn)
        return self.driver.find_element(*OrderPageLocators.bck_to_all_order_btn).is_displayed()

    def check_new_order_title(self):
        return self.driver.find_element(*OrderPageLocators.new_order_title).text

    def select_dropdown_element(self):
        dropdown_ul = self.driver.find_element(
            *OrderPageLocators.dropdown_list)
        dropdown_items = dropdown_ul.find_elements_by_tag_name("li")
        random.choice(dropdown_items).click()

    def elements_of_order(self):
        self.goto_order_tab()
        self.check_order_active()
        self.goto_pending_tab()
        self.check_order_tabs_active()
        try:
            assert self.check_order_title() == 'Orders'
        except:
            print('No result found for order title.')
        self.new_order_button_click()

        try:
            assert self.check_back_click_title() == True
        except:
            print('No result found back to all title.')

        try:
            assert self.check_new_order_title() == 'New Order'
        except:
            print('No result for new order title.')

        self.driver.find_element(*OrderPageLocators.ship_from_input).click()
        self.select_dropdown_element()

        self.driver.find_element(*OrderPageLocators.customer_input).click()
        self.select_dropdown_element()

        self.driver.find_element(*OrderPageLocators.ship_to_input).click()
        self.select_dropdown_element()
