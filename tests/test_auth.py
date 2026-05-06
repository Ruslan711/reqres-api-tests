import allure
import pytest

from utils.helper import Helper
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
@allure.testcase("https://example.com/tc-register-success", "TC-REGISTER-SUCCESS")
@pytest.mark.smoke
@pytest.mark.regression
def test_register_success(env_config):
    helper = Helper()

    request = RegisterRequest(
        email="eve.holt@reqres.in",
        password="pistol",
    )

    with allure.step("Делаю запрос на регистрацию"):
        response, success, error = RegisterUser(env_config).register(request=request)
        helper.attach_response(response)

    with allure.step("Проверяю, что регистрация прошла успешно"):
        assert response.status_code == 200
        assert isinstance(success, RegisterResponse)
        assert success.id is not None
        assert isinstance(success.token, str)
        assert error is None


@allure.feature("Authentication")
@allure.title("Неуспешная регистрация без пароля")
@allure.testcase("https://example.com/tc-register-fail", "TC-REGISTER-FAIL")
@pytest.mark.regression
def test_register_missing_password(env_config):
    helper = Helper()

    request = RegisterRequest(
        email="lyani.costales@horizonspost.com",
        password="",  # без пароля
    )

    with allure.step("Пробуюю зарегистрироваться без пароля"):
        response, success, error = RegisterUser(env_config).register(request=request)
        helper.attach_response(response)

    with allure.step("Проверяю, что получили ошибку"):
        assert response.status_code == 400
        assert success is None
        assert isinstance(error, ErrorResponse)
        assert "password" in error.error.lower()


@allure.feature("Authentication")
@allure.title("Успешный вход пользователя")
@allure.testcase("https://example.com/tc-login-success", "TC-LOGIN-SUCCESS")
@pytest.mark.smoke
@pytest.mark.regression
def test_login_success(env_config):
    helper = Helper()

    request = LoginRequest(
        email="eve.holt@reqres.in",
        password="cityslicka",
    )

    with allure.step("Делаю запрос на логин"):
        response, success, error = LoginUser(env_config).login(request=request)
        helper.attach_response(response)

    with allure.step("Проверяю, что логин успешный"):
        assert response.status_code == 200
        assert isinstance(success, LoginResponse)
        assert isinstance(success.token, str)
        assert error is None


@allure.feature("Authentication")
@allure.title("Неуспешный вход без пароля")
@allure.testcase("https://example.com/tc-login-fail", "TC-LOGIN-FAIL")
@pytest.mark.regression
def test_login_missing_password(env_config):
    helper = Helper()

    request = LoginRequest(
        email="lyani.costales@horizonspost.com",
        password="",
    )

    with allure.step("Пробую войти без пароля"):
        response, success, error = LoginUser(env_config).login(request=request)
        helper.attach_response(response)

    with allure.step("Проверяю, что получили ошибку"):
        assert response.status_code == 400
        assert success is None
        assert isinstance(error, ErrorResponse)
        assert "password" in error.error.lower()