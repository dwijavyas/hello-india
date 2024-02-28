import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chr_options)
    return driver
