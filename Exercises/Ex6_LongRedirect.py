import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect",allow_redirects = True)

count_redirescts = len(response.history)
print(f"Всего редиректов: {count_redirescts}")

redirect = [count_redirescts-1]

redirect = response.history

for redirect in redirect:
 print(redirect.url)
 print(f"Статус-код: {redirect.status_code}")



