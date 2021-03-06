
from selenium.webdriver.common.by import By


class SupplierPageLocators(object):
    
#--------------Home page locators--------------#


    signin = (By.CLASS_NAME, 'btn-primary')
    kirv_logo = (By.XPATH, '//img[@alt = "KIRV"]')
    products_link = (By.XPATH, '//*[@id = "main-navigation"]/ul/li[1]')
    customers_link = (By.XPATH, '//*[@id = "main-navigation"]/ul/li[2]')
    orders_link = (By.XPATH, '//*[@id = "main-navigation"]/ul/li[3]')
    input_search_customers = (By.XPATH, '//input[@placeholder="Search Customers"]')
    search_button = (By.XPATH, '//button[text() = "Search"]')
    logout_button = (By.XPATH, '//span[text() = "Logout"]')
    customers_title = (By.CLASS_NAME, 'page-title')
    all_customer_link = (By.XPATH, '//a[text()="All Customers"]//parent::li')
    pending_link = (By.XPATH, '//a[text()="Pending"]//parent::li')
    active_link = (By.XPATH, '//a[text()="Active"]//parent::li')
    inactive_link = (By.XPATH, '//a[text()="Inactive"]//parent::li')
    customer_name = (By.XPATH, '//th[text()="CUSTOMER NAME"]')
    state = (By.XPATH, '//th[text()="STATE"]')
    no_of_locations = (By.XPATH, '//th[text()="NO. OF LOCATION"]')
    main_contact = (By.XPATH, '//th[text()="MAIN CONTACT"]')
    phone_number = (By.XPATH, '//th[text()="PHONE NUMBER"]')
    account_status = (By.XPATH, '//th[text()="ACCOUNT STATUS"]')
    table_body = (By.XPATH, 'html/body/table/tbody')
    table_rows = (By.XPATH, '//tr')
    table_data = (By.XPATH, '//td')
    total_table_records = (By.XPATH, '//quick-filter/div/div[2]/div')
    page_number1 = (By.XPATH, '//a[text()="1"]//parent::li')
    page_number2 = (By.XPATH, '//a[text()="2"]//parent::li')
    page_link = (By.CLASS_NAME, 'page-link')
    search_message = (By.XPATH, '//h3[text()="Contracts Not Found!"]')
    first_record_customer_name = (By.XPATH, '//table/tbody/tr[1]/td[1]')
    first_record_state = (By.XPATH, '//table/tbody/tr/td[2]')
    first_record_no_of_location = (By.XPATH, '//table/tbody/tr/td[3]')
    first_record_main_contact = (By.XPATH, '//table/tbody/tr/td[4]')
    first_record_phone_number = (By.XPATH, '//table/tbody/tr/td[5]')
    first_record_account_status = (By.XPATH, '//table/tbody/tr/td[6]')
    view = (By.XPATH, '//table/tbody/tr/td[8]')
    body = (By.XPATH, '/html/body')
    #chat = (By.XPATH, '//iframe[@id="drift-widget"]')
    chat = (By.TAG_NAME, 'iframe')
    close_chat = (By.XPATH, '//*[@id="root"]/div/div[2]/button')

