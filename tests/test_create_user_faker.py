from faker import Faker

from services.reqres_in.users.post_create import CreateUser
from services.reqres_in.users.models.user import CreateUserRequest, CreateUserResponse

fake = Faker()


def test_create_user_faker(env_config):
    name = fake.name()
    job = fake.job()

    user_request = CreateUserRequest(
        name=name,
        job=job,
    )

    response, created_user = CreateUser(env_config).create_user(
        name=user_request.name,
        job=user_request.job,
    )

    assert response.status_code == 201
    assert isinstance(created_user, CreateUserResponse)

    assert created_user.name == user_request.name
    assert created_user.job == user_request.job
    assert created_user.id is not None
    assert created_user.createdAt is not None