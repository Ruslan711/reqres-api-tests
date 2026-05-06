from services.reqres_in.users.post_create import CreateUser


def test_create_user(env_config, created_users):

    response, user = CreateUser(env_config).create_user(
        name="John",
        job="QA"
    )

    assert response.status_code == 201
    assert user.name == "John"

    created_users.append(user.id)