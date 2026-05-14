from services.base_api import BaseAPI
from services.reqres_in.auth.models.auth import (
    RegisterRequest,
    RegisterResponse,
    ErrorResponse,
)


class RegisterUser(BaseAPI):
    def __init__(self, env_config):
        super().__init__(
            base_url=env_config.reqres_url,
            api_key=env_config.reqres_api_key,
        )

    def register(self, request: RegisterRequest, validate: bool = True):
        url = f"{self.base_url}/register"

        response = self.session.post(url, json=request.model_dump())

        parsed = None

        if validate:
            if response.status_code == 200:
                parsed = RegisterResponse.model_validate(response.json())
            elif response.status_code == 400:
                parsed = ErrorResponse.model_validate(response.json())

        return response, parsed