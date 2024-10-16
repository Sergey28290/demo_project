import allure
import pytest

from settings import login, password, test_cases, data, base_url


@allure.epic("Тесты UI")
@allure.suite('Негативный тест-сьют')
@allure.testcase('https://kiwi.demo.ru/case/278/')
@allure.feature('Авторизация')
@allure.story('Авторизоваться с некорректными учетными данными')
@allure.title('Проверка авторизации с некорректными учетными данными')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login, password, description", test_cases, ids=data)
def test_incorrect_authorization(login_page, login, password, description):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate(base_url)
    with allure.step('Ввести некорректные учетные данные'):
        with allure.step(description):
            login_page.incorrect_authorization(login, password)


@allure.epic('Тесты UI')
@allure.suite('Позитивный тест-сьют')
@allure.testcase('https://kiwi.demo.ru/case/277/')
@allure.feature('Авторизация')
@allure.story('Авторизоваться с валидными учетными данными')
@allure.title('Проверка авторизации с валидными учетными данными')
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_authorization(login_page):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate(base_url)
    with allure.step('Ввести валидные логин и пароль'):
        login_page.correct_authorization(login, password)
    with allure.step('Проверить открытие главной страницы'):
        login_page.check_successful_authorization()
