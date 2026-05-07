from services.base_api import BaseAPI
from services.reqres_in.auth.models.auth import (
    LoginRequest,
    LoginResponse,
    ErrorResponse,
)


class LoginUser(BaseAPI):
    def __init__(self, env_config):
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)

    def login(self, request: LoginRequest, validate: bool = True):
        url = f"{self.base_url}/login"

        response = self.session.post(url, json=request.model_dump())

        parsed_success = None
        parsed_error = None

        if validate:
            if response.status_code == 200:
                parsed_success = LoginResponse.model_validate(response.json())
            elif response.status_code == 400:
                parsed_error = ErrorResponse.model_validate(response.json())

        return response, parsed_success, parsed_error
