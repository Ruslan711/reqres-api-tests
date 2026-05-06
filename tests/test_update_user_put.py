from services.reqres_in.users.update_user import UpdateUserPut
from services.reqres_in.users.models.user import UpdateUserRequest


def test_update_user_put(env_config):

    request = UpdateUserRequest(name="Alice", job="Lead QA")

    response, updated = UpdateUserPut(env_config).update(2, request)

    assert response.status_code == 200
    assert updated.name == "Alice"