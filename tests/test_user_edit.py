from LearnQA_PythonAPI.lib.my_requests import MyRequests
from LearnQA_PythonAPI.lib.base_case import BaseCase
from LearnQA_PythonAPI.lib.assertions import Assertions


class TestUserEdit(BaseCase):
    def setup(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        self.email = register_data['email']
        self.first_name = register_data['firstName']
        self.password = register_data['password']
        self.user_id = self.get_json_value(response1, "id")

    def test_edit_firstName_just_created_user_by_the_same_auth_user(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"
        response3 = MyRequests.put(f"/user/{self.user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(f"/user/{self.user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name of user after edit")

    def test_edit_just_created_user_by_the_same_unauth_user(self):
        # EDIT W/O AUTH (no headers and cookies)
        new_name = "Changed Name"
        response = MyRequests.put(f"/user/{self.user_id}",
                                 data={"firstName": new_name}
        )

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Auth token not supplied",\
            f"Unexpected response content '{response.content}'"

        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # GET - firstName should be the same
        response3 = MyRequests.get(f"/user/{self.user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(response3, "firstName", self.first_name, "Wrong name of user after edit")

    def test_edit_just_created_user_by_the_other_auth_user(self):
        # LOGIN by other user
        login_data = {
            'email': 'vinkotov@example.com',
            'password': "1234"
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT new user by other auth user
        new_name = "Changed Name"
        response3 = MyRequests.put(f"/user/{self.user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode('utf-8') == "Please, do not edit test users with ID 1, 2, 3, 4 or 5.", \
            f"Unexpected response content '{response3.content}'"

        # LOGIN by new user
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response4 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response4, "auth_sid")
        token = self.get_header(response4, "x-csrf-token")

        # GET by new user - firstName should be the same
        response5 = MyRequests.get(f"/user/{self.user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(response5, "firstName", self.first_name, "Wrong name of user after edit")

    def test_edit_email_just_created_user_by_the_same_auth_user(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_email = "emailexample.com"
        response3 = MyRequests.put(f"/user/{self.user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"email": new_email}
        )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode('utf-8') == "Invalid email format", f"Unexpected response content '{response3.content}'"

        # GET
        response4 = MyRequests.get(f"/user/{self.user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(response4, "email", self.email, "Wrong user email after edit")

    def test_edit_firstName_To_Short_by_the_same_auth_user(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "C"
        response3 = MyRequests.put(f"/user/{self.user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_json_value_by_name(response3, "error", "Too short value for field firstName", f"Unexpected response content '{response3.content}'")

        # GET
        response4 = MyRequests.get(f"/user/{self.user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(response4, "firstName", self.first_name, "Wrong name of user after edit")