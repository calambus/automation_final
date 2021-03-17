from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_admin_page import MainAdminPage
from helpers.general_helpers import generate_string
from pages.add_user_page import AddUserPage
from helpers.db_helper import check_user_in_group_db, clear_db_user_groups_table, clear_db_user_not_admin
import allure

allure.story("Check that Group assigned to User is sent to DB")


def test_ad_user_with_group(browser, create_group):
    username = generate_string(6)
    password = generate_string(10)
    with allure.step("Open Base page"):
        bp = BasePage(browser)
        bp.open_base_page()
    with allure.step("Open Login page"):
        lp = LoginPage(browser)
        lp.open_login_page()
    with allure.step("Login as Admin"):
        lp.login_as_admin()
        mp = MainAdminPage(browser)
    with allure.step("Open Add User page"):
        mp.open_users_or_groups_from_left_menu('user_list')
        au = AddUserPage(browser)
    with allure.step("Add User with assigned group"):
        au.add_user_with_group(username, password, create_group, browser)
    with allure.step("Check that group assigned to User in DB"):
        check_user_in_group_db(username, create_group)
