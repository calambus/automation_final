from selenium.webdriver.common.by import By


class MainAdminLOcators:
    LOCATOR_GROUPS = (By.XPATH, "//a[@href='/admin/auth/group/']")
    LOCATOR_MAIN_TITLE = (By.XPATH, "//h1[contains(text(),'Site administration')]")
    LOCATOR_ADD_USER = (By.XPATH, "//a[@href='/admin/auth/user/add/']")
    LOCATOR_USERS = (By.XPATH, "//a[@href='/admin/auth/user/']")

    def get_left_bar_users_or_groups_xpath(self, param: str):
        if param == 'users':
            return (By.XPATH, "//div[@class='app-auth module']//a[contains(text(),'Users')]")
        if param == 'groups':
            return (By.XPATH, "//div[@class='app-auth module']//a[contains(text(),'Groups')]")
