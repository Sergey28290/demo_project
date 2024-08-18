import allure
import pytest

from settings import *


@allure.epic('Тесты API')
@allure.suite('Позитивный тест-сьют')
@allure.testcase('TC-304')
@allure.feature('Авторизация')
@allure.story('Авторизация с валидными учетными данными')
@allure.title('Проверка авторизации с валидными учетными данными')
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_authorization(login_page):
    with allure.step('Ввести валидные логин и пароль'):
        login_page.authorization(base_url, login, password)
    with allure.step('Проверить статус код'):
        login_page.check_response_status_code_200()
    with allure.step('Проверить заголовки'):
        login_page.check_response_headers()
    with allure.step('Проверить время отклика'):
        login_page.check_response_time()
    with allure.step('Проверить тело ответа'):
        login_page.jsonschema_validate(schema_1)


@allure.epic("Тесты API")
@allure.suite('Негативный тест-сьют')
@allure.testcase('TC-305')
@allure.feature('Авторизация')
@allure.story('Авторизация с некорректными учетными данными')
@allure.title('Проверка авторизации с некорректными учетными данными')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login, password, description", test_cases, ids=data)
def test_incorrect_authorization(login_page, login, password, description):
    with allure.step(description):
        login_page.authorization(base_url, login, password)
    with allure.step('Проверить статус код'):
        login_page.check_response_status_code_400()
    with allure.step('Проверить заголовки'):
        login_page.check_response_headers()
    with allure.step('Проверить тело ответа'):
        login_page.jsonschema_validate(message)
