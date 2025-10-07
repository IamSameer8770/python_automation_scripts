import pytest
from selenium import webdriver

@pytest.fixture()
def browser_setup():
    driver=webdriver.Chrome()
    return driver


