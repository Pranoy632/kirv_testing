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
    step_kirv_logo = (
        By.XPATH, '//div[contains(@class, "text-center")] / img[@class = "logo"]')

    steps = (By.XPATH, '//div[contains(@class, "signup-steps text-center")]')

    welcome_title = (By.XPATH, '//div[@class = "step-title"]')

    company_signup_note_para = (By.XPATH, '//p[@class="signup-note"]')

    address_input = (
        By.XPATH, '//label/span[text()=" Address line 1*"]//following-sibling::input')

    unit_num_input = (
        By.XPATH, '//label/span[text()=" Unit Number"]//following-sibling::input')

    city_input = (
        By.XPATH, '//label/span[text()=" City*"]//following-sibling::input')

    state_input = (
        By.XPATH, '//label/span[text()=" State*"]//following-sibling::div/input')

    zip_code_input = (
        By.XPATH, '//label/span[text()=" Zip code*"]//following-sibling::input')

    reseller_id_input = (
        By.XPATH, '//label/span[text()=" Reseller ID*"]//following-sibling::input')

    company_website_input = (
        By.XPATH, '//label/span[text()=" Company website*"]//following-sibling::input')

    email_input = (
        By.XPATH, '//label/span[text()=" Email*"]//following-sibling::input')

    phone_number = (
        By.XPATH, '//label/span[text()=" Phone number*"]//following-sibling::input')

    continue_btn = (By.XPATH, '//button[contains(text(), "Continue")]')


class LocationLocators(object):

    location_num = (By.XPATH, '//label[1]/span[text()="1"]')

    enter_manually = (By.XPATH, '//a[text()="Enter address manually"]')

    loc_name_input = (
        By.XPATH, '//label/span[text()=" Location name *"]//following-sibling::input')

    address_input = (
        By.XPATH, '//label/span[text()=" Address line 1*"]//following-sibling::input')

    city_input = (
        By.XPATH, '//label/span[text()=" City*"]//following-sibling::input')

    state_input = (
        By.XPATH, '//label/span[text()=" State *"]//following-sibling::div/input')

    zip_code_input = (
        By.XPATH, '//label/span[text()=" Zip code*"]//following-sibling::input')

    add_loc_btn = (By.XPATH, '//button[text()="Add location"]')

    email_address_input = (
        By.XPATH, '//label/span[text()=" Location email address*"]//following-sibling::input')

    phone_number_input = (
        By.XPATH, '//label/span[text()=" Location phone number*"]//following-sibling::input')

    next_btn = (By.XPATH, '//button[text()="Next"]')


class WareHouseLocators(object):

    check_retail_locartion = (By.XPATH, '//label[text()="test city"]')

    confirm_btn = (By.XPATH, '//button[text()="Confirm"]')

    no_additional_warehouse_btn = (
        By.XPATH, '//span[text()="No additional warehouses"]')


class CategoriesLocators(object):

    often_purchase_title = (By.XPATH, '//div[contains(@class, "step-title")]')

    categories_step = (
        By.XPATH, '//div[contains(text(), "Step 4 of 5 - Purchasing preferences")]')

    categories_title = (By.XPATH, '//ul[@class="categories-title"]')

    categories_ul = (By.XPATH, '//ul[@class="categories-ul"]')


class VolumesLocators(object):

    volume_step = (
        By.XPATH, '//div[contains(text(), "Step 5 of 5 - Purchasing volumes")]')

    volumes_title = (By.XPATH, '//div[contains(@class, "step-title")]')

    headers = (By.XPATH, '//h3')

    trucks_list = (
        By.XPATH, '//h3/following-sibling::div/div[contains(@class, "row")]')

    plus_btn = (
        By.XPATH, '//h3/following-sibling::div/div/div[2]/div/button[2]')
