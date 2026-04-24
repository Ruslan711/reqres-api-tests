import requests
from faker import Faker

from models.user_create import UserRequest, UserResponse


fake = Faker()


def test_create_user_faker():
    name = fake.name()
    job = fake.job()

    user_request = UserRequest(
        name=name,
        job=job
    )

    response = requests.post(
        "https://reqres.in/api/users",
        json=user_request.dict(),
        headers={
            "x-api-key": "pub_2f34b8e56d29a23cae45fec15742468240ee46b2b59b965084aae7563daa6e3b"
        },
    )

    assert response.status_code == 201

    body = response.json()

    user_response = UserResponse(**body)

    assert user_response.name == user_request.name
    assert user_response.job == user_request.job
