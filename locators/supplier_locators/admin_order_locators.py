from selenium.webdriver.common.by import By


class Admin_Locators(object):
    # login Page
    name = (By.NAME, "username")
    password = (By.NAME, "password")
    submitButton = (By.TAG_NAME, "button")
    url = "https://kirv-ui-staging.herokuapp.com/contract"

    # B2B  = (By.XPATH, '//a[@href="'+url+'"]')
    kirv_services_logo = (By.XPATH, '//h1[contains(text(),"KIRV Services")]')
    customer_dashboard_locator = (By.XPATH, '//img[@src="https://s3.amazonaws.com/kirv-prod/services-logos/Icons-+Customer+Dashboard.png"]')
    kirv_service_locator = (By.XPATH, '//img[@src="/static/images/new_logo.png"]')
    B2B = (By.XPATH, '//img[@src="https://s3.amazonaws.com/kirv-prod/services-logos/Icons+-+Marketplace+Services.png"]')
    super_admin_locator = (By.XPATH, '//img[@src="https://s3.amazonaws.com/kirv-prod/services-logos/super-admin.png"]')
    sso_super_admin_locator = (By.XPATH, '//img[@src="https://s3.amazonaws.com/kirv-prod/services-logos/sso-super-admin.png"]')
    kirv_logo = (By.XPATH, '//img[@alt="KIRV" and @src="../assets/images/kirv/new_logo.png"]')
    home_page_tab = (By.XPATH, '//ul[contains(@class,"navbar-nav d-block")]')

    # home page of admin order
    order_active =(By.XPATH, '//span[contains(text(),"Orders")]/parent::li')
    orderLocator = (By.XPATH, '//span[contains(text(),"Orders")]')
    order_title = (By.XPATH, '//div[contains(@class,"page-title" )]')
    logout_in_order = (By.XPATH, '//span[contains(text(),"Logout")]')
    order_homepage_tab = (By.XPATH, '//ul[@class="sub-navigation"]')
    order_out_of_total_order = (By.XPATH, '//quick-filter/div/div[2]/div')
    pagination_in_order_page = (By.XPATH, '//ul[contains(@class,"pagination pagination-center")]')
    whole_page = (By.XPATH , '/html/body')
    pagination = (By.XPATH, '//ul[contains(@class,"pagination pagination-center")]')


    # order homePage
    chat_box = (By.XPATH, '//*[@id="drift-widget"]')

    ########################## state new ##############################
    new = (By.XPATH,'//a[contains(text(),"New")]')
    new_is_active  = (By.XPATH,'//a[contains(text(),"New")]/parent::li')
    new_error_msg = (By.XPATH, '//h3[contains(text(),"Orders Not Found!")]') 
    get_first_order_num = (By.XPATH,'//tbody/tr/td[2]')
    cancel_Back_search = (By.XPATH,'//*[@id="clear"]')
    search_in_new = (By.XPATH,'//*[@id="search"]')
    table_header = (By.XPATH, '//table[contains(@class,"table table-border")]/th')
    table_row = (By.XPATH, '//table[contains(@class,"table table-border")]/tbody/tr')

    Back_from_new = (By.XPATH, '/html/body/app-root/ng-component/div/div/span')

    ##############################pending state ############################

    pending = (By.XPATH,'//a[contains(text(),"Pending")]')
    pending_is_active = (By.XPATH, '//a[contains(text(),"Pending")]/parent::li')
    get_first_order_buyer_name = (By.XPATH,'//tbody/tr/td[3]')


    ####################### Release State ##############################
    release = (By.XPATH, '//li/a[contains(text(),"Released")]')
    release_order_out_of_total_no =(By.XPATH, '//quick-filter/div/div[2]/div[contains(text(),"1-50 of 88 Orders")]')
    release_is_active = (By.XPATH, '//a[contains(text(),"Released")]/parent::li')


    ################### Ship state ######################################
    ship = (By.XPATH, '//a[contains(text(),"Shipped")]')
    ship_order_out_of_total_no =(By.XPATH, '//quick-filter/div/div[2]/div[contains(text(),"1-50 of 67 Orders")]')
    ship_is_active = (By.XPATH, '//a[contains(text(),"Shipped")]/parent::li[@class="active"]')

