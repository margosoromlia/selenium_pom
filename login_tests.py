import pytest
from pages.login_page import LoginPage
from constants import CREDS



@pytest.mark.parametrize("login, password", [
    (CREDS['standard_user']['login'], CREDS['standard_user']['password']),
    (CREDS['locked_out_user']['login'], CREDS['locked_out_user']['password']),
    (CREDS['problem_user']['login'], CREDS['problem_user']['password']),
    (CREDS['performance_glitch_user']['login'], CREDS['performance_glitch_user']['password'])
])
def test_login_page_user_1(get_driver, login, password):
    login_page = LoginPage(get_driver)
    login_page.perform_complete_login(login, password)
    # assert login_page.not_logged()
    assert login_page.is_logged()



# def test_login_page_user_2(get_driver):
#     login_page = LoginPage(get_driver)
#     login_page.perform_complete_login(CREDS['locked_out_user']['login'], CREDS['locked_out_user']['password'])
#     assert login_page.not_logged()
#
#
# def test_login_page_user_3(get_driver):
#     login_page = LoginPage(get_driver)
#     login_page.perform_complete_login(CREDS['problem_user']['login'], CREDS['problem_user']['password'])
#     assert login_page.is_logged()


def test_login_page_user_4(get_driver):
    login_page = LoginPage(get_driver)
    login_page.perform_complete_login(CREDS['performance_glitch_user']['login'],
                                      CREDS['performance_glitch_user']['password'])
    assert login_page.is_logged()
