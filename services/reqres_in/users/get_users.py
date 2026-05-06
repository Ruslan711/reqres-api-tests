from services.base_api import BaseAPI
from services.reqres_in.users.models.user import UsersListResponse


class GetUsers(BaseAPI):

    def __init__(self, env_config):
        super().__init__(
            base_url=env_config.reqres_url,
            api_key=env_config.reqres_api_key
        )

    def get_users(self, page: int = 1, validate: bool = True):
        url = f"{self.base_url}/users"
        params = {"page": page}

        response = self.session.get(url, params=params)

        parsed = None
        if validate:
            parsed = UsersListResponse.model_validate(response.json())

        return response, parsed