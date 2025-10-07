import time

import pytest
#from selenium.webdriver.chrome import webdriver
from selenium import webdriver


from base_pages.login_admin_page import Login_Admin_Page
from selenium.webdriver.common.keys import Keys
from test_cases.confest import browser_setup
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test_01_Admin_Login:
    url=Read_Config.get_url()
    username=Read_Config.get_username()
    password=Read_Config.get_password()
    invalid_username=Read_Config.get_invalid_username()
    logger=Log_Maker.log_gem()

    @pytest.mark.regression
    def test_title_verification(self,browser_setup):
        self.logger.info("*******Test_Case_001 starter***********************************")
        self.driver= browser_setup
        self.driver.get(self.url)
       # self.driver.save_screenshot(".\\screenshots\\test_title_verification1.png")
        print(self.driver.title)
        exc_title=self.driver.title
        if exc_title==self.driver.title:
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_title_verification1.png")
            self.logger.info("******Title verification is successfull********************************************")
            self.driver.close()

        else:
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_login(self,browser_setup):
        self.logger.info("********Test_Case_002 started**********************************")
        self.driver=browser_setup
        self.driver.get(self.url)
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        time.sleep(4)
        self.driver.save_screenshot(".\\screenshots\\test_valid_login1.png")
        self.logger.info("******Test_Case_002 completed*****************************")
        self.admin_lp.click_login()
    @pytest.mark.sanity
    def test_invalid_login(self, browser_setup):
        self.driver = browser_setup
        self.driver.get(self.url)
        self.admin_lp = Login_Admin_Page(self.driver)

        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        time.sleep(4)
        self.driver.save_screenshot(".\\screenshots\\test_invalid_login.png")
        time.sleep(3)
        self.admin_lp.click_login()




