import time
from pages.basepage import BasePage
from locators.supplier_locators.admin_order_locators import Admin_Locators
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys


mode_of_payment = ["Net-30","Net-5","Wire","Credit Card"]
table_header = ['SOURCE','ORDER NUMBER','TOTAL','ORDER DATE','SHIP DATE','BUYER/CUSTOMER','TERMS','ORDER STATUS']
pending_table_header = ["SOURCE","CREATED ON","BUYER","SHIP FROM","SHIP TO","STATUS"]
home_page_tab = ['Products','Customers','Orders']
order_home_page_tab = ['New','Pending','Released','Shipped']


class HomePage(BasePage):

    def check_for_kirv_image(self):
        kirv_logo_image = self.driver.find_element(*Admin_Locators.kirv_logo)
        try:
            kirv_logo_image.is_displayed()
            print("Success -> kirv image displayed")
        except:
            print("Error -> kirv image is not displayed")
        return


    def order_title_displayed(self):
        ord_title = self.driver.find_element(*Admin_Locators.order_title)
        try:
            assert(ord_title.is_displayed())
            print("Success -> order title is display")
        except:
            print("Error -> order title is missing")
        return 1


    def check_for_logout(self):
        logout_btn = self.driver.find_element(*Admin_Locators.logout_in_order)
        try:
            logout_btn.is_enabled()
            print("Success -> logout is clickable")
        except:
            print("Error -> logout button is missing")
        return

    def admin_home_page(self, tab_list):
        tab = tab_list.find_elements_by_tag_name("li")
        return tab

    def list_of_pagination(self):
        pagination = self.driver.find_element(*Admin_Locators.pagination_in_order_page)
        list_of_element_of_pagination = pagination.find_elements_by_tag_name("li")
        return list_of_element_of_pagination


    def check_for_tab(self,list_of_tab,home_page_tab):
        index_of_list_of_tab = 0
        for tab in list_of_tab:
            if tab.text == home_page_tab[index_of_list_of_tab]:
                    index_of_list_of_tab += 1
        try:
            assert(index_of_list_of_tab==len(list_of_tab))
            print("Success -> All Tab Is Visible")
        except:
            print("Error -> Tab Field Are Missing")
        return 1

    def order_tab_is_clickable(self):
        order = self.driver.find_element(*Admin_Locators.orderLocator)
        try:
            assert(order.is_enabled)
            order.click()
            order_is_active = self.driver.find_element(*Admin_Locators.order_active)
            order_is_selected = order_is_active.get_attribute("class")
            assert("active" in order_is_selected.split())
            print("Success -> order element is clickable")
            return 1
        except:
            print("Error -> order element is not clickable")


    def check_home_page(self,tab_list,homePageTab):
        try:
            self.check_for_kirv_image()
            self.check_for_logout()
            self.check_for_tab(tab_list,homePageTab)
            print("Success -> all element in homepage")
        except:
            print("Error -> element missing in homepage")
        return 1

    def check_admin_home_page(self):
        tab_list = self.driver.find_element(*Admin_Locators.home_page_tab)
        list_of_tab = self.admin_home_page(tab_list)
        self.check_home_page(list_of_tab,home_page_tab)
        return 1


    def check_number_order(self,num_of_oder_locator):
        try:
            out_of_order = num_of_oder_locator.split()
            order_name = out_of_order[len(out_of_order)-1]
            total_number_of_order = out_of_order[len(out_of_order)-2]
            if(len(out_of_order) > 2):
                assert(total_number_of_order!=0)
                nth_order = out_of_order[0].split("-")[0]
                no_of_order = out_of_order[0].split("-")[1]
                print("Success -> found order out of total no. of order")
                return order_name,nth_order,no_of_order,total_number_of_order
            else:
                print("Success -> zero order found")
                return order_name,"-1","-1",total_number_of_order
        except:
            print("order out of total no. of order not found")

    def send_keys_to_element(self,element_to_send_keys,element_id):
        try:
            assert(element_to_send_keys.is_enabled())
            element_to_send_keys.click()
            element_to_send_keys.send_keys(element_id)
            element_to_send_keys.send_keys(Keys.ENTER)
        except:
            print("search is not found")
            return

    def cancel_search(self):
        cancel_search = self.driver.find_element(*Admin_Locators.cancel_Back_search)
        assert(cancel_search.is_enabled())
        cancel_search.click()
        return 1

    def check_for_table(self):
        table_header = self.driver.find_elements(*Admin_Locators.table_header)
        table_row = self.driver.find_elements(*Admin_Locators.table_row)
        header_count = len(table_header)
        table_row_count = len(table_row)
        return header_count,table_row_count,table_header,table_row
  
    def check_table_header(self,header_element,header_count,status_tab):
        list_index = 0
        if(status_tab==order_home_page_tab[1]):
            header_list = pending_table_header
        else:
            header_list = table_header
        try:
            for header in header_element:
                if(header.text==header_list[list_index]):
                    list_index = list_index + 1
            assert(header_count == list_index)
            print("Success -> All header are correct")
            return 1
        except:
            print("Error -> headers are missing")
        return

    def check_for_table_content_in_new(self,table_row,status_tab):
        try:
            for row in table_row:
                cell = row.find_elements_by_tag_name('td')
                assert(cell[0].text=="kirv")
                assert(cell[6].text in mode_of_payment)
                assert(cell[7].text==status_tab)
                if(status_tab==order_home_page_tab[3]):
                    assert(cell[8].text == "View")
                else:
                    assert(cell[8].text=="View keyboard_arrow_down")
            print("Success -> All field are correct in table")
            return 1
        except:
            print("Error -> Field are missing from table")
    
    def check_for_table_content_in_pending(self,table_row,status_tab):
        try:
            for row in table_row:
                cell = row.find_elements_by_tag_name('td')
                if(len(cell)!=0):
                    cell_list = map(lambda x : x.text,cell)
                    cell_list = list(cell_list)
                    assert(cell_list[0]=="Kirv")
                    assert(cell_list[-1]=="View keyboard_arrow_down")
            print("Success -> All field are correct in table")
            return 1
        except:
            print("Error -> Field are missing from table")
        return

    def search_in_orders(self,search_key):
        search_text = self.driver.find_element(*Admin_Locators.search_in_new)
        search_text.click()
        search_text.send_keys(search_key)
        search_text.send_keys(Keys.ENTER)
        assert(self.cancel_search())
        return 1


    def get_page_end(self):
        #action = action_chains.ActionChains(self.driver)
        #action.send_keys(Keys.END)
        #self.close_chat_popup()
        web_page = self.driver.find_element(*Admin_Locators.whole_page)
        web_page.send_keys(Keys.END)
        #action.perform()
        return

    def get_page_at_begining(self):
        web_page = self.driver.find_element(*Admin_Locators.whole_page)
        web_page.send_keys(Keys.HOME)
        return


    def check_for_pagination(self,total_no_of_order):
        pages = 0 if total_no_of_order == 0 else int(total_no_of_order / 50) if (total_no_of_order % 50 == 0) else (int(total_no_of_order / 50)+1)
        if(pages == 0):
            message = self.driver.find_element(*Admin_Locators.new_error_msg)
            error_msg = message.text
            assert(message.is_displayed())
            assert(error_msg == "Orders Not Found!")
        else:
            pagination_list = self.list_of_pagination()
            pagination_root = self.driver.find_element(*Admin_Locators.pagination)
            assert(pages > 1)
            self.get_page_end()
            assert(self.driver.find_element(*Admin_Locators.pagination).is_displayed())
            page_index = 1
            self.get_page_at_begining()
            time.sleep(3)
            for page in pagination_list:
                assert(page.text==str(page_index))
                assert(page.is_enabled())
                if("active" in page.get_attribute("class").split()):
                    assert("active" in page.get_attribute("class").split())
                else:
                    assert(self.driver.find_element(*Admin_Locators.pagination).is_displayed())
                    assert(page.is_enabled())
                    page.click()
                    #assert("active" in page.get_attribute("class").split())
                    time.sleep(3)
                page_index += 1
        return 1

    def check_table(self,status_tab):
            header_count,table_row_count,table_header,table_row = self.check_for_table()
            if(status_tab == order_home_page_tab[0] or status_tab == order_home_page_tab[2] or status_tab == order_home_page_tab[3]):
                assert(self.check_table_header(table_header,header_count,status_tab)==1)
                assert(self.check_for_table_content_in_new(table_row,status_tab)==1)
            elif(status_tab == order_home_page_tab[1]):
                assert(self.check_table_header(table_header,header_count,status_tab)==1)
                assert(self.check_for_table_content_in_pending(table_row,status_tab)==1)
            return 1

    def check_for_table_in_order(self,status_tab):
        num_of_oder_locator = self.driver.find_element(*Admin_Locators.order_out_of_total_order).text
        order_name,nth_order,no_of_order,total_no_of_order = self.check_number_order(num_of_oder_locator)
        try:
            if(int(total_no_of_order) == 0):
                message = self.driver.find_element(*Admin_Locators.new_error_msg)
                error_msg = message.text
                assert(message.is_displayed())
                assert(error_msg == "Orders Not Found!")
                print("Success -> displaying expected message ",error_msg)
            elif(int(total_no_of_order) < 50):
                header_count,table_row_count,table_header,table_row = self.check_for_table()
                assert(total_no_of_order == no_of_order)
                assert(int(nth_order) == 1)
                if(status_tab==order_home_page_tab[1]):
                    table_row_count = table_row_count - 1
                assert(table_row_count == int(no_of_order))
                self.check_table(status_tab)
            else:
                header_count,table_row_count,table_header,table_row = self.check_for_table()
                self.check_table(status_tab)
                self.check_for_pagination(int(total_no_of_order))
            print("Success -> Table data are valid")
            return 1
        except:
            print("Error -> Table data are Invalid")


    def get_attribute_by_tab_name(self,tab_is_active):
        return tab_is_active.get_attribute("class")


    def test_cases_for_order_tab(self,status_tab,tab_name,status,total_order,search_key,table_records_name):
        try:
            if(int(total_order) != 0):
                assert(self.search_in_orders(search_key))
            assert(tab_name == status_tab)
            assert(status == "active")
            assert(self.order_title_displayed())
            assert(table_records_name == "Orders")
            self.check_for_table_in_order(status_tab)
            print("Success` -> tab ",status_tab)
        except:
            print("Error -> tab ",status_tab)

    def check_all_tab_functinality(self,status_tab):
        num_of_oder_locator = self.driver.find_element(*Admin_Locators.order_out_of_total_order).text
        order_name,nth_order,no_of_order,total_no_of_order = self.check_number_order(num_of_oder_locator)
        if(status_tab == order_home_page_tab[0]):
            tab_name = self.driver.find_element(*Admin_Locators.new)
            status_tab_text = tab_name.text
            tab_name.click()
            tab_status = self.driver.find_element(*Admin_Locators.new_is_active)
            search_key = self.driver.find_element(*Admin_Locators.get_first_order_num).text
        elif(status_tab == order_home_page_tab[1]):
            tab_name = self.driver.find_element(*Admin_Locators.pending)
            status_tab_text = tab_name.text
            tab_name.click()
            tab_status = self.driver.find_element(*Admin_Locators.pending_is_active)
            search_key = self.driver.find_element(*Admin_Locators.get_first_order_buyer_name).text
        elif(status_tab == order_home_page_tab[2]):
            tab_name = self.driver.find_element(*Admin_Locators.release)
            status_tab_text = tab_name.text
            tab_name.click()
            tab_status = self.driver.find_element(*Admin_Locators.release_is_active)
            search_key = self.driver.find_element(*Admin_Locators.get_first_order_num).text
        elif(status_tab == order_home_page_tab[3]):
            tab_name = self.driver.find_element(*Admin_Locators.ship)
            status_tab_text = tab_name.text
            tab_name.click()
            tab_status = self.driver.find_element(*Admin_Locators.ship_is_active)
            search_key = self.driver.find_element(*Admin_Locators.get_first_order_num).text
        else:
            print("Invalid page")
            return
        tab_is_active = self.get_attribute_by_tab_name(tab_status)
        self.test_cases_for_order_tab(status_tab,status_tab_text,tab_is_active,total_no_of_order,search_key,order_name)
        return



    def check_for_order_homepage(self):
        assert(self.order_tab_is_clickable())
        order_tabs = self.driver.find_element(*Admin_Locators.order_homepage_tab)
        order_list_of_tab = self.admin_home_page(order_tabs)
        assert(self.check_for_tab(order_list_of_tab,order_home_page_tab)==1)
        for tab in order_home_page_tab:
            self.check_all_tab_functinality(tab)






