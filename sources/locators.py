from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    LOG_IN_TO_ACCOUNT = By.XPATH, "//button[text()='Войти в аккаунт']"  # Кнопка Войти в аккаунт
    REGISTER = By.XPATH, "//a[@href='/register']"  # Ссылка Зарегистрироваться
    NAME_FIELD = By.XPATH, "//label[text()='Имя']/following-sibling::input"  # Поле Имя
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/following-sibling::input"  # Поле Email
    PASSWORD_FIELD = By.XPATH, "//input[@name='Пароль']"  # Поле Пароль
    BUTTON_REGISTER = By.XPATH, "//button[contains(@class, 'button_button_type_primary')]"  # Кнопка Зарегистрироваться
    BUTTON_LOGIN = By.XPATH, "//button[text()='Войти']"  # Кнопка Войти
    ERROR_INCORRECT_PASSWORD = By.XPATH, "//div[contains(@class, 'input_status_error')]"  # Ошибка некорректного пароля
    BUTTON_ORDER = By.XPATH, "//button[text()='Оформить заказ']"  # Кнопка оформления заказа
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, "//a[@href='/account']"  # Кнопка Личный Кабинет
    LINK_LOGIN = By.XPATH, "//a[@href='/login']"  # Ссылка Войти
    LINK_PASSWORD_RECOVERY = By.XPATH, "//a[@href='/forgot-password']"  # Ссылка Восстановить пароль
    BUTTON_SAVE = By.XPATH, "//button[text()='Сохранить']"  # Кнопка Сохранить
    BUTTON_CONSTRUCTOR = By.XPATH, "//a[contains(@class, 'AppHeader_header') and @href='/']"  # Кнопка Конструктор
    LOGO = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a"  # Логотип Stellar Burgers
    BUTTON_LOGOUT = By.XPATH, "//button[text()='Выход']"  # Кнопка Выход
    SECTION_ROLLS = By.XPATH, "//span[text()='Булки']/parent::div"  # Раздел Булки
    SECTION_SAUCES = By.XPATH, "//span[text()='Соусы']/parent::div"  # Раздел Соусы
    SECTION_FILLINGS = By.XPATH, "//span[text()='Начинки']/parent::div"  # Раздел Начинки
    ROLL = By.XPATH, "//img[@alt='Краторная булка N-200i']"  # Булка
    SAUCE = By.XPATH, "//img[@alt='Соус фирменный Space Sauce']"  # Соус
    FILLING = By.XPATH, "//img[@alt='Говяжий метеорит (отбивная)']"  # Начинка
