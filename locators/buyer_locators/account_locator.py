from selenium.webdriver.common.by import By


class AccountLocators(object):

    account_link = (By.XPATH, '//ul[@class="navbar-nav-right"]')
    my_account_title = (By.XPATH, '//h2[@class="page-title"]')


class UserProfileLocators(object):
    sub_navbar_link = (By.XPATH, '//ul[@class="sub-navigation"]')
    customer_profile_title = (By.XPATH, '//h4[@class="section-title"]')
    customer_pro_edit_btn = (By.XPATH, '//span[@class="edit-but"]')
    full_name = (By.XPATH, '//input[@placeholder="Enter Full Name"]')
    full_name_err = (
        By.XPATH, '//label [input[@placeholder="Enter Full Name"]]/following-sibling::span[@class="error-detail"]')
    cust_pro_save_btn = (By.XPATH, '//button[text()="Save"]')
    cust_pro_cancel_btn = (By.XPATH, '//button[text()="Cancel"]')
    email = (By.XPATH, '//input[@placeholder="Enter Email"]')
    email_err = (
        By.XPATH, '//label [input[@placeholder="Enter Email"]]/following-sibling::span[@class="error-detail"]')
    phone = (By.XPATH, '//input[@placeholder="Enter Phone"]')
    phone_err = (
        By.XPATH, '//label [input[@placeholder="Enter Phone"]]/following-sibling::span[@class="error-detail"]')
    other_phone = (By.XPATH, '//input[@placeholder="Enter Other Phone"]')
    other_phn_err = (
        By.XPATH, '//label [input[@placeholder="Enter Other Phone"]]/following-sibling::span[@class="error-detail"]')


class BrandLocators(object):
    brand_img = (By.XPATH, '//div[contains(@class, "brand-logos")]/img')
