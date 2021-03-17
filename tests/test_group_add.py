from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.groups_page import GroupsPage
from pages.main_admin_page import MainAdminPage


def test_db_group_added_and_displayed(browser, create_group):
    bp = BasePage(browser)
    bp.open_base_page()
    lg = LoginPage(browser)
    lg.open_login_page()
    lg.login_as_admin()
    mp = MainAdminPage(browser)
    mp.should_be_main_page()
    mp.open_users_or_groups_from_left_menu('groups')
    gp = GroupsPage(browser)
    gp.check_group_exist(create_group)
