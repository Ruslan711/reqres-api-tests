from services.base_api import BaseAPI
from services.reqres_in.users.models.resource import SingleResourceResponse


class GetResource(BaseAPI):
    def __init__(self, env_config):
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)

    def get_resource(self, resource_id: int, validate: bool = True):
        url = f"{self.base_url}/unknown/{resource_id}"

        response = self.session.get(url)

        parsed = None
        if validate and response.status_code == 200:
            parsed = SingleResourceResponse.model_validate(response.json())

        return response, parsed