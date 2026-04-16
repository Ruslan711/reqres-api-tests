import requests
from faker import Faker

import pytest

from reqres_in.models.user_create import UserRequest, UserResponse
from reqres_in.models.user_update import UpdateUserRequest, UpdateUserResponse

fake = Faker()

def test_user_crud_faker():
    name = fake.name()
    job = fake.job()

    create_request = UserRequest(name=name, job=job)

    create_response = requests.post(
        "https://reqres.in/api/users",
        json=create_request.dict(),
    )

    if create_response.status_code == 401:
        pytest.skip("Если вернётся 401, пропускаем тест")

    assert create_response.status_code in [200, 201]

    created_body = create_response.json()
    created_user = UserResponse(**created_body)

    assert created_user.id is not None
    assert created_user.createdAt is not None

    user_id = created_user.id

    get_response = requests.get(f"https://reqres.in/api/users/{user_id}")

    assert get_response.status_code in [200, 404]

    new_name = fake.name()
    new_job = fake.job()

    update_request = UpdateUserRequest(
        name=new_name,
        job=new_job
    )

    update_response = requests.patch(
        f"https://reqres.in/api/users/{user_id}",
        json=update_request.dict(exclude_none=True),
    )

    assert update_response.status_code == 200

    updated_body = update_response.json()
    updated_user = UpdateUserResponse(**updated_body)

    assert updated_user.name == new_name
    assert updated_user.job == new_job

    delete_response = requests.delete(
        f"https://reqres.in/api/users/{user_id}"
    )

    print("DELETE STATUS:", delete_response.status_code)

    assert delete_response.status_code == 204

