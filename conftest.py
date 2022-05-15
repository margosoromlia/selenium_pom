import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrom_options():
    options = chrome_options()
    options.add_argument('chrom')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(get_chrom_options):
    options = get_chrom_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def get_driver(get_webdriver):
    driver = get_webdriver
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    yield driver
    driver.quit()
