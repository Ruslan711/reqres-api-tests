import allure
import pytest

from utils.helper import Helper
from services.reqres_in.resources.get_resources import GetResources
from services.reqres_in.resources.get_resource import GetResource
from services.reqres_in.resources.models.resource import (
    ResourcesListResponse,
    SingleResourceResponse,
)


@allure.feature("Resources")
@allure.title("Получаю список ресурсов")
@allure.testcase("https://example.com/tc-get-resources-list", "TC-GET-RESOURCES-LIST")
@pytest.mark.regression
def test_get_resources_list(env_config):
    helper = Helper()

    with allure.step("Запрашиваю список ресурсов"):
        response, resources = GetResources(env_config).get_resources(page=2)
        helper.attach_response(response)

    with allure.step("Проверяю статус-код ответа"):
        assert response.status_code == 200

    with allure.step("Проверяю структуру и данные"):
        assert isinstance(resources, ResourcesListResponse)
        assert resources.page == 1
        assert len(resources.data) > 0
        first = resources.data[0]
        assert first.id is not None
        assert first.name != ""


@allure.feature("Resources")
@allure.title("Получение одного ресурса по ID")
@allure.testcase("https://example.com/tc-get-resource", "TC-GET-RESOURCE")
@pytest.mark.regression
def test_get_single_resource(env_config):
    helper = Helper()

    with allure.step("Запрашиваем ресурс с ID = 2"):
        response, resource = GetResource(env_config).get_resource(resource_id=2)
        helper.attach_response(response)

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200

    with allure.step("Проверяем структуру и данные"):
        assert isinstance(resource, SingleResourceResponse)
        assert resource.data.id == 2
        assert resource.data.name != ""


@allure.feature("Resources")
@allure.title("Получение несуществующего ресурса")
@allure.testcase("https://example.com/tc-get-resource-404", "TC-GET-RESOURCE-404")
@pytest.mark.regression
def test_get_resource_not_found(env_config):
    helper = Helper()

    with allure.step("Запрашиваем несуществующий ресурс"):
        response, resource = GetResource(env_config).get_resource(resource_id=23)
        helper.attach_response(response)

    with allure.step("Проверяем статус-код 404"):
        assert response.status_code == 404

    with allure.step("Проверяем, что тело не валидируем моделью"):
        assert resource is None