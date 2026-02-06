from services.reqres_in.users.get_user import GetUser


def test_get_user(env_config):
    user_id = 2  # Используем существующего пользователя

    response = GetUser(env_config).get_user(user_id)

    # Проверь:
    # 1. Статус код должен быть 200
    # 2. В ответе должен быть объект "data"
    # 3. ID в ответе должен совпадать с запрошенным
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id
