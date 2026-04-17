import pytest
import requests
from pydantic import BaseModel


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


def get_user(user_id: int):
    return requests.get(
        f"https://reqres.in/api/users/{user_id}",
        headers={
            "x-api-key": "pub_2f34b8e56d29a23cae45fec15742468240ee46b2b59b965084aae7563daa6e3b"
        }
    )


@pytest.mark.parametrize("user_id, expected_status", [
    (1, 200),
    (2, 200),
    (3, 200),
    (384, 404),
])
def test_get_user_parametrized(user_id, expected_status):
    response = get_user(user_id)

    assert response.status_code == expected_status

    if expected_status == 200:
        body = response.json()["data"]
        user = UserData(**body)

        assert user.id == user_id
