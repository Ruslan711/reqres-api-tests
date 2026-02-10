Урок 1: Домашнее задание
Что мы сделали на уроке
На уроке мы создали базовую структуру фреймворка для тестирования REST API:

reqres_in/
├── config/
│   └── environments.py      # Настройки окружений
├── services/
│   ├── base_api.py          # Базовый класс API
│   └── reqres_in/
│       └── users/
│           └── post_create.py  # POST /users (создание)
├── tests/
│   └── test_create_user.py  # Тест создания
├── conftest.py              # Фикстуры pytest
├── requirements.txt
├── .env.example
└── .env
Мы реализовали: - Метод POST /users — создание пользователя - Тест для этого метода





Твоя задача
Реализовать остальные методы API и написать тесты для них.

Методы для реализации
Метод	Эндпоинт	Описание	Файл
GET	/users/{id}	Получить пользователя по ID	get_user.py
PATCH	/users/{id}	Обновить данные пользователя	patch_update.py
DELETE	/users/{id}	Удалить пользователя	delete_user.py



Пошаговая инструкция
Шаг 1: Создай класс GetUser
Создай файл services/reqres_in/users/get_user.py:

from services.base_api import BaseAPI


class GetUser(BaseAPI):

    def __init__(self, env_config):
        # Вызови конструктор родителя, передав URL и API ключ
        # Подсказка: посмотри как это сделано в post_create.py
        pass

    def get_user(self, user_id: int):
        """Получение пользователя по ID.

        Args:
            user_id (int): ID пользователя

        Returns:
            requests.Response: Ответ от сервера
        """
        # Отправь GET-запрос на /users/{user_id}
        # Подсказка: self.session.get(url)
        pass
Шаг 2: Напиши тест для GetUser
Создай файл tests/test_get_user.py:

from services.reqres_in.users.get_user import GetUser


def test_get_user(env_config):
    user_id = 2  # Используем существующего пользователя

    response = GetUser(env_config).get_user(user_id)

    # Проверь:
    # 1. Статус код должен быть 200
    # 2. В ответе должен быть объект "data"
    # 3. ID в ответе должен совпадать с запрошенным
    pass
Шаг 3: Создай класс UpdateUser
Создай файл services/reqres_in/users/patch_update.py:

from services.base_api import BaseAPI


class UpdateUser(BaseAPI):

    def __init__(self, env_config):
        # Твой код здесь
        pass

    def update(self, user_id: int, name: str, job: str):
        """Обновление данных пользователя.

        Args:
            user_id (int): ID пользователя
            name (str): Новое имя
            job (str): Новая должность

        Returns:
            requests.Response: Ответ от сервера
        """
        # Отправь PATCH-запрос с данными {"name": name, "job": job}
        # Подсказка: self.session.patch(url, json=data)
        pass
Шаг 4: Напиши тест для UpdateUser
Создай файл tests/test_update_user.py:

from services.reqres_in.users.post_create import CreateUser
from services.reqres_in.users.patch_update import UpdateUser


def test_update_user(env_config):
    # 1. Сначала создай пользователя
    create_response = CreateUser(env_config).create_user(
        name="John Doe",
        job="QA Engineer"
    )
    user_id = create_response.json()["id"]

    # 2. Обнови его данные
    response = UpdateUser(env_config).update(
        user_id=user_id,
        name="Bob Smith",
        job="Senior QA"
    )

    # 3. Проверь:
    # - Статус код 200
    # - Имя в ответе = "Bob Smith"
    # - Должность в ответе = "Senior QA"
    # - В ответе есть поле "updatedAt"
    pass
Шаг 5: Создай класс DeleteUser
Создай файл services/reqres_in/users/delete_user.py:

from services.base_api import BaseAPI


class DeleteUser(BaseAPI):

    def __init__(self, env_config):
        # Твой код здесь
        pass

    def delete(self, user_id: int):
        """Удаление пользователя.

        Args:
            user_id (int): ID пользователя

        Returns:
            requests.Response: Ответ от сервера
        """
        # Отправь DELETE-запрос
        # Подсказка: self.session.delete(url)
        pass
Шаг 6: Напиши тест для DeleteUser
Создай файл tests/test_delete_user.py:

from services.reqres_in.users.post_create import CreateUser
from services.reqres_in.users.delete_user import DeleteUser


def test_delete_user(env_config):
    # 1. Создай пользователя
    create_response = CreateUser(env_config).create_user(
        name="To Delete",
        job="Temporary"
    )
    user_id = create_response.json()["id"]

    # 2. Удали его
    response = DeleteUser(env_config).delete(user_id)

    # 3. Проверь:
    # - Статус код должен быть 204 (No Content)
    pass


Справочник HTTP-кодов
Код	Название	Когда используется
200	OK	GET, PATCH — успешное выполнение
201	Created	POST — ресурс создан
204	No Content	DELETE — ресурс удалён
400	Bad Request	Неверные данные в запросе
401	Unauthorized	Нет авторизации (проверь API ключ)
404	Not Found	Ресурс не найден


Справочник методов requests
# GET-запрос
response = self.session.get(url)

# POST-запрос с JSON
response = self.session.post(url, json={"key": "value"})

# PATCH-запрос с JSON
response = self.session.patch(url, json={"key": "value"})

# DELETE-запрос
response = self.session.delete(url)

# Получить статус код
response.status_code  # 200, 201, 204 и т.д.

# Получить тело ответа как JSON
response.json()  # {"data": {...}}

# Получить тело ответа как текст
response.text  # '{"data": {...}}'



Как проверить работу
Запуск всех тестов
pytest -v
Запуск одного теста
pytest tests/test_get_user.py -v
Запуск с подробным выводом при ошибке
pytest -v --tb=short
Итоговая структура после выполнения ДЗ
reqres_in/
├── config/
│   └── environments.py
├── services/
│   ├── base_api.py
│   └── reqres_in/
│       └── users/
│           ├── post_create.py   # POST — создали на уроке
│           ├── get_user.py      # GET — твоя реализация
│           ├── patch_update.py  # PATCH — твоя реализация
│           └── delete_user.py   # DELETE — твоя реализация
├── tests/
│   ├── test_create_user.py      # Создали на уроке
│   ├── test_get_user.py         # Твой тест
│   ├── test_update_user.py      # Твой тест
│   └── test_delete_user.py      # Твой тест
├── conftest.py
├── requirements.txt
├── .env.example
└── .env


Критерии выполнения
 Все 4 теста проходят успешно (pytest -v показывает 4 passed)
 Каждый класс находится в отдельном файле
 Код написан по аналогии с post_create.py
 Используются правильные HTTP-методы (GET, PATCH, DELETE)
 Проверяются корректные статус-коды
Частые ошибки
ImportError: No module named 'services'
Решение: Запускай pytest из корня проекта (папка reqres_in)

401 Unauthorized
Решение: Проверь, что файл .env существует и содержит правильный ключ

AssertionError
Решение: Посмотри, что реально возвращает API:

print(response.json())
print(response.status_code)
Бонусное задание (необязательно)
Если хочешь потренироваться больше:

Добавь негативные тесты: - Попробуй получить несуществующего пользователя (ID = 999) - Ожидаемый результат: статус 404

Добавь тест на список пользователей: - GET /users — возвращает список - Проверь, что в ответе есть массив "data"

Удачи! На следующем уроке мы добавим Pydantic для валидации и Allure для красивых отчётов.
