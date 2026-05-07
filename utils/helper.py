import allure
import json


class Helper:
    def attach_response(self, response):
        """Прикрепляет ответ API к отчёту Allure."""

        try:
            if response.text:
                data = response.json()
            else:
                data = {"status_code": response.status_code}
        except Exception:
            data = response.text

        allure.attach(
            body=json.dumps(data, indent=4, ensure_ascii=False)
            if isinstance(data, (dict, list))
            else str(data),
            name="API Response",
            attachment_type=allure.attachment_type.JSON
        )