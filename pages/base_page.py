from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.__wait = WebDriverWait(self.driver, 15, 0.3)

    def goto(self):
        self.driver.get(self.url)

    def is_visible(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def click_element(self, locator):
        """
        :param locator: tuple - (By.X, "//selector")
        :return:
        """
        element = self.__wait.until(EC.visibility_of_element_located(locator))

        element.click()

    def send_keys_to_element(self, locator, text):
        """

        :param locator:
        :param text:
        :return:
        """
        element = self.__wait.until(EC.visibility_of_element_located(locator))

        element.send_keys(text)

    def get_element_text(self, locator):
        pass