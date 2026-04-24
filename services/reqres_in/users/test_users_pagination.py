from models.pagination import PaginationResponse
from services.reqres_in.users.get_users import GetUsers


def test_users_pagination(env_config):
    response = GetUsers(env_config).get_users(page=1)

    assert response.status_code == 200

    pagination = PaginationResponse(**response.json())

    assert len(pagination.data) == pagination.per_page
    assert pagination.page == 1
    assert pagination.total_pages >= pagination.page
