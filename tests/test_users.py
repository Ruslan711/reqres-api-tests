import allure
import pytest

from utils.helper import Helper
from services.reqres_in.users.get_users import GetUsers
from services.reqres_in.users.get_user import GetUser
from services.reqres_in.users.create_user import CreateUser
from services.reqres_in.users.put_update_user import UpdateUserPut
from services.reqres_in.users.patch_update_user import UpdateUserPatch
from services.reqres_in.users.delete_user import DeleteUser
from services.reqres_in.users.models.user import (
    UsersListResponse,
    SingleUserResponse,
    CreateUserResponse,
    UpdateUserRequest,
    UpdateUserResponse,
)


@allure.feature("Users")
@allure.title("Получение списка пользователей")
@allure.testcase("https://example.com/tc-get-users", "TC-GET-USERS")
@pytest.mark.regression
def test_get_users_list(env_config):
    helper = Helper()

    with allure.step("Отправляю запрос на список пользователей page=2"):
        response, users = GetUsers(env_config).get_users(page=2)
        helper.attach_response(response)

    with allure.step("Проверяю статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяю Pydantic модель ответа"):
        assert isinstance(users, UsersListResponse)

    with allure.step("Проверяю значения полей"):
        assert users.page == 2
        assert users.per_page > 0
        assert isinstance(users.data, list)


@allure.feature("Users")
@allure.title("Получение одного пользователя по ID")
@allure.testcase("https://example.com/tc-get-user", "TC-GET-USER")
@pytest.mark.smoke
@pytest.mark.regression
def test_get_single_user(env_config):
    helper = Helper()

    with allure.step("Запрашиваю пользователя по ID=2"):
        response, user = GetUser(env_config).get_user(user_id=2)
        helper.attach_response(response)

    with allure.step("Проверяю статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяю Pydantic модель"):
        assert isinstance(user, SingleUserResponse)

    with allure.step("Проверяю данные пользователя"):
        assert user.data.id == 2



@allure.feature("Users")
@allure.title("Получение несуществующего пользователя")
@allure.testcase("https://example.com/tc-get-user-404", "TC-GET-USER-404")
@pytest.mark.regression
def test_get_user_not_found(env_config):
    helper = Helper()

    with allure.step("Запрашиваю несуществующего пользователя"):
        response, user = GetUser(env_config).get_user(user_id=23)
        helper.attach_response(response)

    with allure.step("Проверяю статус-код 404"):
        assert response.status_code == 404

    with allure.step("Проверяю, что ответ пустой"):
        assert user is None


@allure.feature("Users")
@allure.title("Создание пользователя")
@allure.testcase("https://example.com/tc-create-user", "TC-CREATE-USER")
@pytest.mark.smoke
@pytest.mark.regression
def test_create_user(env_config, delete_user):
    helper = Helper()

    with allure.step("Создаю пользователя"):
        response, created = CreateUser(env_config).create_user(
            name="morpheus",
            job="leader",
        )
        helper.attach_response(response)

    with allure.step("Сохраняю пользователя для удаления"):
        if created and created.id:
            delete_user.append(created.id)

    with allure.step("Проверяю статус-код"):
        assert response.status_code == 201

    with allure.step("Проверяю Pydantic модель"):
        assert isinstance(created, CreateUserResponse)

    with allure.step("Проверяю значения полей"):
        assert created.name == "morpheus"
        assert created.job == "leader"



@allure.feature("Users")
@allure.title("Обновление пользователя PUT")
@allure.testcase("https://example.com/tc-update-user-put", "TC-UPDATE-USER-PUT")
@pytest.mark.regression
def test_update_user_put(env_config):
    helper = Helper()

    request = UpdateUserRequest(name="neo", job="chosen one")

    with allure.step("Отправляю PUT запрос"):
        response, updated = UpdateUserPut(env_config).update(
            user_id=2,
            request=request,
        )
        helper.attach_response(response)

    with allure.step("Проверяю статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяю Pydantic модель"):
        assert isinstance(updated, UpdateUserResponse)

    with allure.step("Проверяю значения полей"):
        assert updated.name == "neo"
        assert updated.job == "chosen one"



@allure.feature("Users")
@allure.title("Обновление пользователя PATCH")
@allure.testcase("https://example.com/tc-update-user-patch", "TC-UPDATE-USER-PATCH")
@pytest.mark.regression
def test_update_user_patch(env_config):
    helper = Helper()

    request = UpdateUserRequest(job="zion resident")

    with allure.step("Отправляю PATCH запрос"):
        response, updated = UpdateUserPatch(env_config).update(
            user_id=2,
            request=request,
        )
        helper.attach_response(response)

    with allure.step("Проверяю статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяю Pydantic модель"):
        assert isinstance(updated, UpdateUserResponse)

    with allure.step("Проверяю значения полей"):
        assert updated.job == "zion resident"



@allure.feature("Users")
@allure.title("Удаление пользователя")
@allure.testcase("https://example.com/tc-delete-user", "TC-DELETE-USER")
@pytest.mark.regression
def test_delete_user(env_config):
    helper = Helper()

    with allure.step("Удаляю пользователя"):
        response = DeleteUser(env_config).delete(user_id=2)
        helper.attach_response(response)

    with allure.step("Проверяю статус-код"):
        assert response.status_code == 204

    with allure.step("Проверяю тело ответа"):
        assert response.text == ""