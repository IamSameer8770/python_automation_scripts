import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

class Add_Customer_Page:
    #locators in the application
    link_customers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menu_option_xpath="//a[@href='/Admin/Customer/List']"
    link_add_new_xpath="//a[normalize-space()='Add new']"
    text_email_id="Email"
    text_password_id="Password"
    text_first_name_id="FirstName"
    text_last_name_id="FirstName"
    rdo_gender_male_id="Gender_Male"
    rdo_gender_female_id = "Gender_Female"
    text_company_name_id="Company"
    chck_tax_emept_id="IsTaxExempt"
    click_newsletter_xpath="(//span[@role='combobox'])[1]"
    drp_newsletter_xpath="//li[@id='select2-SelectedNewsletterSubscriptionStoreIds-result-pn7w-1']"
    slct_managevenors_id="VendorId"
    chclbx_active_id="Active"
    text_admin_content_id="AdminComment"
    click_save_xpath="//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver


    def click_customer_menu(self):
        self.driver.find_element(By.XPATH,self.link_customers_menu_xpath).click()

    def click_customer_option(self):
        self.driver.find_element(By.XPATH,self.link_customer_menu_option_xpath).click()

    def click_addnew_button(self):
        self.driver.find_element(By.XPATH,self.link_add_new_xpath).click()

    def enter_email(self,email):
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.text_first_name_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.text_last_name_id).send_keys(lastname)

    def select_gender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.ID,self.rdo_gender_male_id).click()
        elif gender=="Female":
            self.driver.find_element(By.ID,self.rdo_gender_female_id).click()
        else:
            self.driver.find_element(By.ID,self.rdo_gender_male_id).click()

    def enter_company_name(self,companyname):
        self.driver.find_element(By.ID,self.text_company_name_id).send_keys(companyname)

    def rdo_tax_emept(self):
        self.driver.find_element(By.ID,self.chck_tax_emept_id).click()

    def chclbx_active(self):
        self.driver.find_element(By.ID,self.chclbx_active_id).click()

    def enter_admintext(self,admincontents):
        self.driver.find_element(By.ID,self.text_admin_content_id).send_keys(admincontents)

    def click_save(self):
        self.driver.find_element(By.XPATH,self.click_save_xpath).click()
