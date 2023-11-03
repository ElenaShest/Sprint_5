from selenium import webdriver
from selenium.webdriver.common.by import By
webdriver.Chrome()

class Locators:
    MAIN_URL = "https://stellarburgers.nomoreparties.site/" # адрес главной
    REG_URL = "https://stellarburgers.nomoreparties.site/register" # адрес регистрации
    AUTO_URL = "https://stellarburgers.nomoreparties.site/login" # адрес авторизации
    FORGOT_PASS_URL = "https://stellarburgers.nomoreparties.site/forgot-password" # адрес восстановления пароля
    BUTTON_LK = (By.XPATH, ".//nav[@class='AppHeader_header__nav__g5hnF']/a[@class='AppHeader_header__link__3D_hX']") # кнопка "Личный кабинет" на главной
    BUTTON_LOGIN_IN_ACC = (By.XPATH, ".//button[text()='Войти в аккаунт']") # кнопка "Войти в аккаунт" на главной
    BUTTON_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']") # кнопка "Оформить заказ" на главной
    BUTTON_REG = (By.XPATH, ".//a[@href='/register']") # кнопка "Зарегистрироваться" на странице авторизации
    BUTTON_RESTORE_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']") # кнопка "Восстановить пароль" на странице авторизации
    FIELD_EMAIL_AUTO = (By.XPATH, ".//input[@name='name']") # поле ввода "Email" при авторизации
    FIELD_PASSWORD_AUTO = (By.XPATH, ".//input[@name='Пароль']") # поле ввода "Пароль" при авторизации
    BUTTON_IN = (By.XPATH, ".//button[text()='Войти']") # кнопка "Войти" при авторизации
    FIELD_NAME_REG = (By.XPATH, "(.//input[@name='name'])[1]") # кнопка "Имя" при регистрации
    FIELD_EMAIL_REG = (By.XPATH, "(.//input[@name='name'])[2]") # поле ввода "Email" при регистрации
    FIELD_PASSWORD_REG = (By.XPATH, ".//input[@name='Пароль']") # поле ввода "Пароль" при регистрации
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']") # кнопка "Зарегистрироваться" при регистрации
    ERROR_PASS = (By.XPATH, ".//p[text()='Некорректный пароль']") # ошибка валидации под полем "Пароль"
    BUTTON_LOGIN = (By.XPATH, ".//a[@href='/login']") # кнопка "Войти" на странице регистрации/восстановления пароля
    BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']") # кнопка "Выход" в личном кабинете
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']") # кнопка "Конструктор" в шапке
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # логотип stellar burgers
    TAB_BUNS = (By.XPATH, ".//span[text()='Булки']") # вкладка "Булки" на главной
    TAB_SAUCES = (By.XPATH, ".//span[text()='Соусы']") # вкладка "Соусы" на главной
    TAB_FILLINGS = (By.XPATH, ".//span[text()='Начинки']") # вкладка "Начинки" на главной
