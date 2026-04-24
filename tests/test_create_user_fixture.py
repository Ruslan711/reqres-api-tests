import pytest
import requests
from faker import Faker
from pydantic import BaseModel
from datetime import datetime


fake = Faker()


class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: datetime


@pytest.fixture
def user_data():
    return {
        "name": fake.name(),
        "job": fake.job()
    }


def create_user(data):
    return requests.post(
        "https://reqres.in/api/users",
        json=data,
        headers={"x-api-key": "pub_2f34b8e56d29a23cae45fec15742468240ee46b2b59b965084aae7563daa6e3b"}
    )


def test_create_user(user_data):
    response = create_user(user_data)

    if response.status_code == 401:
        pytest.skip("Тут в случае 401 тест скипнется")

    assert response.status_code in [200, 201]

    body = response.json()
    user = CreateUserResponse(**body)

    assert user.name == user_data["name"]
    assert user.job == user_data["job"]
