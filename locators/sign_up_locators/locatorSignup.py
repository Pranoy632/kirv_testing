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

    location_num1 = (By.XPATH, '//label[1]/span[text()="1"]')

    location_num2 = (By.XPATH, '//label[2]/span[text()="2"]')

    location_num3 = (By.XPATH, '//label[3]/span[text()="3"]')

    enter_manually = (By.XPATH, '//a[text()="Enter address manually"]')

    loc_name_input = (
        By.XPATH, '//span[contains(text(),"Location name")]//following-sibling::input')

    address_input = (
        By.XPATH, '//span[contains(text(),"Address line 1")]//following-sibling::input')

    unit_no_input = (
        By.XPATH, '//span[contains(text(), "Unit number")]//following-sibling:: input')

    city_input = (
        By.XPATH, '//span[contains(text(),"City")]//following-sibling::input')

    state_input = (
        By.XPATH, '//span[contains(text(),"State")]//following-sibling::div/input')

    zip_code_input = (
        By.XPATH, '//span[contains(text(),"Zip code")]//following-sibling::input')

    add_loc_btn = (By.XPATH, '//button[contains(text(),"Add location")]')

    email_address_input = (
        By.XPATH, '//span[contains(text(),"Location email address")]//following-sibling::input')

    phone_number_input = (
        By.XPATH, '//span[contains(text(),"Location phone number")]//following-sibling::input')

    alt_phone_number_input = (
        By.XPATH, '//span[contains(text(),"Location alt. phone number")]//following-sibling::input')

    loc_name_error = (
        By.XPATH, '//span[contains(text(),"Location name")]//ancestor::div[1]')

    address_error = (
        By.XPATH, '//span[contains(text(),"Address line 1")]//ancestor::div[1]')

    city_error = (
        By.XPATH, '//span[contains(text(),"City")]//ancestor::div[1]')

    state_error = (
        By.XPATH, '//span[contains(text(),"State")]//ancestor::div[1]')

    zip_code_error = (
        By.XPATH, '//span[contains(text(),"Zip code")]//ancestor::div[1]')

    email_address_error = (
        By.XPATH, '//span[contains(text(),"Location email address")]//ancestor::div[1]')

    phone_number_error = (
        By.XPATH, '//span[contains(text(),"Location phone number")]//ancestor::div[1]')

    alt_phone_number_error = (
        By.XPATH, '//span[contains(text(),"Location alt. phone number")]//ancestor::div[1]')

    next_btn = (
        By.XPATH, '//button[contains(text(),"Next")]')

    edit_address_btn = (
        By.XPATH, '//a[text()="Edit address"]')

    update_loc_btn = (
        By.XPATH, '//button[contains(text(),"Update location")]')

    loc_address_input = (
        By.XPATH, '//label[contains(text(), "Location address")]//following-sibling::input')

    loc_address_error = (
        By.XPATH, '//label[contains(text(), "Location address")]//ancestor::div[1]')

    google_map = (
        By.XPATH, '//agm-map/div')

