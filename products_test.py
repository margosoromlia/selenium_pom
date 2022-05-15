from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from constants import *
import time
import pytest


def test_product_page(get_driver):
    login_page = LoginPage(get_driver)
    login_page.perform_complete_login(CREDS['standard_user']['login'], CREDS['standard_user']['password'])

    product_page = ProductsPage(get_driver)
    product_page.click_on_product("Sauce Labs Backpack")
    time.sleep(10)


@pytest.mark.parametrize("product_name, desc, price", [
    (PRODUCTS['Backpack']['name'], PRODUCTS['Backpack']['desc'], PRODUCTS['Backpack']['price']),
    (PRODUCTS['Bikelight']['name'], PRODUCTS['Bikelight']['desc'], PRODUCTS['Bikelight']['price']),
    (PRODUCTS['T-Shirt']['name'], PRODUCTS['T-Shirt']['desc'], PRODUCTS['T-Shirt']['price']),
    (PRODUCTS['Jacket']['name'], PRODUCTS['Jacket']['desc'], PRODUCTS['Jacket']['price']),
    (PRODUCTS['Sauce Labs']['name'], PRODUCTS['Sauce Labs']['desc'], PRODUCTS['Sauce Labs']['price']),
    (PRODUCTS['T-Shirt (Red)']['name'], PRODUCTS['T-Shirt (Red)']['desc'], PRODUCTS['T-Shirt (Red)']['price']),
])
def test_check_description(get_driver, product_name, desc, price):
    login_page = LoginPage(get_driver)
    login_page.perform_complete_login(CREDS['standard_user']['login'], CREDS['standard_user']['password'])

    product_page = ProductsPage(get_driver)
    product_page.click_on_product(product_name)

    assert product_page.actual_description() == desc
    assert product_page.actual_price() == price
