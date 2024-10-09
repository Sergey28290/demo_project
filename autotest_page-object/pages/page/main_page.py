from allure_commons.types import AttachmentType
import allure

from .base_page import BasePage
from .locators import SelectionLocators


class MainPage(BasePage):

    def testing_procedure(self):
        self.test_enter_email()
        self.test_enter_password()
        self.test_submit_button()
        self.test_profile_button()
        self.test_last_name_field()
        self.test_first_name_field()
        self.test_patronymic_field()
        self.test_postal_address_field()
        self.test_email_field()
        self.test_telephone_field()
        self.test_date_of_birth_field()
        self.test_category_field()

    def test_enter_email(self):
        with allure.step('Найти поле ввода "Почта"'):
            assert self.is_element_present(
                *SelectionLocators.ENTER_EMAIL
            ), "Поле ввода 'Почта' не найдено"
        with allure.step('Поле ввода "Почта" найдено'):
            pass
        with allure.step('Ввести в поле "Почта" корректное значение'):
            self.element_send_login()

    def test_enter_password(self):
        with allure.step('Найти поле ввода "Пароль"'):
            assert self.is_element_present(
                *SelectionLocators.ENTER_PASSWORD
            ), 'Поле ввода "Пароль" не найдено'
        with allure.step('Поле ввода "Пароль" не найдено'):
            pass
        with allure.step('Ввести в поле "Пароль" корректное значение'):
            self.element_send_password()

    def test_submit_button(self):
        with allure.step('Найти клавишу "Подтвердить"'):
            assert self.is_element_present(
                *SelectionLocators.SUBMIT_BUTTON
            ), 'Клавиша "Подтвердить" не найдена'
        with allure.step('Клавиша "Подтвердить" найдена'):
            pass
        with allure.step('Нажать на клавишу "Подтвердить"'):
            self.element_click()

    def test_profile_button(self):
        with allure.step('Переход на страницу "Расписание"'):
            pass
        with allure.step('Найти клавишу "Профиль"'):
            assert self.is_element_present(
                *SelectionLocators.PROFILE_BUTTON
            ), "Клавиша 'Профиль' не найдена"
        with allure.step('Клавиша "Профиль" найдена'):
            pass
        with allure.step('Нажать на клавишу "Профиль"'):
            self.element_click()

    def test_last_name_field(self):
        with allure.step('Найти поле ввода "Фамилия"'):
            assert self.is_element_present(
                *SelectionLocators.LAST_NAME_FIELD
            ), "Поле ввода 'Фамилия' не найдено"
        with allure.step('Поле ввода "Фамилия" найдено'):
            pass

    def test_first_name_field(self):
        with allure.step('Найти поле ввода "Имя"'):
            assert self.is_element_present(
                *SelectionLocators.FIRST_NAME_FIELD
            ), "Поле ввода 'Имя' не найдено"
        with allure.step("Поле ввода 'Имя' найдено"):
            pass

    def test_patronymic_field(self):
        with allure.step('Найти поле ввода "Отчество"'):
            assert self.is_element_present(
                *SelectionLocators.PATRONYMIC_FIELD
            ), "Поле ввода 'Отчество' не найдено"
        with allure.step("Поле ввода 'Отчество' найдено"):
            pass

    def test_postal_address_field(self):
        with allure.step('Найти поле ввода "Адрес"'):
            assert self.is_element_present(
                *SelectionLocators.POSTAL_ADDRESS
            ), 'Поле ввода "Адрес" не найдено'
        with allure.step('Поле ввода "Адрес" найдено'):
            pass

    def test_email_field(self):
        with allure.step('Найти поле ввода "Email"'):
            assert self.is_element_present(
                *SelectionLocators.EMAIL_FIELD
            ), 'Поле ввода "Email" не найдено'
        with allure.step('Поле ввода "Email" найдено'):
            pass

    def test_telephone_field(self):
        with allure.step('Найти поле ввода "Телефон"'):
            assert self.is_element_present(
                *SelectionLocators.TELEPHONE_FIELD
            ), 'Поле ввода "Телефон" не найдено'
        with allure.step('Поле ввода "Телефон" не найдено'):
            pass

    def test_date_of_birth_field(self):
        with allure.step('Найти поле выбора "Дата рождения"'):
            assert self.is_element_present(
                *SelectionLocators.DATE_OF_BIRTH
            ), 'Поле выбора "Дата рождения" не найдено'
        with allure.step('Поле выбора "Дата рождения" найдено'):
            pass

    def test_category_field(self):
        with allure.step('Найти поле выбора "Категория"'):
            assert self.is_element_present(
                *SelectionLocators.CATEGORY_FIELD
            ), 'Поле выбора "Категория" не найдено'
        with allure.step('Поле выбора "Категория" найдено'):
            pass

        with allure.step("Cоздание скриншота"):
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
