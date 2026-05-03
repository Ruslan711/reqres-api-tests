from services.reqres_in.users.get_user import GetUser
from models.user import User


def test_user_validation(env_config):
    user_id = 1

    response = GetUser(env_config).get_user(user_id)

    assert response.status_code == 200

    data = response.json()["data"]

    user = User(**data)

    assert user.id == user_id
