import requests


class ReqresClient:

    BASE_URL = "https://reqres.in/api"

    def __init__(self):
        self.headers = {
            "x-api-key": "reqres_1e1f36f344ad4d5ba45cd684382b46c2"
        }

    def create_user(self, data: dict):
        return requests.post(
            f"{self.BASE_URL}/users",
            json=data,
            headers=self.headers
        )

    def get_user(self, user_id: int):
        return requests.get(
            f"{self.BASE_URL}/users/{user_id}",
            headers=self.headers
        )

    def update_user(self, user_id: int, data: dict):
        return requests.patch(
            f"{self.BASE_URL}/users/{user_id}",
            json=data,
            headers=self.headers
        )

    def delete_user(self, user_id: int):
        return requests.delete(
            f"{self.BASE_URL}/users/{user_id}",
            headers=self.headers
        )
