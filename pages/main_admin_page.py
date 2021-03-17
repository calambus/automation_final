from pages.base_page import BasePage
from locators.locators_main_admin_page import MainAdminLOcators


class MainAdminPage(BasePage, MainAdminLOcators):

    def should_be_main_page(self):
        self.find_element(self.LOCATOR_MAIN_TITLE)

    def open_users_or_groups_from_left_menu(self, param):
        locator = self.get_left_bar_users_or_groups_xpath(param)
        link = self.find_element(locator)
        link.click()

    def open_add_user_page(self):
        add_user_link = self.find_element(self.LOCATOR_ADD_USER)
        add_user_link.click()
