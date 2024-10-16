base_url = "https://ir-test-dev.demo.ru"
login = "login"
password = "password"

test_cases = [
    ("invalidemail", "12345", "Ввести некорректный формат email"),
    ("sergioche@", "12345", "Ввести некорректный формат email"),
    ("sergioche@riginter", "12345", "Ввести некорректный формат email"),
    ("sergioche@riginter.pro", "p", "Ввести минимальную длину пароля"),
    ("sergioche@riginter.pro", "p" * 257, "Ввести максимальную длину пароля"),
    ("sergioche@riginter.pro", "password", "Ввести слабый пароль"),
    ("", "", "Ввести пустые email и пароль")
]

data = [
    'Invalid email formats',
    'Invalid email formats',
    'Invalid email formats',
    'Minimum length password',
    'Maximum length password',
    'Weak password',
    'Empty email and password'
]