import requests

class TestCookieDefinition:
    def test_cookie_definition(self):
        payload = {"email": 'vinkotov@example.com', "password": '1234'}
        response_for_cookie = requests.post("https://playground.learnqa.ru/api/homework_cookie", data=payload)

        cookie_from_response = {'HomeWork': 'hw_value'} ## некрасиво, но умышленно не достаю значение через response_for_cookie.cookies.get, потому что надо проверить не только значение.ю но и вид куки, что это точно HomeWork

        assert dict(response_for_cookie.cookies) == cookie_from_response, "Cookie from response is not equal to expected one"
