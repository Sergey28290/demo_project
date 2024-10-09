from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import allure

from configuration import login, password, timeout


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.element = None

    def open(self):
        with allure.step("Открыть страницу"):
            self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.element = self.browser.find_element(how, what)
        except (NoSuchElementException, NoAlertPresentException):
            return False
        return self.element

    def element_click(self):
        self.element.click()

    def element_send_login(self):
        self.element.send_keys(login)

    def element_send_password(self):
        self.element.send_keys(password)
