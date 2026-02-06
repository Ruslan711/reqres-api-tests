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
    assert response.status_code == 204
    pass