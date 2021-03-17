from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_admin_page import MainAdminPage
from helpers.general_helpers import generate_string
from pages.add_user_page import AddUserPage
from helpers.db_helper import check_user_in_group_db, clear_db_user_groups_table, clear_db_user_not_admin

def test_ad_user_with_group(browser, create_group):
    username = generate_string(6)
    password = generate_string(10)
    bp = BasePage(browser)
    bp.open_base_page()
    lp = LoginPage(browser)
    lp.open_login_page()
    lp.login_as_admin()
    mp = MainAdminPage(browser)
    mp.open_add_user_page()
    au = AddUserPage(browser)
    au.add_user_with_group(username, password, create_group)
    check_user_in_group_db(username, create_group)
