import pytest
import requests
from LearnQA_PythonAPI.lib.my_requests import MyRequests
from LearnQA_PythonAPI.lib.base_case import BaseCase
from LearnQA_PythonAPI.lib.assertions import Assertions


class TestUserRegister(BaseCase):
    exclude_params = [
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email"),
        ("password")
    ]

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists",f"Unexpected response content '{response.content}'"

    def test_create_user_with_incorrect_email_format(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format",f"Unexpected response content '{response.content}'"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_create_user_without_one_parameter(self, condition):
        data = self.prepare_registration_data()

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

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of '{condition}' field is too short",f"Unexpected response content '{response.content}'"

    def test_create_user_with_short_username(self):
        data = self.prepare_registration_data()
        data.update(username="v")

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short",f"Unexpected response content '{response.content}'"

    def test_create_user_with_long_username(self):
        data = self.prepare_registration_data()
        # username lenght is 256 symbols
        data.update(username = 'vinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvn')

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long",f"Unexpected response content '{response.content}'"









