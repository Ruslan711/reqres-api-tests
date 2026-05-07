from services.base_api import BaseAPI
from services.reqres_in.users.models.user import UpdateUserRequest, UpdateUserResponse


class UpdateUserPatch(BaseAPI):

    def __init__(self, env_config):
        super().__init__(
            base_url=env_config.reqres_url,
            api_key=env_config.reqres_api_key
        )

    def update(self, user_id: int, request: UpdateUserRequest, validate: bool = True):
        """Частичное обновление данных пользователя (PATCH).

        Args:
            user_id (int): ID пользователя
            request (UpdateUserRequest): данные для частичного обновления
            validate (bool): валидировать ли ответ через Pydantic
        """

        response = self.session.patch(
            f"{self.base_url}/users/{user_id}",
            json=request.model_dump(exclude_none=True)
        )

        parsed = None
        if validate and response.status_code == 200:
            parsed = UpdateUserResponse.model_validate(response.json())

        return response, parsed