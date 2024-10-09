from selenium.webdriver.common.by import By


class SelectionLocators:
    ENTER_EMAIL = (By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[1]/div/input")
    ENTER_PASSWORD = (By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[2]/div/input")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[2]/button[1]")
    PROFILE_BUTTON = (By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[1]/div[2]/a/img")
    LAST_NAME_FIELD = (By.XPATH, "//*[text()[contains(., 'Фамилия')]]")
    FIRST_NAME_FIELD = (By.XPATH, "//*[text()[contains(., 'Имя')]]")
    PATRONYMIC_FIELD = (By.XPATH, "//*[text()[contains(., 'Отчество')]]")
    POSTAL_ADDRESS = (By.XPATH, "//*[text()[contains(., 'адрес')]]")
    EMAIL_FIELD = (By.XPATH, "//*[text()[contains(., 'Email')]]")
    TELEPHONE_FIELD = (By.XPATH, "//*[text()[contains(., 'Телефон')]]")
    DATE_OF_BIRTH = (By.XPATH, "//*[text()[contains(., 'Дата рождения')]]")
    CATEGORY_FIELD = (By.XPATH, "//*[text()[contains(., 'Категория')]]")
