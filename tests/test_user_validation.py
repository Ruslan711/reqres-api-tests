import requests

from models.user import User


def test_user_validation():
    # 1. Получите данные пользователя (id=1) через GET
    response = requests.get(
        "https://reqres.in/api/users/1",
        headers={
            "x-api-key": "pub_2f34b8e56d29a23cae45fec15742468240ee46b2b59b965084aae7563daa6e3b"
        },
    )

    assert response.status_code == 200

    # 2. Создайте экземпляр модели из данных
    data = response.json()["data"]
    user = User(**data)

    # 3. Проверьте корректность типов
    assert type(user.id) is int
    assert type(user.email) is str
    assert type(user.first_name) is str
    assert type(user.last_name) is str
    assert type(user.avatar) is str
