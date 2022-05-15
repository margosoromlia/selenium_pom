from constants import URL_MAIN
from pages.base_page import BasePage
from locators.login_page_locators import *


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, URL_MAIN)
        self.goto()

    def enter_login(self, login):
        self.send_keys_to_element(LOGIN_INPUT, login)

    def enter_password(self, password):
        self.send_keys_to_element(PASSWORD_INPUT, password)

    def clik_button_login(self):
        self.click_element(LOGIN_BUTTON)

    def is_logged(self):
        return self.is_visible(TITLE_CHECK)

    def not_logged(self):
        return self.is_visible(LOGIN_ERROR_MSG)

    def perform_complete_login(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.clik_button_login()
