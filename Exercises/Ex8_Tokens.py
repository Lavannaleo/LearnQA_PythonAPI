import requests
import json
import time

key1 = "token"
key2 = "seconds"

status_not_ready = "Job is NOT ready"
status_ready = "Job is ready"

##  Создаем JOB

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print("1. Job создан")
obj = json.loads(response.text)

if key1 in obj:
    token = obj[key1]
    print(f"Токен: {token}")
    if key2 in obj:
        sec = obj[key2]
        print(f"JOB будет выполняться: {sec} сек")

        ## Отправляем запрос до завершения JOB

        response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
        print("2. Запрос ДО выполнения Job отправлен")
        obj = json.loads(response.text)
    else:
        print(f"Ключа {key2} нет в ответе")
else:
    print(f"Ключа {key1} нет в ответе")

key3 = "error"
key4 = "status"
key5 = "result"

if key3 in obj:
    error = obj[key3]
    print(f"Ошибка: {error}. Запустите скрипт заново")
    exit(0)
else:
    print(f"Ключа {key3} нет в ответе")

if key4 in obj:
    status = obj[key4]
    if status == status_not_ready:
        print(f"Статус JOB: {status}")
        print(f"3. Жду {sec} сек")

        ## Ждем выполнения JOB

        time.sleep(sec)

        ## Отправляем запрос после выполнения JOB

        response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
        print("4. Запрос ПОСЛЕ выполнения Job отправлен")
        obj = json.loads(response.text)
else:
    print(f"Ключа {key4} нет в ответе")

if key5 in obj:
    status = obj[key4]
    result = obj[key5]
    if status == status_ready:
        print(f"Статус JOB: {status}")
        print(f"Результат JOB: {result}")
else:
    print(f"Ключа {key5} нет в ответе")
