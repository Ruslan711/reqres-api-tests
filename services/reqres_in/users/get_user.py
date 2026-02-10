from services.base_api import BaseAPI


class GetUser(BaseAPI):

    def __init__(self, env_config):
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)

    def get_user(self, user_id: int):
        """Получение пользователя по ID.

        Args:
            user_id (int): ID пользователя

        Returns:
            requests.Response: Ответ от сервера
        """
        url = f"{self.base_url}/users/{user_id}"
        response = self.session.get(url)
        return response
