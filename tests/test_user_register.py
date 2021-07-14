import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

class TestUserRegister(BaseCase):
    exclude_params = [
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email"),
        ("password")
    ]

    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists",f"Unexpected response content '{response.content}'"

    def test_create_user_with_incorrect_email_format(self):
        email = 'vinkotovexample.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format",f"Unexpected response content '{response.content}'"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_create_user_without_one_parameter(self, condition):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        # Обнуляю нужный элемент словаря data; некрасиво, но не знаю как по-другому, не хватает знания питона
        if condition == 'username':
            data.update(username="")
        elif condition == 'firstName':
            data.update(firstName="")
        elif condition == 'lastName':
            data.update(lastName="")
        elif condition == 'email':
            data.update(email="")
        elif condition == 'password':
            data.update(password="")

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of '{condition}' field is too short",f"Unexpected response content '{response.content}'"

    def test_create_user_with_short_username(self):
        username = 'v'
        data = {
            'password': '123',
            'username': username,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short",f"Unexpected response content '{response.content}'"

    def test_create_user_with_long_username(self):
        # username lenght is 251 symbols
        username = 'vinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvn'
        data = {
            'password': '123',
            'username': username,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long",f"Unexpected response content '{response.content}'"









