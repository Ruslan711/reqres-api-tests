from services.base_api import BaseAPI


class UpdateUser(BaseAPI):

    def __init__(self, env_config):
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)


    def update(self, user_id: int, name: str, job: str):
        """Обновление данных пользователя.

        Args:
            user_id (int): ID пользователя
            name (str): Новое имя
            job (str): Новая должность

        Returns:
            requests.Response: Ответ от сервера
        """
        url = f"{self.base_url}/users/{user_id}"
        data = {
            "name": name,
            "job": job
        }
        return self.session.patch(url, json=data)
