from faker import Faker

from reqres_in.models.user_create import UserRequest, UserResponse
from reqres_in.models.user_update import UpdateUserRequest, UpdateUserResponse
from reqres_in.services.reqres_client import ReqresClient

fake = Faker()


def test_user_crud_faker():
    client = ReqresClient()

    create_request = UserRequest(
        name=fake.name(),
        job=fake.job()
    )

    create_response = client.create_user(
        data=create_request.model_dump()
    )

    assert create_response.status_code in (200, 201)

    created_user = UserResponse(**create_response.json())
    assert created_user.id is not None

    user_id = created_user.id


    get_response = client.get_user(user_id)
    assert get_response.status_code in (200, 404)


    update_request = UpdateUserRequest(
        name=fake.name(),
        job=fake.job()
    )

    update_response = client.update_user(
        user_id=user_id,
        data=update_request.model_dump(exclude_none=True)
    )

    assert update_response.status_code == 200

    updated_user = UpdateUserResponse(**update_response.json())
    assert updated_user.name == update_request.name
    assert updated_user.job == update_request.job


    delete_response = client.delete_user(user_id)
    assert delete_response.status_code == 204
