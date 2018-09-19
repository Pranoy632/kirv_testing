from selenium.webdriver.common.by import By


class SigninPageLocators(object):

    email_login_signup = (
        By.CSS_SELECTOR, 'ng-component > div > div > div > div > form > fieldset > field:nth-child(1) > div > label > input')
    pwd_login_signup = (
        By.CSS_SELECTOR, 'ng-component > div > div > div > div > form > fieldset > field:nth-child(2) > div > label > input')

    contactInfo_signUp_companyName = (
        By.CSS_SELECTOR, 'app-contact > div > div > app-contact-form > div > div > form > fieldset > div > div:nth-child(1) > field > div > label > input')
    contactInfo_signUp_contactName = (
        By.CSS_SELECTOR, 'app-contact > div > div > app-contact-form > div > div > form > fieldset > div > div:nth-child(2) > field > div > label > input')
    contactInfo_signUp_phn = (
        By.CSS_SELECTOR, 'app-contact > div > div > app-contact-form > div > div > form > fieldset > div > div:nth-child(3) > field > div > label > input')

    brand_signUp = (By.CLASS_NAME, 'select-check')

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

    location_signUp_name1 = (
        By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > field > div > label > input')
    location_signUp_street_add1 = (
        By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > field > div > label > input')
    location_signUp_city1 = (
        By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(3) > field > div > label > input')
    location_signUp_state1 = (
        By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(4) > field > div > label > div > input')
    location_signUp_post_code1 = (
        By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(5) > field > div > label > input')
    location_signUp_email1 = (
        By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(6) > field > div > label > input')
    location_signUp_phn1 = (
        By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(7) > field > div > label > input')
    location_signUp_otherphn1 = (
        By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(8) > field > div > label > input')

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
    location_signUp_add_loc = (By.CLASS_NAME, 'add-location')
    location_signUp_delete3 = (
        By.CSS_SELECTOR, '#heading3 > h5 > div > i.material-icons.delete-location')
    location_signUp_del_modal = (
        By.XPATH, '//*[@id="remove-location-modal3"]/div/div/div[2]/button[2]')
    loc_next_btn = (By.CSS_SELECTOR, 'app-locations > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(5) > div > div > div > button.btn.btn-green.mt-10.btn-arrow.float-right')

    ship_signUp_start_time = (
        By.CSS_SELECTOR, 'app-warehouses > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(9) > field > div > label > input')
    ship_signUp_end_time = (
        By.CSS_SELECTOR, 'app-warehouses > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(10) > field > div > label > input')
    ship_start_time = (By.ID, 'timepicker-item-id-2')
    ship_end_time = (By.ID, 'timepicker-item-id-6')
    ship_ok_btn_start_end = (
        By.XPATH, '//*[@id="time-picker"]/div[3]/button[2]')
    ship_signUp_add_ship = (
        By.CSS_SELECTOR, 'app-warehouses > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(3) > div > a')
    ship_signUp_delete2 = (By.XPATH, '//*[@id="heading2"]/h5/div/i[1]')
    ship_signUp_del_modal = (
        By.XPATH, '//*[@id="remove-location-modal2"]/div/div/div[2]/button[2]')
    ship_next_btn = (By.CSS_SELECTOR, 'app-warehouses > div > div > app-locations-form > div > div > form > fieldset > div:nth-child(4) > div > div > div > button.btn.btn-green.mt-10.btn-arrow.float-right')

    categories_signUp_cook_microwave = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > field > div > label > div > input')
    categories_signUp_cook_oven = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(2) > field > div > label > div > input')
    categories_signUp_cook_hood = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(3) > field > div > label > div > input')
    categories_signUp_cook_stove = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(4) > field > div > label > div > input')
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

    categories_signUp_next_btn = (
        By.CSS_SELECTOR, 'app-categories > div > div > app-categories-form > div > div > form > fieldset > div.row > div > div > div > button.btn.btn-green.mt-10.btn-arrow.float-right')

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

    volumes_signUp_acknowledge_check = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div.custom-control.custom-checkbox > label')
    volumes_signUp_sub_app_btn = (
        By.CSS_SELECTOR, 'ng-component > div.row > div > form > fieldset > div.row > div > div > div > button.btn.btn-green.mt-10.btn-arrow.float-right')

    congratulation_modal_close = (By.CSS_SELECTOR, '#congrats > button')

    signup = (By.CLASS_NAME, 'btn-green')
