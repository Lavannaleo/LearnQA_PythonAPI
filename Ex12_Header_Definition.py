import requests

class TestHeaderDefinition:
    def test_header_definition(self):
        payload = {"email": "vinkotov@example.com", "password": "1234"}
        response_for_header = requests.post("https://playground.learnqa.ru/api/homework_header", data=payload)

        ## Expected result:  'x-secret-homework-header': 'Some secret value'
        header_key = 'x-secret-homework-header'
        header_value = 'Some secret value'

        assert response_for_header.headers.get(header_key) == header_value,f"Header '{header_key}' with value '{header_value}' from response is not equal to expected one"