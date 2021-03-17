from pages.base_page import BasePage
from locators.locators_add_user import AddUserLocators
from selenium.webdriver.support.ui import Select
import allure
from allure_commons.types import AttachmentType

class AddUserPage(BasePage, AddUserLocators):

    def add_user_with_group(self, username, password, group, browser):
        uname = self.find_element(self.LOCATOR_USERNAME)
        passwrd = self.find_element(self.LOCATOR_PASSWORD)
        repeate_pass = self.find_element(self.LOCATOR_CONFIRM_PASSWORD)
        save = self.find_element(self.LOCATOR_SAVE)
        uname.send_keys(username)
        passwrd.send_keys(password)
        repeate_pass.send_keys(password)
        save.click()
        save = self.find_element(self.LOCATOR_SAVE)
        select = Select(self.find_element(self.LOCATOR_GROUP_SELECT))
        select.select_by_visible_text(group)
        add_to_group = self.find_element(self.LOCATOR_ADD_SELECTED_GROUP)
        allure.attach(
            browser.get_screenshot_as_png(),
            name='screen_error',
            attachment_type=AttachmentType.PNG
        )
        add_to_group.click()
        save.click()
