from services.base_api import BaseAPI
from services.reqres_in.users.models.user import UpdateUserRequest, UpdateUserResponse


class UpdateUserPut(BaseAPI):

    def __init__(self, env_config):
        super().__init__(
            base_url=env_config.reqres_url,
            api_key=env_config.reqres_api_key
        )

    def update(self, user_id: int, request: UpdateUserRequest, validate: bool = True):
        response = self.session.put(
            f"{self.base_url}/users/{user_id}",
            json=request.model_dump(exclude_none=True)
        )

        parsed = None
        if validate and response.status_code == 200:
            parsed = UpdateUserResponse.model_validate(response.json())

        return response, parsed
