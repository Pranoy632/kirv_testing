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
        By.XPATH, '(//p[contains(@class, "panel-dicd")])[2]')
    signup_to_buy_btn = (By.XPATH, '//a[text() = "Sign up to buy from us"]')


class CreateAccountLocators(object):

    create_account_title = (By.XPATH, '//div[contains(@class, "step-title")]')

    set_credentials_para = (By.XPATH, '//p[@class="short-note"]')

    already_account_link = (
        By.XPATH, '//a[text()=" Already have an account?"]')

    email_input = (
        By.XPATH, '//span[text()=" Email address*"]//following-sibling::input')

    password_input = (
        By.XPATH, '//span[text()=" Create a password*"]//following-sibling::input')

    email_err = (
        By.XPATH, '//label [span[text()=" Email address*"]]//following-sibling::span[@class="error-detail"]')

    password_err = (
        By.XPATH, '//label [span[text()=" Create a password*"]]//following-sibling::span[@class="error-detail"]')

    confirm_btn = (By.XPATH, '//button[text()="Confirm"]')


class ContactInfoLocators(object):

    tell_us_about_para = (By.XPATH, '//p[@class="signup-note"]')

    comapany_name_input = (
        By.XPATH, '//label [span[text()=" Company Name *"]]//following-sibling::input')

    comapany_name_err = (
        By.XPATH, '//label [span[text() = " Company Name *"]]//following-sibling::span[@class="error-detail"]')

    contact_name_input = (
        By.XPATH, '//label [span[text()=" Contact Name *"]]//following-sibling::input')

    contact_name_err = (
        By.XPATH, '//label [span[text() = " Contact Name *"]]//following-sibling::span[@class="error-detail"]')

    phone_input = (
        By.XPATH, '//label [span[text()=" Phone *"]]//following-sibling::input')

    phone_err = (
        By.XPATH, '//label [span[text() = " Phone *"]]//following-sibling::span[@class="error-detail"]')

    create_account_button = (By.XPATH, '//button[text()="Create account"]')

    quit_sign_up = (By.XPATH, '//div[text()="Quit sign up"]')


class CompanyInfoLocators(object):
    pass
