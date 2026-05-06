from services.reqres_in.users.get_user import GetUser
from services.reqres_in.users.models.user import UserData


def test_user_validation(env_config):
    user_id = 1

    response, _ = GetUser(env_config).get_user(user_id)

    assert response.status_code == 200

    data = response.json()["data"]

    user = UserData.model_validate(data)

    assert user.id == user_id