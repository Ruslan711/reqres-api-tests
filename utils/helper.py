import allure
import json


def attach_response(response):
    """Прикрепляет ответ API к отчёту Allure."""

    try:
        if response.text:
            data = response.json()
        else:
            data = {"status_code": response.status_code}
    except Exception:
        data = response.text

    if isinstance(data, (dict, list)):
        body = json.dumps(data, indent=4, ensure_ascii=False)
        attachment_type = allure.attachment_type.JSON
    else:
        body = str(data)
        attachment_type = allure.attachment_type.TEXT

    allure.attach(
        body=body,
        name="API Response",
        attachment_type=attachment_type,
    )