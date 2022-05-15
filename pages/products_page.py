from selenium.common.exceptions import NoSuchElementException
from constants import URL_PRODUCTS
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 15, 0.3)

    def get_url_products(self):
        self.driver.get(URL_PRODUCTS)

    def __get_product(self, product_name):
        self.__wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))

        all_products = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        for product in all_products:
            if product.text == product_name:
                return product

    def click_on_product(self, product_name):
        product = self.__get_product(product_name)
        product.click()

    def actual_description(self):
        description = self.__wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "inventory_details_desc")))
        return description.text

    def actual_price(self):
        price = self.__wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "inventory_details_price")))
        return price.text
