import pytest
from LearnQA_PythonAPI.lib.my_requests import MyRequests
from LearnQA_PythonAPI.lib.base_case import BaseCase
from LearnQA_PythonAPI.lib.assertions import Assertions
import allure

@allure.epic("Registraion Cases")
class TestUserRegister(BaseCase):
    exclude_params = [
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email"),
        ("password")
    ]
    @allure.description("This test successfully user creation by email and password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("This negative test checks create user with existing email")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists",f"Unexpected response content '{response.content}'"

    @allure.description("This negative test checks create user with incorrect email format")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_incorrect_email_format(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format",f"Unexpected response content '{response.content}'"

    @allure.description("This negative test checks create user without one parameter")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('condition', exclude_params)
    def test_create_user_without_one_parameter(self, condition):
        data = self.prepare_registration_data()

        # ?????????????? ???????????? ?????????????? ?????????????? data
        data[condition] = ""

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of '{condition}' field is too short",f"Unexpected response content '{response.content}'"

    @allure.description("This negative test checks create user with very short username")
    @allure.severity(allure.severity_level.MINOR)
    def test_create_user_with_short_username(self):
        data = self.prepare_registration_data()
        data.update(username="v")

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short",f"Unexpected response content '{response.content}'"

    @allure.description("This negative test checks create user with very long username")
    @allure.severity(allure.severity_level.MINOR)
    def test_create_user_with_long_username(self):
        data = self.prepare_registration_data()
        # username lenght is 256 symbols
        data.update(username = 'vinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvanvinvinvn')

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long",f"Unexpected response content '{response.content}'"









