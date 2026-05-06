from services.base_api import BaseAPI
from services.reqres_in.users.models.user import CreateUserResponse


class CreateUser(BaseAPI):

    def __init__(self, env_config):
        super().__init__(
            base_url=env_config.reqres_url,
            api_key=env_config.reqres_api_key
        )

    def create_user(self, name: str, job: str, validate: bool = True):
        """Создание нового пользователя.

        Args:
            name (str): Имя пользователя
            job (str): Должность пользователя
        """

        response = self.session.post(
            f"{self.base_url}/users",
            json={"name": name, "job": job}
        )

        parsed = None
        if validate:
            parsed = CreateUserResponse.model_validate(response.json())

        return response, parsed