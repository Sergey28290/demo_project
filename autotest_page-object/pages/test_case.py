import allure
import pytest

from .page.main_page import MainPage


@allure.feature('Тестирование соответствия UI личного кабинета к ТЗ')
@allure.story('Открыта страница "Bumbleby"')
def test_interface_of_the_personal_account_page(browser):
    link = "https://bumbleby.ru"
    test = MainPage(browser, link)
    test.open()
    test.testing_procedure()
