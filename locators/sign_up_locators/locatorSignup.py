from selenium.webdriver.common.by import By


class SignupPageLocators(object):

    signupLink = (By.XPATH, '//a[text()="Sign up here"]')
    kirv_logo = (
        By.XPATH, '//div[@class="header-new text-center"]/img[@class="logo"]')
    business_looking = (
        By.XPATH, '//div[@class="header-new text-center"]//following-sibling::div[1]')
    cart_plus_icon = (
        By.XPATH, '//h2[text()="I would like to buy remanufactured products from Kirv"]//preceding::img[1]')
    buy_remanufactured_product = (
        By.XPATH, '//h2[text()="I would like to buy remanufactured products from Kirv"]')
    purchase_remanufactured_products_para = (
        By.XPATH, '//p[@class="mb-3 mb-md-5 panel-dicd"]')
    signup_to_buy_btn = (By.XPATH, '//a[text() = "Sign up to buy from us"]')
