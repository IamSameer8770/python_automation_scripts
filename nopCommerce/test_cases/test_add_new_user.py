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

class Test_03_Add_New_user:
    url = Read_Config.get_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gem()

    @pytest.mark.smoke
    def test_add_new_customer(self,browser_setup):
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

        self.add_customer=Add_Customer_Page(self.driver)
        self.add_customer.click_customer_menu()
        self.add_customer.click_customer_option()
        self.add_customer.click_addnew_button()
        self.add_customer.enter_email("jack@gmail.com")
        self.add_customer.enter_password("jack123456")
        self.add_customer.enter_firstname("jack")
        self.add_customer.enter_lastname("son")
        self.add_customer.select_gender("Male")
        self.add_customer.enter_company_name("Florida india pvt lmtd")
        self.add_customer.rdo_tax_emept()
        self.add_customer.chclbx_active()
        self.add_customer.enter_admintext("Testing")
        self.logger.info("**** New User Details added successfully****")
        self.add_customer.click_save()
        customer_added_success_msg="The new customer has been added successfully."
        success_text=self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissable']").text
        if customer_added_success_msg in success_text:
            assert True
            self.driver.save_screenshot('\\screenshots\\test03.png')
            self.logger.info("**** Test_03_passed ****")
            self.driver.close()
        else:
            self.logger.info("**** Test_03_Failed ****")
            self.driver.save_screenshot('\\screenshots\\test03.png')
            self.driver.close()









