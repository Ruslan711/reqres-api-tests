import requests
import pytest
from unittest.mock import patch


def process_user_data(user_id: int):
    response = requests.get(f"https://reqres.in/api/users/{user_id}")

    if response.status_code != 200:
        return {"status": "error", "code": response.status_code}

    data = response.json()["data"]

    return {
        "status": "success",
        "user_id": data["id"],
        "email": data["email"]
    }


@patch("requests.get")
def test_user_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "data": {
            "id": 2,
            "email": "lyani.costales@horizonspost.com"
        }
    }

    result = process_user_data(2)

    assert result["status"] == "success"
    assert result["user_id"] == 2
    assert result["email"] == "lyani.costales@horizonspost.com"


@patch("requests.get")
def test_user_error(mock_get):
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = {}

    result = process_user_data(325)

    assert result["status"] == "error"
    assert result["code"] == 404
