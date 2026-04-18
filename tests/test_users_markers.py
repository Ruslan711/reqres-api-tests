import pytest
import requests
import os


HEADERS = {
    "x-api-key": "pub_2f34b8e56d29a23cae45fec15742468240ee46b2b59b965084aae7563daa6e3b"
}


@pytest.mark.smoke
def test_get_user_list():
    response = requests.get(
        "https://reqres.in/api/users?page=2",
        headers=HEADERS
    )

    if response.status_code == 401:
        pytest.skip("нет доступа к API (401)")

    assert response.status_code == 200
    assert "data" in response.json()


@pytest.mark.regression
def test_create_user():
    payload = {
        "name": "John",
        "job": "QA Engineer"
    }

    response = requests.post(
        "https://reqres.in/api/users",
        json=payload,
        headers=HEADERS
    )

    if response.status_code == 401:
        pytest.skip("нет доступа к API (401)")

    assert response.status_code in [200, 201]
    assert response.json()["name"] == payload["name"]


@pytest.mark.regression
def test_update_user():
    if not os.getenv("UPDATE_TESTS"):
        pytest.skip("переменная не задана UPDATE_TESTS")

    payload = {
        "name": "Ruslan",
        "job": "QA"
    }

    response = requests.patch(
        "https://reqres.in/api/users/2",
        json=payload,
        headers=HEADERS
    )

    if response.status_code == 401:
        pytest.skip("нет доступа к API (401)")

    assert response.status_code == 200
    assert response.json()["name"] == payload["name"]
