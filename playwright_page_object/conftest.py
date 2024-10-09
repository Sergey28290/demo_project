import pytest

from page_object.pages.auth import AuthPage


@pytest.fixture
def login_page(page):
    return AuthPage(page)
