# Sprint_5
# Проект автоматизации тестирования сайта заказа космических бургеров

1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install pytest, pip install selenium, установить драйвера для хрома
3. Команда для запуска — pytest -v .\tests

Тесты:
1. test_registration.py - файл с тестами регистрации
   2. test_registration_success - успешная регистрация
   3. test_registration_short_pass_error - регистрация с коротким паролем
4. test_authorization.py - файл с тестами авторизации
   5. test_authorization_button_login_in_acc - вход через кнопку "Войти в аккаунт" на главной
   6. test_authorization_button_lk - вход через кнопку "Личный кабинет" на главной
   7. test_authorization_form_registration - вход через форму регистрации
   8. test_authorization_form_forgot_pass - вход через форму восстановления пароля
9. test_transition.py - файл с тестами перехода между страницами
   10. test_transition_from_main_to_lk - переход с главной в личный кабинет
   11. test_transition_from_lk_to_constructor - переход из личного кабинета на главную через кнопку "Конструктор"
   12. test_transition_from_lk_to_logo - переход из личного кабинета на главную через логотип
13. test_exit.py - файл с тестами выхода
    14. test_exit_button_exit - выход по кнопке "Выход" в личном кабинете
15. test_tab_in_constructor.py - файл с тестами переключения вкладок на главной
    16. test_navigate_through_tabs_buns_sauces - переключение вкладок с Булок на Соусы
    17. test_navigate_through_tabs_buns_fillings - переключение вкладок с Булок на Начинки
    18. test_navigate_through_tabs_sauces_fillings - переключение вкладок с Соусов на Начинки
    19. test_navigate_through_tabs_sauces_buns - переключение вкладок с Соусов на Булки


