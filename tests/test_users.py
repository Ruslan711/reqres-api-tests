import allure
import pytest

from utils.helper import attach_response
from services.reqres_in.users.get_users import GetUsers
from services.reqres_in.users.get_user import GetUser
from services.reqres_in.users.create_user import CreateUser
from services.reqres_in.users.put_update_user import UpdateUserPut
from services.reqres_in.users.patch_update_user import UpdateUserPatch
from services.reqres_in.users.delete_user import DeleteUser
from services.reqres_in.users.models.user import (
    UsersListResponse,
    SingleUserResponse,
    CreateUserRequest,
    CreateUserResponse,
    UpdateUserRequest,
    UpdateUserResponse,
)


@allure.feature("Users")
@allure.title("Получение списка пользователей")
@pytest.mark.regression
def test_get_users_list(env_config):
    with allure.step("Отправляю запрос на список пользователей page=2"):
        response, users = GetUsers(env_config).get_users(page=2)
        attach_response(response)

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
@pytest.mark.smoke
@pytest.mark.regression
def test_get_single_user(env_config):
    with allure.step("Запрашиваю пользователя по ID=2"):
        response, user = GetUser(env_config).get_user(user_id=2)
        attach_response(response)

    with allure.step("Проверяю статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяю Pydantic модель"):
        assert isinstance(user, SingleUserResponse)

    with allure.step("Проверяю данные пользователя"):
        assert user.data.id == 2


@allure.feature("Users")
@allure.title("Получение несуществующего пользователя")
@pytest.mark.regression
def test_get_user_not_found(env_config):
    with allure.step("Запрашиваю несуществующего пользователя"):
        response, user = GetUser(env_config).get_user(user_id=23)
        attach_response(response)

    with allure.step("Проверяю статус-код 404"):
        assert response.status_code == 404

    with allure.step("Проверяю, что ответ пустой"):
        assert user is None


@allure.feature("Users")
@allure.title("Создание пользователя")
@pytest.mark.smoke
@pytest.mark.regression
def test_create_user(env_config, delete_user):
    request = CreateUserRequest(
        name="morpheus",
        job="leader",
    )

    with allure.step("Создаю пользователя"):
        response, created = CreateUser(env_config).create_user(request=request)
        attach_response(response)

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
@pytest.mark.regression
def test_update_user_put(env_config, delete_user):
    create_request = CreateUserRequest(
        name="morpheus",
        job="leader",
    )

    with allure.step("Создаю пользователя для обновления"):
        create_response, created = CreateUser(env_config).create_user(
            request=create_request,
        )
        attach_response(create_response)

    with allure.step("Проверяю, что пользователь создан"):
        assert create_response.status_code == 201
        assert isinstance(created, CreateUserResponse)
        assert created.id is not None

    with allure.step("Регистрирую пользователя для последующего удаления"):
        delete_user.append(created.id)

    update_request = UpdateUserRequest(name="neo", job="chosen one")

    with allure.step("Отправляю PUT запрос на обновление пользователя"):
        response, updated = UpdateUserPut(env_config).update(
            user_id=created.id,
            request=update_request,
        )
        attach_response(response)

    with allure.step("Проверяю статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяю Pydantic модель"):
        assert isinstance(updated, UpdateUserResponse)

    with allure.step("Проверяю значения полей"):
        assert updated.name == "neo"
        assert updated.job == "chosen one"


@allure.feature("Users")
@allure.title("Обновление пользователя PATCH")
@pytest.mark.regression
def test_update_user_patch(env_config, delete_user):
    create_request = CreateUserRequest(
        name="morpheus",
        job="leader",
    )

    with allure.step("Создаю пользователя для частичного обновления"):
        create_response, created = CreateUser(env_config).create_user(
            request=create_request,
        )
        attach_response(create_response)

    with allure.step("Проверяю, что пользователь создан"):
        assert create_response.status_code == 201
        assert isinstance(created, CreateUserResponse)
        assert created.id is not None

    with allure.step("Регистрирую пользователя для последующего удаления"):
        delete_user.append(created.id)

    update_request = UpdateUserRequest(job="zion resident")

    with allure.step("Отправляю PATCH запрос на обновление пользователя"):
        response, updated = UpdateUserPatch(env_config).update(
            user_id=created.id,
            request=update_request,
        )
        attach_response(response)

    with allure.step("Проверяю статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяю Pydantic модель"):
        assert isinstance(updated, UpdateUserResponse)

    with allure.step("Проверяю значения полей"):
        assert updated.job == "zion resident"


@allure.feature("Users")
@allure.title("Удаление пользователя")
@pytest.mark.regression
def test_delete_user(env_config):
    create_request = CreateUserRequest(
        name="morpheus",
        job="leader",
    )

    with allure.step("Создаю пользователя для удаления"):
        create_response, created = CreateUser(env_config).create_user(
            request=create_request,
        )
        attach_response(create_response)

    with allure.step("Проверяю, что пользователь создан"):
        assert create_response.status_code == 201
        assert isinstance(created, CreateUserResponse)
        assert created.id is not None

    with allure.step("Удаляю пользователя"):
        delete_response = DeleteUser(env_config).delete(user_id=created.id)
        attach_response(delete_response)

    with allure.step("Проверяю статус-код удаления"):
        assert delete_response.status_code == 204

    with allure.step("Проверяю, что пользователь больше не существует"):
        get_response, user = GetUser(env_config).get_user(user_id=created.id)
        attach_response(get_response)

        assert get_response.status_code == 404
        assert user is None