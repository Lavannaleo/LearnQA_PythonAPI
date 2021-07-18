from LearnQA_PythonAPI.lib.my_requests import MyRequests
from LearnQA_PythonAPI.lib.base_case import BaseCase
from LearnQA_PythonAPI.lib.assertions import Assertions

class TestUserDelete(BaseCase):
    def test_delete_user_with_id_2(self):
        # LOGIN user id=2
        login_data = {
        'email': 'vinkotov@example.com',
        'password': '1234'
        }
        response = MyRequests.post("/user/login", data=login_data)

        self.auth_sid = self.get_cookie(response, "auth_sid")
        self.token = self.get_header(response, "x-csrf-token")

        # DELETE user with id=2
        response1 = MyRequests.delete(f"/user/2",
                                      headers={"x-csrf-token": self.token},
                                      cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_code_status(response1, 400)
        assert response1.content.decode('utf-8') == "Please, do not delete test users with ID 1, 2, 3, 4 or 5.",f"Unexpected response content '{response1.content.decode('utf-8')}'"

    def test_delete_user_same_user_is_auth(self):
        # REGISTER new user
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN new user
        login_data = {
        'email': email,
        'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid_new_user = self.get_cookie(response2, "auth_sid")
        token_new_user = self.get_header(response2, "x-csrf-token")

        # DELETE new user
        response3 = MyRequests.delete(f"/user/{user_id}",
                                      headers={"x-csrf-token": token_new_user},
                                      cookies={"auth_sid": auth_sid_new_user}
        )

        Assertions.assert_code_status(response3, 200)

        # INFO about new user is absent - delete is success
        login_data = {
        'email': email,
        'password': password
        }
        response2 = MyRequests.get(f"/user/{user_id}", data=login_data)

        Assertions.assert_code_status(response2, 404)
        assert response2.content.decode('utf-8') == "User not found", "Unexpected case - user is found"

    def test_delete_user_other_user_is_auth(self):
        # REGISTER new user
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN new user
        login_data = {
        'email': email,
        'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid_new_user = self.get_cookie(response2, "auth_sid")
        token_new_user = self.get_header(response2, "x-csrf-token")

        #LOGOUT new user
        response_logout = MyRequests.post("/user/login", data=login_data)

        # LOGIN user id=2
        login_data = {
        'email': 'vinkotov@example.com',
        'password': '1234'
        }
        response = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")

        # DELETE new user
        response3 = MyRequests.delete(f"/user/{user_id}",
                                      headers={"x-csrf-token": token_new_user},
                                      cookies={"auth_sid": auth_sid_new_user}
        )

        Assertions.assert_code_status(response3, 200)

        # LOGIN new user - delete is false
        login_data = {
        'email': email,
        'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")


