import allure
import pytest

from utils.helper import attach_response
from services.reqres_in.auth.models.auth import (
    RegisterRequest,
    RegisterResponse,
    LoginRequest,
    LoginResponse,
    ErrorResponse,
)
from services.reqres_in.auth.register_user import RegisterUser
from services.reqres_in.auth.login_user import LoginUser


@allure.feature("Authentication")
@allure.title("Успешная регистрация пользователя")
@pytest.mark.smoke
@pytest.mark.regression
def test_register_success(env_config):
    request = RegisterRequest(
        email="eve.holt@reqres.in",
        password="pistol",
    )

    with allure.step("Делаю запрос на регистрацию"):
        response, result = RegisterUser(env_config).register(request=request)
        attach_response(response)

    with allure.step("Проверяю, что регистрация прошла успешно"):
        assert response.status_code == 200
        assert isinstance(result, RegisterResponse)
        assert result.id is not None
        assert isinstance(result.token, str)


@allure.feature("Authentication")
@allure.title("Неуспешная регистрация без пароля")
@pytest.mark.regression
def test_register_missing_password(env_config):
    request = RegisterRequest(
        email="lyani.costales@horizonspost.com",
        password="",
    )

    with allure.step("Пробую зарегистрироваться без пароля"):
        response, result = RegisterUser(env_config).register(request=request)
        attach_response(response)

    with allure.step("Проверяю, что получили ошибку"):
        assert response.status_code == 400
        assert isinstance(result, ErrorResponse)
        assert isinstance(result.error, str)
        assert result.error.strip() != ""


@allure.feature("Authentication")
@allure.title("Успешный вход пользователя")
@pytest.mark.smoke
@pytest.mark.regression
def test_login_success(env_config):
    request = LoginRequest(
        email="eve.holt@reqres.in",
        password="cityslicka",
    )

    with allure.step("Делаю запрос на логин"):
        response, result = LoginUser(env_config).login(request=request)
        attach_response(response)

    with allure.step("Проверяю, что логин успешный"):
        assert response.status_code == 200
        assert isinstance(result, LoginResponse)
        assert isinstance(result.token, str)


@allure.feature("Authentication")
@allure.title("Неуспешный вход без пароля")
@pytest.mark.regression
def test_login_missing_password(env_config):
    request = LoginRequest(
        email="lyani.costales@horizonspost.com",
        password="",
    )

    with allure.step("Пробую войти без пароля"):
        response, result = LoginUser(env_config).login(request=request)
        attach_response(response)

    with allure.step("Проверяю, что получили ошибку"):
        assert response.status_code == 400
        assert isinstance(result, ErrorResponse)
        assert isinstance(result.error, str)
        assert result.error.strip() != ""