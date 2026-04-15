import requests
from faker import Faker
from models.user_update import UpdateUserRequest, UpdateUserResponse

fake = Faker()


def test_update_user_faker():
    name = fake.name()
    job = fake.job()

    user_request = UpdateUserRequest(
        name=name,
        job=job
    )

    response = requests.patch(
        "https://reqres.in/api/users/2",
        json=user_request.dict(exclude_none=True),
        headers={
            "x-api-key": "pub_2f34b8e56d29a23cae45fec15742468240ee46b2b59b965084aae7563daa6e3b"
        },
    )

    assert response.status_code == 200

    body = response.json()

    user_response = UpdateUserResponse(**body)

    assert user_response.name == user_request.name
    assert user_response.job == user_request.job
