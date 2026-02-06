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

    response_json = response.json()

    assert response.status_code == 200
    assert response_json["name"] == "Bob Smith"
    assert response_json["job"] == "Senior QA"
    assert "updatedAt" in response_json
    # 3. Проверь:
    # - Статус код 200
    # - Имя в ответе = "Bob Smith"
    # - Должность в ответе = "Senior QA"
    # - В ответе есть поле "updatedAt"
    pass