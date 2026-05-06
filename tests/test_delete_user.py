from services.reqres_in.users.delete_user import DeleteUser


def test_delete_user(env_config):

    response = DeleteUser(env_config).delete(2)

    assert response.status_code == 204