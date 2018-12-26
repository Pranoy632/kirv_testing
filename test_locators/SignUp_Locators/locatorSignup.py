from selenium.webdriver.common.by import By


class SigninPageLocators(object):

    # SignUp

    title_login_signup = (
        By.CSS_SELECTOR, 'ng-component > div > div > div > div > div > div > h1')

    email_login_signup = (
        By.CSS_SELECTOR, 'ng-component > div > div > div > div > form > fieldset > field:nth-child(1) > div > label > input')
    pwd_login_signup = (
        By.CSS_SELECTOR, 'ng-component > div > div > div > div > form > fieldset > field:nth-child(2) > div > label > input')
    email_login_signup_error = (
        By.CSS_SELECTOR, 'ng-component > div > div > div > div > form > fieldset > field:nth-child(1) > div > span')
    pwd_login_signup_error = (
        By.CSS_SELECTOR,
        'ng-component > div > div > div > div > form > fieldset > field:nth-child(2) > div > span')
    signup_login_btn = (
        By.CSS_SELECTOR, 'ng-component > div > div > div > div > form > fieldset > div.sticky-bottom-btn-panel > div > div > button.btn.btn-green')

    # contactInfo

    contactInfo_title = (
        By.CSS_SELECTOR, 'app-contact > div > div > div.media > div > div > div > h1')

    contactInfo_signUp_companyName = (
        By.CSS_SELECTOR, 'app-contact > div > div > app-contact-form > div > div > form > fieldset > div > div:nth-child(1) > field > div > label > input')
    contactInfo_signUp_contactName = (
        By.CSS_SELECTOR, 'app-contact > div > div > app-contact-form > div > div > form > fieldset > div > div:nth-child(2) > field > div > label > input')
    contactInfo_signUp_phn = (
        By.CSS_SELECTOR, 'app-contact > div > div > app-contact-form > div > div > form > fieldset > div > div:nth-child(3) > field > div > label > input')
    contactInfo_companyName_error = (
        By.CSS_SELECTOR, 'app-contact > div > div > app-contact-form > div > div > form > fieldset > div > div:nth-child(1) > field > div > span')
    contactInfo_contactName_error = (
        By.CSS_SELECTOR, 'app-contact > div > div > app-contact-form > div > div > form > fieldset > div > div:nth-child(2) > field > div > span')
    contactInfo_signUp_phn_number_error = (
        By.CSS_SELECTOR, 'app-contact > div > div > app-contact-form > div > div > form > fieldset > div > div:nth-child(3) > field > div > span')
    contactInfo_signUp_btn = (
        By.CSS_SELECTOR, 'app-contact > div > div > app-contact-form > div > div > form > fieldset > div > div.sticky-bottom-btn-panel > div > div > button.btn.btn-green')

    # brand
    brand_title = (By.CSS_SELECTOR,
                   'app-brands > div > div > div.media > div > div > div > h1')
    brand_signUp = (By.CLASS_NAME, 'select-check')
    brand_start_app_btn = (
        By.CSS_SELECTOR, 'app-brands > div > div > app-brands-form > div > form > fieldset > div.sticky-bottom-btn-panel > div > div > button.btn.btn-green')

    # companyInfo

    companyinfo_title = (
        By.CSS_SELECTOR, 'app-company-information > div > div > div.media > div > div > div.col-lg-7.col-md-12.text-center > h1')

    compyinfo_signUp_reseller_id = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(1) > field > div > label > input')
    compyinfo_signUp_street_add = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(2) > field > div > label > input')
    compyinfo_signUp_city = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(3) > field > div > label > input')
    compyinfo_signUp_state = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(4) > field > div > label > div > input')
    compyinfo_signUp_post_code = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(5) > field > div > label > input')
    compyinfo_signUp_website = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(6) > field > div > label > input')
    compyinfo_signUp_email = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(7) > field > div > label > input')
    compyinfo_signUp_phn = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(8) > field > div > label > input')
    compyinfo_signUp_otherphn = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(9) > field > div > label > input')

    companyinfo_street_add_error = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(2) > field > div > span')

    companyinfo_city_error = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(3) > field > div > span')

    companyinfo_state_error = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(4) > field > div > span')

    companyinfo_post_error = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(5) > field > div > span')

    companyinfo_website_error = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(6) > field > div > span')

    companyinfo_email_error = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(7) > field > div > span')

    companyinfo_phn_error = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(8) > field > div > span')

    companyinfo_othr_error = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.row > div:nth-child(9) > field > div > span')

    companyinfo_next_btn = (
        By.CSS_SELECTOR, 'app-company-information > div > div > app-company-information-form > div > div > form > fieldset > div.sticky-bottom-btn-panel > div > div > button.btn.btn-green')

    # location

    location_title = (
        By.CSS_SELECTOR, 'app-locations > div > div > div.media > div > div > div.col-lg-7.col-md-12.text-center > h1')

    location_signUp_name1 = (
        By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > field > div > label > input')
    location_signUp_street_add1 = (
        By.CSS_SELECTOR, '#collapse1 > div > div > div:nth-child(2) > field > div > label > input')

    # location_signUp_street_add1 = (
    # By.CSS_SELECTOR, '#collapse1 > div > div > div:nth-child(2) > field >
    # div > label > input')
    location_signUp_city1 = (
        By.CSS_SELECTOR, '#collapse1 > div > div > div:nth-child(3) > field > div > label > input')
    location_signUp_state1 = (
        By.CSS_SELECTOR, '#collapse1 > div > div > div:nth-child(4) > field > div > label > div > input')
    location_signUp_post_code1 = (
        By.CSS_SELECTOR, '#collapse1 > div > div > div:nth-child(5) > field > div > label > input')
    location_signUp_email1 = (
        By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(6) > field > div > label > input')
    location_signUp_phn1 = (
        By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(7) > field > div > label > input')
    location_signUp_otherphn1 = (
        By.CSS_SELECTOR, '#collapse1 > div > div > div:nth-child(8) > field > div > label > input')

    street_error1 = (
        By.CSS_SELECTOR, '#collapse1 > div > div > div:nth-child(2) > field > div > span')
    city_error1 = (
        By.CSS_SELECTOR, '#collapse1 > div > div > div:nth-child(3) > field > div > span')
    state_error1 = (
        By.CSS_SELECTOR, '#collapse1 > div > div > div:nth-child(4) > field > div > span')
    post_error1 = (
        By.CSS_SELECTOR, '#collapse1 > div > div > div:nth-child(5) > field > div > span')
    otr_phn_error1 = (By.CSS_SELECTOR,
                      '#collapse1 > div > div > div:nth-child(8) > field > div > span')

    location_signUp_name2 = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(1) > field > div > label > input')
    location_signUp_street_add2 = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(2) > field > div > label > input')
    location_signUp_city2 = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(3) > field > div > label > input')
    location_signUp_state2 = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(4) > field > div > label > div > input')
    location_signUp_post_code2 = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(5) > field > div > label > input')
    location_signUp_email2 = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(6) > field > div > label > input')
    location_signUp_phn2 = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(7) > field > div > label > input')
    location_signUp_otherphn2 = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(8) > field > div > label > input')
    location_signUp_check2 = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div.col-md-4.location-checkbox > div > label')

    loc2_post_code_err = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(5) > field > div > span')
    loc2_email_err = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(6) > field > div > span')
    loc2_phn_err = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(7) > field > div > span')

    location_signUp_add_loc = (By.CLASS_NAME, 'add-location')
    location_signUp_delete3 = (
        By.CSS_SELECTOR, '#heading3 > h5 > div > i.material-icons.delete-location')
    location_signUp_del_modal = (
        By.XPATH, '//*[@id="remove-location-modal3"]/div/div/div[2]/button[2]')
    loc_next_btn = (By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(5) > div > div > div > button.btn.btn-green')

    # warehouse/ship

    ship_title = (
        By.CSS_SELECTOR, 'app-warehouses > div > div > div.media > div > div > div.col-lg-7.col-md-12.text-center > h1')

    ship_signUp_start_time = (
        By.CSS_SELECTOR, 'app-warehouses > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(9) > field > div > label > input')
    ship_signUp_end_time = (
        By.CSS_SELECTOR, 'app-warehouses > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(10) > field > div > label > input')
    ship_start_time = (By.ID, 'timepicker-item-id-2')
    ship_end_time = (By.ID, 'timepicker-item-id-6')
    ship_ok_btn_start_end = (
        By.XPATH, '//*[@id="time-picker"]/div[3]/button[2]')
    ship_signUp_add_ship2 = (
        By.CSS_SELECTOR, 'app-warehouses > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(3) > div > a')

    ship2_name = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(1) > field > div > label > input')
    ship2_street_add = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(2) > field > div > label > input')
    ship2_city = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(3) > field > div > label > input')
    ship2_state = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(4) > field > div > label > div > input')
    ship2_post = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(5) > field > div > label > input')
    ship2_email = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(6) > field > div > label > input')
    ship2_phn = (By.CSS_SELECTOR,
                 '#collapse2 > div > div > div:nth-child(7) > field > div > label > input')
    ship2_othr_phn = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(8) > field > div > label > input')
    ship2_start = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(9) > field > div > label > input')
    ship2_end = (By.CSS_SELECTOR,
                 '#collapse2 > div > div > div:nth-child(10) > field > div > label > input')

    ship2_street_err = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(2) > field > div > span')
    ship2_city_err = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(3) > field > div > span')
    ship2_post_err = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(5) > field > div > span')
    ship2_email_err = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(6) > field > div > span')
    ship2_phn_err = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(7) > field > div > span')
    ship2_othr_phn_err = (
        By.CSS_SELECTOR, '#collapse2 > div > div > div:nth-child(8) > field > div > span')

    ship_signUp_add_ship3 = (
        By.CSS_SELECTOR, 'app-warehouses > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(4) > div > a')

    ship_signUp_delete3 = (By.XPATH, '//*[@id="heading3"]/h5/div/i[1]')
    ship_signUp_del_modal = (
        By.XPATH, '//*[@id="remove-location-modal3"]/div/div/div[2]/button[2]')
    ship_next_btn = (
        By.CSS_SELECTOR, 'app-warehouses > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(5) > div > div > div > button.btn.btn-green')

    # categories

    categories_title = (
        By.CSS_SELECTOR, 'app-categories > div > div > div.media > div > div > div.col-lg-7.col-md-12.text-center > h1')

    categories_signUp_cook_microwave = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(3) > field > div > label > div > input')
    categories_signUp_cook_oven = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(4) > field > div > label > div > input')
    categories_signUp_cook_hood = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(2) > field > div > label > div > input')
    categories_signUp_cook_stove = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > field > div > label > div > input')
    categories_signUp_dish_dishwasher = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(2) > div > div > field > div > label > div > input')
    categories_signUp_laundry_washer = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(3) > div > div:nth-child(1) > field > div > label > div > input')
    categories_signUp_laundry_pedestal = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(3) > div > div:nth-child(2) > field > div > label > div > input')
    categories_signUp_laundry_combo = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(3) > div > div:nth-child(3) > field > div > label > div > input')
    categories_signUp_laundry_dryer = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(3) > div > div:nth-child(4) > field > div > label > div > input')
    categories_signUp_other_garbage = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(4) > div > div:nth-child(1) > field > div > label > div > input')
    categories_signUp_other_compactor = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(4) > div > div:nth-child(2) > field > div > label > div > input')
    categories_signUp_refrigeration_icemaker = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(5) > div > div:nth-child(1) > field > div > label > div > input')
    categories_signUp_refrigeration_freezer = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(5) > div > div:nth-child(2) > field > div > label > div > input')
    categories_signUp_refrigeration_refrigerator = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(5) > div > div:nth-child(3) > field > div > label > div > input')

    categories_cooking_stove_er = (
        By.CSS_SELECTOR, 'app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(4) > field > div > span')
    categories_laundry_combo_er = (
        By.CSS_SELECTOR, 'app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(3) > div > div:nth-child(3) > field > div > span')

    categories_laundry_dryer_er = (
        By.CSS_SELECTOR, 'app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(3) > div > div:nth-child(4) > field > div > span')
    categories_other_compactor_er = (
        By.CSS_SELECTOR, 'app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(4) > div > div:nth-child(2) > field > div > span')
    categories_refrigeration_icemaker_er = (
        By.CSS_SELECTOR, 'app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(5) > div > div:nth-child(1) > field > div > span')

    categories_refrigeration_freezer_er = (
        By.CSS_SELECTOR, 'app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(5) > div > div:nth-child(2) > field > div > span')

    categories_signUp_next_btn = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div.row > div > div > div > button.btn.btn-green')

    # volumes

    volumes_title = (
        By.CSS_SELECTOR, 'ng-component > div > div > div.media > div > div > div.col-lg-7.col-md-12.text-center > h1')

    volumes_signUp_quarter_truck_q1 = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(1) > field > div > label > div > input')
    volumes_signUp_half_truck_q1 = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(2) > field > div > label > div > input')
    volumes_signUp_full_truck_q1 = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(3) > field > div > label > div > input')

    volumes_signUp_check_q2 = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div:nth-child(1) > div > div:nth-child(2) > div > div > div > label')
    volumes_signUp_quarter_truck_q2 = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(1) > field > div > label > div > input')
    volumes_signUp_half_truck_q2 = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(2) > field > div > label > div > input')
    volumes_signUp_full_truck_q2 = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(3) > field > div > label > div > input')

    volumes_num_full_trucks_q1_err = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(3) > field > div > span')

    volumes_num_half_trucks_q2_err = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(2) > field > div > span')

    volumes_num_full_trucks_q2_err = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(3) > field > div > span')

    volumes_signUp_acknowledge_check = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div.custom-control.custom-checkbox > label')

    volumes_back_button = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div.row > div > div > div > button:nth-child(3)')

    volumes_signUp_sub_app_btn = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div.row > div > div > div > button.btn.btn-green')

    # congratulations

    # congrats_kirv_image = (
    #     By.XPATH, '//*[@class="logo"]')
    # congrats_title = (
    #     By.XPATH, '//*[contains(text(),"Congratulations!")]')
    # congratulation_modal_close = (By.CSS_SELECTOR, '#congrats > div > a')

    congrats_kirv_image = (
        By.CSS_SELECTOR, '#congrats > header > img')
    congrats_title = (
        By.CSS_SELECTOR, '#congrats > div > h1')
    congratulation_modal_close = (By.CSS_SELECTOR, '#congrats > div > a')

    # sign-up

    signup = (By.CLASS_NAME, 'btn-green')
    signupLink = (By.XPATH, '//a[text()="Sign up here"]')

    # sign-up steps

    steps = (By.XPATH, '//ul[@class="steps-ul"]')
