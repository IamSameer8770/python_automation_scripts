import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

class Search_Customer_Page:
    #locators in the application
    text_email_id="SearchEmail"
    text_first_name_id="SearchFirstName"
    text_last_name_id="SearchLastName"
    text_company_name_id="SearchCompany"
    btn_search_id="search-customers"

    rows_table_xpath="//table[@id='customers-grid']/tbody//tr"
    col_table_xpath="//table[@id='customers-grid']/tbody//tr/td"

    def __init__(self,driver):
        self.driver=driver

    def enter_email(self,email):
        self.driver.find_element(By.ID, self.text_email_id).clear()
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def enter_first_name(self,firstname):
        self.driver.find_element(By.ID, self.text_first_name_id).clear()
        self.driver.find_element(By.ID,self.text_first_name_id).send_keys(firstname)

    def enter_last_name(self,lastname):
        self.driver.find_element(By.ID, self.text_last_name_id).clear()
        self.driver.find_element(By.ID,self.text_last_name_id).send_keys(lastname)

    def enter_company_name(self,company_name):
        self.driver.find_element(By.ID,self.text_company_name_id).clear()
        self.driver.find_element(By.ID, self.text_company_name_id).send_keys(company_name)

    def click_search(self):
        self.driver.find_element(By.ID,self.btn_search_id).click()

    def get_results_table_row(self):
        row=self.driver.find_elements(By.XPATH,self.rows_table_xpath)
        return len(row)

    def get_results_table_col(self):
        col=self.driver.find_elements(By.XPATH,self.col_table_xpath)
        return len(col)

