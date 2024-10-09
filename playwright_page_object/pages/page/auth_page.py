from locators import AuthLocators


class AuthPage:
    def __init__(self, page):
        self.page = page
        self.email_input = self.page.locator(AuthLocators.EMAIL_INPUT)
        self.password_input = self.page.locator(AuthLocators.PASSWORD_INPUT)
        self.input_button = self.page.locator(AuthLocators.INPUT_BUTTON)

    def navigate(self, base_url: str):
        self.page.goto(f"{base_url}/login")

    def correct_authorization(self, login: str, password: str):
        self.email_input.fill(login)
        self.password_input.fill(password)
        self.input_button.click()

    def check_successful_authorization(self):
        content = self.page.content()
        assert "Пользователь" in content, "Authorization failed"

    def incorrect_authorization(self, login: str, password: str):
        self.email_input.fill(login)
        self.password_input.fill(password)
        self.input_button.click()

    def check_unsuccessful_authorization(self):
        content = self.page.content()
        assert "Пользователь" not in content, "Authorization should have failed"
