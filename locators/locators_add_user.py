from selenium.webdriver.common.by import By


class AddUserLocators:
    LOCATOR_USERNAME = (By.XPATH, "//input[@name='username']")
    LOCATOR_PASSWORD = (By.XPATH, "//input[@name='password1']")
    LOCATOR_CONFIRM_PASSWORD = (By.XPATH, "//input[@name='password2']")
    LOCATOR_SAVE = (By.XPATH, "//input[@value='Save']")
    # LOCATOR_ADD_SELECTED_GROUP = (By.XPATH, "//a[@id='id_groups_add_link']")
    LOCATOR_ADD_SELECTED_GROUP = (By.XPATH, "//div[@class ='form-row field-groups'] // a[@ class ='selector-add']")
    //div[@class ='form-row field-groups'] // a[@ class ='selector-add']
    LOCATOR_GROUP_SELECT = (By.XPATH, "//select[@id='id_groups_from']")
    LOCATOR_USERNAME_ROW = (By.XPATH, "//th[@class='field-username']")