class WareHouseLocators(object):

    check_retail_locartion = (
        By.XPATH, '//label[text()="test city"]')

    check_first_retail_location = (
        By.XPATH, '//h3[text()="Retail location"]//following-sibling::div[1]/label')

    check_second_retail_location = (
        By.XPATH, '//h3[text()="Retail location"]//following-sibling::div[2]/label')

    check_third_retail_location = (
        By.XPATH, '//h3[text()="Retail location"]//following-sibling::div[3]/label')

    check_none_retail_location = (
        By.XPATH, '//label[text()="None of these"]')

    check_first_retail_location_id = (
        By.ID, 'customCheck0')

    check_second_retail_location_id = (
        By.ID, 'customCheck1')

    check_none_retail_location_id = (
        By.ID, 'customCheck_cancel')

    confirm_btn = (
        By.XPATH, '//button[text()="Confirm"]')

    no_additional_warehouse_btn = (
        By.XPATH, '//span[text()="No additional warehouses"]')

    back_a_step = (
        By.XPATH, '//div[contains(text(), "Back a step")]')

    purchasing_preferences = (
        By.XPATH, '//div[contains(text(), "Step 4 of 5 - Purchasing preferences")]')

    warehouse_num1 = (
        By.XPATH, '//span[contains(text(), "1")]')

    warehouse_num2 = (
        By.XPATH, '//span[contains(text(), "2")]')

    warehouse_name_input = (
        By.XPATH, '//span[contains(text(), "Warehouse name")]//following-sibling::input')

    warehouse_address_input = (
            By.XPATH, '//label[contains(text(), "Warehouse address")]//following-sibling::input')

    add_loc_btn = (
        By.XPATH, '//button[contains(text(), "Add location")]')

    warehouse_name_error = (
        By.XPATH, '//span[contains(text(), "Warehouse name")]//ancestor::div[1]')

    warehouse_address_error = (
        By.XPATH, '//label[contains(text(), "Warehouse address")]//ancestor::div[1]')

    manual_address_link = (
        By.XPATH, '//a[contains(text(), "Enter address manually")]')

    lookup_link = (
        By.XPATH, '//a[contains(text(), "Enter by lookup")]')

    google_map = (
        By.XPATH, '//agm-map/div')

    edit_address = (
        By.XPATH, '//a[contains(text(), "Edit address")]')

    update_location_btn = (
        By.XPATH, '//button[contains(text(), "Update location")]')

    warehouse_email_input = (
        By.XPATH, '//span[contains(text(), "Warehouse email address")]//following-sibling::input')

    warehouse_phone_no_input = (
        By.XPATH, '//span[contains(text(), "Warehouse phone number")]//following-sibling::input')

    warehouse_alt_phone_no_input = (
        By.XPATH, '//span[contains(text(), "Warehouse alt. phone number")]//following-sibling::input')

    warehouse_email_error = (
        By.XPATH, '//span[contains(text(), "Warehouse email address")]//ancestor::div[1]')

    warehouse_phone_no_error = (
        By.XPATH, '//span[contains(text(), "Warehouse phone number")]//ancestor::div[1]')

    warehouse_alt_phone_no_error = (
        By.XPATH, '//span[contains(text(), "Warehouse alt. phone number")]//ancestor::div[1]')

    confirm_and_continue_btn = (
        By.XPATH, '//button[contains(text(), "Confirm & Continue")]')

    from_time_btn = (
        By.XPATH, '//span[contains(text(), "From")]//following-sibling::input')

    until_time_btn = (
        By.XPATH, '//span[contains(text(), "Until")]//following-sibling::input')

    from_time = (
        By.XPATH, '//button[contains(text(), "1")]')

    until_time = (
        By.XPATH, '//button[contains(text(), "3")]')

    body = (
        By.XPATH, '//body')

    ok_btn = (
        By.XPATH, '//button[contains(text(), "Ok")]')

    manual_link = (
        By.XPATH, '//a[contains(text(), "Enter address manually")]')

    warehouse_name_input = (
        By.XPATH, '//span[contains(text(), "Warehouse name")]//following-sibling::input')

    warehouse_address_line_input = (
        By.XPATH, '//span[contains(text(), "Address line 1")]//following-sibling::input')

    warehouse_unit_number_input = (
        By.XPATH, '//span[contains(text(), "Unit number")]//following-sibling::input')

    warehouse_city_input = (
        By.XPATH, '//span[contains(text(), "City")]//following-sibling::input')

    warehouse_state_input = (
        By.XPATH, '//span[contains(text(), "State")]//following-sibling::div/input')

    warehouse_zipcode_input = (
        By.XPATH, '//span[contains(text(), "Zip code")]//following-sibling::input')

    warehouse_name_error = (
        By.XPATH, '//span[contains(text(), "Warehouse name")]//ancestor::div[1]')

    warehouse_address_line_error = (
        By.XPATH, '//span[contains(text(), "Address line 1")]//ancestor::div[1]')

    warehouse_unit_number_error = (
        By.XPATH, '//span[contains(text(), "Unit number")]//ancestor::div[1]')

    warehouse_city_error = (
        By.XPATH, '//span[contains(text(), "City")]//ancestor::div[1]')

    warehouse_state_error = (
        By.XPATH, '//span[contains(text(), "State")]//ancestor::div[1]')

    warehouse_zipcode_error = (
        By.XPATH, '//span[contains(text(), "Zip code")]//ancestor::div[1]')
