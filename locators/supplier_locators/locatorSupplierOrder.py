from selenium.webdriver.common.by import By


class OrderPageLocators(object):

    homepege_tabs = (By.XPATH, '//ul[contains(@class, "d-block")]')
    order_title = (By.XPATH, '//div[contains(@class, "page-title")]')
    order_tabs = (By.XPATH, '//ul[contains(@class, "sub-navigation")]')
    new_order_button = (By.XPATH, '(//button)[1]')
    bck_to_all_order_btn = (By.XPATH, '//span[contains(@class, "back-to")]')
    new_order_title = (By.XPATH, '//div[contains(@class, "page-title")]')
    ship_from_input = (
        By.XPATH, '//label[contains(text(), "Ship From")]//following-sibling::field/div/label/div/input')
    customer_input = (
        By.XPATH, '//label[contains(text(), "Customer")]//following-sibling::field/div/label/div/input')
    ship_to_input = (
        By.XPATH, '//label[contains(text(), "Ship To")]//following-sibling::field/div/label/div/input')
    dropdown_list = (
        By.XPATH, '//div[contains(@class, "ng2-auto-complete")]/ul')
