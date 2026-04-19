from faker import Faker
from models.user_update import UpdateUserRequest, UpdateUserResponse
from reqres_in.services.reqres_in.users.patch_update import UpdateUser

fake = Faker()


def test_update_user_faker(env_config):
    user_request = UpdateUserRequest(
        name=fake.name(),
        job=fake.job()
    )

    service = UpdateUser(env_config)

    payload = user_request.model_dump(exclude_none=True)

    response = service.update(
        user_id=2,
        name=payload["name"],
        job=payload["job"]
    )

    assert response.status_code == 200

    body = response.json()
    user_response = UpdateUserResponse(**body)

    assert user_response.name == user_request.name
    assert user_response.job == user_request.job
