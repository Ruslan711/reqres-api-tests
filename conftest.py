import pytest

from config.environments import Environment, environments, EnvironmentConfig


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="stage"
    )


@pytest.fixture(scope="session")
def env(request) -> Environment:
    return Environment(request.config.getoption("--env").lower())


@pytest.fixture(scope="session")
def env_config(env) -> EnvironmentConfig:
    return environments[env]


@pytest.fixture(scope="function")
def user_data():
    return {"id": None}


@pytest.fixture(scope="function")
def created_users(env_config):
    ids = []
    yield ids

    from services.reqres_in.users.delete_user import DeleteUser

    for user_id in ids:
        try:
            DeleteUser(env_config).delete(user_id)
        except Exception as e:
            print("Delete error:", e)