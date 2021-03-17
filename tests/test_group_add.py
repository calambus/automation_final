from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.groups_page import GroupsPage
from pages.main_admin_page import MainAdminPage
import allure

allure.story("Check that created group in DB is isplayed in Groups list")


def test_db_group_added_and_displayed(browser, create_group):
    # with allure.step("Open Base page"):
    bp = BasePage(browser)
    bp.open_base_page()
    with allure.step("Open Login page"):
        lg = LoginPage(browser)
        lg.open_login_page()
    with allure.step("Log in as Admin"):
        lg.login_as_admin()
        mp = MainAdminPage(browser)
        mp.should_be_main_page()
    with allure.step("Open Groups list"):
        mp.open_users_or_groups_from_left_menu('groups')
        gp = GroupsPage(browser)
    with allure.step("Verify that created group displayed in the list"):
        gp.check_group_exist(create_group)
