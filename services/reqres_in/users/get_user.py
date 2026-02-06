from services.base_api import BaseAPI


class GetUser(BaseAPI):

    def __init__(self, env_config):
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)
        # Вызови конструктор родителя, передав URL и API ключ
        # Подсказка: посмотри как это сделано в post_create.py
        pass

    def get_user(self, user_id: int):
        url = f"{self.base_url}/users/{user_id}"
        return self.session.get(url)
        # """Получение пользователя по ID.
        #
        # Args:
        #     user_id (int): ID пользователя
        #
        # Returns:
        #     requests.Response: Ответ от сервера
        # """
        # Отправь GET-запрос на /users/{user_id}
        # Подсказка: self.session.get(url)
        pass





# from services.base_api import BaseAPI
#
#
# class GetUser(BaseAPI):
#
#     def __init__(self, env_config):
#         super().__init__(base_url=env_config.reqres_url,api_key=env_config.reqres_api_key)
#
#     def get_user(self, user_id: int):
#         """Получение пользователя по ID.
#
#         Args:
#             user_id (int): ID пользователя
#
#         Returns:
#             requests.Response: Ответ от сервера
#         """
#         url = f"{self.base_url}/users/{user_id}"
#         return self.session.get(url)
