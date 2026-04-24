import requests

from models.pagination import PaginationResponse, HttpUrl


def test_users_pagination():
    response = requests.get(
        "https://reqres.in/api/users?page=1",
        headers={
            "x-api-key": "pub_2f34b8e56d29a23cae45fec15742468240ee46b2b59b965084aae7563daa6e3b"
        },
    )

    assert response.status_code == 200

    body = response.json()

    pagination = PaginationResponse(**body)

    users_count = len(pagination.data)
    assert users_count == pagination.per_page

    assert pagination.page == 1
    assert pagination.total_pages >= pagination.page

    # Если тест упадет, я увижу сообщение "Некорректный email"
    for user in pagination.data:
        assert "@" in user.email, "некорректный email"
