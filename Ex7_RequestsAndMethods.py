import  requests

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("1) GET-запрос")
print("Параметр в запросе: нет")
print(f"Текст ответа: {response.text}")
print(f"Статус-код ответа: {response.status_code}")

response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("2) HEAD-запрос")
print("Параметр в запросе: HEAD")
print(f"Текст ответа: {response.text}")
print(f"Статус-код ответа: {response.status_code}")

response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})
print("3) POST-запрос")
print("Параметр в запросе: POST")
print(f"Текст ответа: {response.text}")
print(f"Статус-код ответа: {response.status_code}")

methodType = {"GET", "POST", "DELETE", "PUT"}

print("4) Перебор вариантов параметров для GET-REQUEST")
methodType = {"GET", "POST", "DELETE", "PUT"}
for methodType in methodType:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": methodType})
    print(f"Параметр в запросе: {methodType}")
    print(f"Текст ответа: {response.text}")
    print(f"Статус-код ответа: {response.status_code}")

print("Перебор вариантов параметров для POST-REQUEST")
methodType = {"GET", "POST", "DELETE", "PUT"}
for methodType in methodType:
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": methodType})
    print(f"Параметр в запросе: {methodType}")
    print(f"Текст ответа: {response.text}")
    print(f"Статус-код ответа: {response.status_code}")

print("Перебор вариантов параметров для DELETE-REQUEST")
methodType = {"GET", "POST", "DELETE", "PUT"}
for methodType in methodType:
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": methodType})
    print(f"Параметр в запросе: {methodType}")
    print(f"Текст ответа: {response.text}")
    print(f"Статус-код ответа: {response.status_code}")

print("Перебор вариантов параметров для PUT-REQUEST")
methodType = {"GET", "POST", "DELETE", "PUT"}
for methodType in methodType:
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": methodType})
    print(f"Параметр в запросе: {methodType}")
    print(f"Текст ответа: {response.text}")
    print(f"Статус-код ответа: {response.status_code}")