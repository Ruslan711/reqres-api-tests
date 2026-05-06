from faker import Faker

from services.reqres_in.users.post_create import CreateUser
from services.reqres_in.users.get_user import GetUser
from services.reqres_in.users.patch_update import UpdateUser
from services.reqres_in.users.delete_user import DeleteUser
from services.reqres_in.users.models.user import (
    CreateUserRequest,
    CreateUserResponse,
    UpdateUserRequest,
    UpdateUserResponse,
)

fake = Faker()


def test_user_crud_faker(env_config):
    create_request = CreateUserRequest(
        name=fake.name(),
        job=fake.job(),
    )

    create_response, created_user = CreateUser(env_config).create_user(
        name=create_request.name,
        job=create_request.job,
    )

    assert create_response.status_code in (200, 201)
    assert isinstance(created_user, CreateUserResponse)
    assert created_user.id is not None

    user_id = created_user.id

    get_response, _ = GetUser(env_config).get_user(user_id=user_id)

    assert get_response.status_code in (200, 404)
    if get_response.status_code == 200:
        body = get_response.json()
        assert body["data"]["id"] == user_id

    update_request = UpdateUserRequest(
        name=fake.name(),
        job=fake.job(),
    )

    update_response, updated_user = UpdateUser(env_config).update(
        user_id=user_id,
        request=update_request,
    )

    assert update_response.status_code == 200
    assert isinstance(updated_user, UpdateUserResponse)
    assert updated_user.name == update_request.name
    assert updated_user.job == update_request.job

    delete_response = DeleteUser(env_config).delete(user_id=user_id)
    assert delete_response.status_code == 204