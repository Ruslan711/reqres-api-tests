from services.reqres_in.users.patch_update import UpdateUser
from services.reqres_in.users.models.user import UpdateUserRequest


def test_update_user(env_config):

    request = UpdateUserRequest(name="Bob", job="QA")

    response, updated = UpdateUser(env_config).update(2, request)

    assert response.status_code == 200
    assert updated.name == "Bob"