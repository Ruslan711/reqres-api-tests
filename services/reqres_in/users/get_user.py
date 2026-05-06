from services.base_api import BaseAPI
from services.reqres_in.users.models.user import SingleUserResponse


class GetUser(BaseAPI):

    def __init__(self, env_config):
        super().__init__(
            base_url=env_config.reqres_url,
            api_key=env_config.reqres_api_key
        )

    def get_user(self, user_id: int):
        """Получение пользователя по ID.

        Args:
            user_id (int): ID пользователя

        Returns:
            requests.Response: Ответ от сервера
        """

        response = self.session.get(
            f"{self.base_url}/users/{user_id}"
        )

        parsed = None
        if response.status_code == 200:
            parsed = SingleUserResponse.model_validate(response.json())

        return response, parsed