#--------------Customers page Company Information locators--------------#


    edit_company_information = (By.XPATH, '//fieldset//span[text()="Edit"]')
    company_name_input = (By.XPATH, '//fieldset//input')
    company_address_input = (By.XPATH, '//fieldset/div[2]/div/div[2]//input')
    company_city_input = (By.XPATH, '//fieldset/div[2]/div/div[3]//input')
    company_state_input = (By.XPATH, '//fieldset/div[2]/div/div[4]//input')
    company_post_code_input = (By.XPATH, '//fieldset/div[2]/div/div[5]//input')
    company_reseller_id_input = (By.XPATH, '//fieldset/div[2]/div/div[7]//input')
    company_account_no_input = (By.XPATH, '//fieldset/div[2]/div/div[8]//input')
    company_phone_input = (By.XPATH, '//fieldset/div[2]/div/div[9]//input')
    company_other_phone_input = (By.XPATH, '//fieldset/div[2]/div/div[10]//input')
    company_email_input = (By.XPATH, '//fieldset/div[2]/div/div[11]//input')
    company_website_input = (By.XPATH, '//fieldset/div[2]/div/div[12]//input')
    company_cancel_button = (By.XPATH, '//fieldset//button[text()="Cancel"]')
    company_save_button = (By.XPATH, '//fieldset//button[text()="Save"]')
    company_name_error = (By.XPATH, '//fieldset/div[2]/div/div/field/div')
    company_address_error = (By.XPATH, '//fieldset/div[2]/div/div[2]/field/div')
    company_city_error = (By.XPATH, '//fieldset/div[2]/div/div[3]/field/div')
    company_state_error = (By.XPATH, '//fieldset/div[2]/div/div[4]/field/div')
    company_post_code_error = (By.XPATH, '//fieldset/div[2]/div/div[5]/field/div')
    company_reseller_id_error = (By.XPATH, '//fieldset/div[2]/div/div[7]/field/div')
    company_account_no_error = (By.XPATH, '//fieldset/div[2]/div/div[8]/field/div')
    company_phone_error = (By.XPATH, '//fieldset/div[2]/div/div[9]/field/div')
    company_other_phone_error = (By.XPATH, '//fieldset/div[2]/div/div[10]/field/div')
    company_email_error = (By.XPATH, '//fieldset/div[2]/div/div[11]/field/div')
    company_website_error = (By.XPATH, '//fieldset/div[2]/div/div[12]/field/div')
    success_popup = (By.XPATH, '//toastr/div')
    error_popup = (By.XPATH, '//toastr/div')

    
    #--------------Customer page Contact Information locators--------------#


    edit_contact_information = (By.XPATH, '//span[text()="Contact Information"]//ancestor::fieldset/div/div[2]/span')
    contact_name_input = (By.XPATH, '//span[text()="Contact Information"]//ancestor::fieldset/div[2]/div/div//input')
    contact_phone_input = (By.XPATH, '//span[text()="Contact Information"]//ancestor::fieldset/div[2]/div/div[2]//input')
    contact_email_input = (By.XPATH, '//span[text()="Contact Information"]//ancestor::fieldset/div[2]/div/div[3]//input')
    contact_cancel_button = (By.XPATH, '//div/div[2]/form//button[text()="Cancel"]')
    contact_save_button = (By.XPATH, '//div/div[2]/form//button[text()="Save"]')
    
    contact_name_error = (By.XPATH, '//span[text()="Contact Information"]//ancestor::fieldset/div[2]/div/div/field/div')
    contact_phone_error = (By.XPATH, '//span[text()="Contact Information"]//ancestor::fieldset/div[2]/div/div[2]/field/div')
    contact_email_error = (By.XPATH, '//span[text()="Contact Information"]//ancestor::fieldset/div[2]/div/div[3]/field/div')


    #--------------Customer page Location Information locators--------------#


    edit_location_information = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div/div[2]/span')
    location_name1_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div//input')
    location_address1_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div[2]//input')
    location_city1_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div[3]//input')
    location_state1_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div[4]//input')
    location_post_code1_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div[5]//input')
    location_email1_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div[7]//input')
    location_phone1_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div[8]//input')
    location_name2_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div//input')
    location_address2_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div[2]//input')
    location_city2_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div[3]//input')
    location_state2_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div[4]//input')
    location_post_code2_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div[5]//input')
    location_email2_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div[7]//input')
    location_phone2_input = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div[8]//input')
    location_cancel_button = (By.XPATH, '//div/div[3]/form//button[text()="Cancel"]')
    location_save_button = (By.XPATH, '//div/div[3]/form//button[text()="Save"]')

    location_name1_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div/field/div')
    location_address1_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div[2]/field/div')
    location_city1_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div[3]/field/div')
    location_state1_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div[4]/field/div')
    location_post_code1_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div[5]/field/div')
    location_email1_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div[7]/field/div')
    location_phone1_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[2]/div[8]/field/div')
    location_name2_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div/field/div')
    location_address2_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div[2]/field/div')
    location_city2_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div[3]/field/div')
    location_state2_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div[4]/field/div')
    location_post_code2_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div[5]/field/div')
    location_email2_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div[7]/field/div')
    location_phone2_error = (By.XPATH, '//span[text()="Store Locations"]//ancestor::fieldset/div[2]/div[4]/div[8]/field/div')


    #--------------Customer page Shipping Information locators--------------#


    shipping_div = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::form//parent::div')
    edit_ship_information = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div/div[2]/span')
    ship_name1_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div//input')
    ship_address1_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[2]//input')
    ship_city1_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[3]//input')
    ship_state1_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[4]//input')
    ship_post_code1_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[5]//input')
    ship_email1_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[7]//input')
    ship_phone1_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[8]//input')
    ship_start_time1_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[9]//input')
    ship_end_time1_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[10]//input')
    ship_name2_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div//input')
    ship_address2_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[2]//input')
    ship_city2_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[3]//input')
    ship_state2_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[4]//input')
    ship_post_code2_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[5]//input')
    ship_email2_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[7]//input')
    ship_phone2_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[8]//input')
    ship_start_time2_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[9]//input')
    ship_end_time2_input = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[10]//input')
    ship_cancel_button = (By.XPATH, '//div/div[4]/form//button[text()="Cancel"]')
    ship_save_button = (By.XPATH, '//div/div[4]/form//button[text()="Save"]')
    ship_name1_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div/field/div')
    ship_address1_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[2]/field/div')
    ship_city1_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[3]/field/div')
    ship_state1_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[4]/field/div')
    ship_post_code1_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[5]/field/div')
    ship_email1_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[7]/field/div')
    ship_phone1_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[8]/field/div')
    ship_start_time1_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[9]/field/div')
    ship_end_time1_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[2]/div[10]/field/div')
    ship_name2_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div/field/div')
    ship_address2_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[2]/field/div')
    ship_city2_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[3]/field/div')
    ship_state2_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[4]/field/div')
    ship_post_code2_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[5]/field/div')
    ship_email2_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[7]/field/div')
    ship_phone2_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[8]/field/div')
    ship_start_time2_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[9]/field/div')
    ship_end_time2_error = (By.XPATH, '//span[text()="Warehouse/Ship To Locations"]//ancestor::fieldset/div[2]/div[4]/div[10]/field/div')


    #--------------Customer page Categories Information locators--------------#


    categories_div = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::form//parent::div')
    edit_categories_information = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div/div[2]/span')
    categories_microwave = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[2]/div//input')


    #categories_oven = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[2]/div[2]//input')


    categories_hood = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[2]/div[2]//input')
    categories_stove = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[2]/div[3]//input')
    categories_dishwasher = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[4]/div//input')
    categories_washer = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[6]/div//input')
    categories_pedestal = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[6]/div[2]//input')
    categories_combo = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[6]/div[3]//input')
    categories_dryer = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[6]/div[4]//input')
    categories_garbage_cabinet = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[8]/div//input')
    categories_compactor = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[8]/div[2]//input')
    categories_icemaker = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[10]/div//input')
    categories_freezer = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[10]/div[2]//input')
    categories_refrigerator = (By.XPATH, '//span[text()=" Buying Categories"]//ancestor::fieldset/div[2]/div[10]/div[3]//input')
    categories_cancel_button = (By.XPATH, '//div/div[5]/form//button[text()="Cancel"]')
    categories_save_button = (By.XPATH, '//div/div[5]/form//button[text()="Save"]')


    #--------------Customer page Volume Information locators--------------#


    volume_div = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::form//parent::div')
    edit_volume_information = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div/div[2]/span')
    volume_q1_quarter_trucks = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div[2]/div/div/div//input')
    volume_q1_half_trucks = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div[2]/div/div/div[2]//input')
    volume_q1_full_trucks = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div[2]/div/div/div[3]//input')
    volume_q2_quarter_trucks = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div[2]/div/div[2]/div//input')
    volume_q2_half_trucks = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div[2]/div/div[2]/div[2]//input')
    volume_q2_full_trucks = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div[2]/div/div[2]/div[3]//input')
    volume_q3_quarter_trucks = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div[2]/div/div[3]/div//input')
    volume_q3_half_trucks = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div[2]/div/div[3]/div[2]//input')
    volume_q3_full_trucks = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div[2]/div/div[3]/div[3]//input')
    volume_q4_quarter_trucks = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div[2]/div/div[4]/div//input')
    volume_q4_half_trucks = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div[2]/div/div[4]/div[2]//input')
    volume_q4_full_trucks = (By.XPATH, '//span[text()="Buying Volumes"]//ancestor::fieldset/div[2]/div/div[4]/div[3]//input')
    volume_cancel_button = (By.XPATH, '//div/div[6]/form//button[text()="Cancel"]')
    volume_save_button = (By.XPATH, '//div/div[6]/form//button[text()="Save"]')
