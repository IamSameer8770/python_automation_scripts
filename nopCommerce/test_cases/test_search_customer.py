import time
import pytest
#from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.login_admin_page import Login_Admin_Page
from base_pages.add_customer_page import Add_Customer_Page
from selenium.webdriver.common.keys import Keys
from test_cases.confest import browser_setup
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.search_customer_page import Search_Customer_Page

class Test_04_search_New_user:
    url = Read_Config.get_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gem()

    @pytest.mark.smoke
    def test_search_customer(self,browser_setup):
        self.logger.info("****** Test_03_adding new customer*********")
        self.driver=browser_setup
        self.driver.get(self.url)
        self.driver.implicitly_wait(20)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        time.sleep(4)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("**** Login Successfull ****")

        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customer_menu()
        self.driver.implicitly_wait(10)
        self.add_customer.click_customer_option()
        self.logger.info("*** search customer by email *****")
        self.search_custmer=Search_Customer_Page(self.driver)
        self.search_custmer.enter_email("user_vendors20p@test.com")
        self.search_custmer.click_search()
        self.logger.info("**** customer details fetched successfully ****")
        #print(self.search_custmer.get_results_table_row())
        #print(self.search_custmer.get_results_table_col())
        self.driver.quit()









