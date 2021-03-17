import requests
import json
from helpers.general_helpers import generate_int


class Api:

    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2/user/'
        self.headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

    def _assert_request(self, method: str, url: str, data=None, headers=None, status_code=200):
        response = requests.request(method, url, data=data, headers=headers)
        assert response.status_code == status_code, f'Status code is {response.status_code}'
        return response.json()

    def create_user(self, username: str, password: str):
        ids = generate_int(3)
        data = [{
            "id": ids,
            "username": username,
            "firstName": 'firstname',
            "lastName": 'lastname',
            "email": 'email',
            "password": password,
            "phone": "string",
            "userStatus": '0'
        }]
        url = self.base_url + 'createWithArray'
        self._assert_request('POST', url, json.dumps(data), self.headers)

    def get_user_info(self, username: str):
        url = self.base_url + username
        self._assert_request('GET', url)

    def login(self, username, password):
        params = f'login?username={username}&password={password}'
        url = self.base_url + params
        self._assert_request('GET', url)

    def logout(self):
        url = self.base_url + 'logout'
        self._assert_request('GET', url)

    def delete_user(self, username):
        url = self.base_url + username
        self._assert_request('DELETE', url)
