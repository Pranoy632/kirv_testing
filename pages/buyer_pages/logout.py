from pages.basepage import *
from locators.buyer_locators.logout_locator import LogoutLocator


class Logout(BasePage):

    def navbar_list(self):
        self.wait_for_element(LogoutLocator.logout_link)
        navbar_right = self.driver.find_element(*LogoutLocator.logout_link)
        navbar_li = navbar_right.find_elements_by_tag_name("li")
        return navbar_li

    def go_to_logout(self):
        list_li = self.navbar_list()
        for item in list_li:
            if item.text == 'Logout':
                item.click()
                print("Success: %s is clicked." % (item.text))
                self.check_logout_active()

    def check_logout_active(self):
        li_active = self.navbar_list()
        for active_item in li_active:
            is_active = "active" in active_item.get_attribute("class")
            if is_active:
                if active_item.text == 'Logout':
                    print("Success: %s is active." % (active_item.text))
