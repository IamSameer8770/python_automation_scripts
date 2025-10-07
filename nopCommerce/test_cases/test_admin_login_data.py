import time

import pytest
#from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from selenium.webdriver.support.ui import *
from selenium.webdriver.common.alert import Alert

from base_pages.login_admin_page import Login_Admin_Page
from selenium.webdriver.common.keys import Keys
from test_cases.confest import browser_setup
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils

class Test_02_Admin_Login_DataDriven:
    url=Read_Config.get_url()
    logger=Log_Maker.log_gem()
    path=".//test_data//excel_login_data.xlsx"


    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_login_data_driven(self,browser_setup):
        self.logger.info("********  Test_Case_002 started Data Driven **********************************")
        self.driver=browser_setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.admin_lp=Login_Admin_Page(self.driver)

        self.row=excel_utils.get_row_count(self.path,"Sheet1")
        print("number of rows:",self.row)

        for r in range(2,self.row+1):
            self.username=excel_utils.read_data(self.path,"Sheet1",r,1)
            self.password=excel_utils.read_data(self.path,"Sheet1",r,2)
            self.exp_login=excel_utils.read_data(self.path,"Sheet1",r,3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            time.sleep(4)
            self.driver.save_screenshot(".\\screenshots\\test_valid_login1.png")
            self.admin_lp.click_login()
            time.sleep(12)
            act_title=self.driver.current_url
            exp_title="https://demo.nopcommerce.com/"
            time.sleep(10)

            if act_title==exp_title:
                print("*****Test Passed*****")
                self.admin_lp.click_logout()
                self.driver.quit()
                time.sleep(10)
            else:
                print("***** Test Fail ******")
                self.driver.quit()






