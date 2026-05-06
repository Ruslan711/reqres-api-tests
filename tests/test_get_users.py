from services.reqres_in.users.get_users import GetUsers


def test_get_users(env_config):

    response, users = GetUsers(env_config).get_users(page=1)

    assert response.status_code == 200
    assert users.page == 1