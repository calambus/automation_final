from api.api import Api
from helpers.general_helpers import generate_string
import allure


@allure.story("Check create User, Login, User Info and logout")
def test_api_scenario():
    username = generate_string(6)
    password = generate_string(6)
    api = Api()
    with allure.step("Create User"):
        api.create_user(username, password)
    with allure.step("Login with created User"):
        api.login(username, password)
    with allure.step("Get User info"):
        api.get_user_info(username)
    with allure.step("Logout"):
        api.logout()
    with allure.step("Delete User"):
        api.delete_user(username)
