from locators import Locators
locators = Locators()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from random import randint

class TestRegistration:

    def test_registration_success(self, browser):
        browser.get(locators.MAIN_URL)
        browser.find_element(*locators.BUTTON_LK).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_REG))
        browser.find_element(*locators.BUTTON_REG).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_REGISTRATION))

        user_name = 'Elena'
        email = f'elenashest2{randint(100, 999)}@yandex.ru'
        password = 'Q1w2e3'
        browser.find_element(*locators.FIELD_NAME_REG).send_keys(user_name)
        browser.find_element(*locators.FIELD_EMAIL_REG).send_keys(email)
        browser.find_element(*locators.FIELD_PASSWORD_REG).send_keys(password)
        browser.find_element(*locators.BUTTON_REGISTRATION).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_REG))

    def test_registration_short_pass_error(self, browser):
        browser.get(locators.REG_URL)
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_REGISTRATION))

        user_name = 'Elena'
        email = f'elenashest2{randint(100, 999)}@yandex.ru'
        password = 'Q1w2e'
        browser.find_element(*locators.FIELD_NAME_REG).send_keys(user_name)
        browser.find_element(*locators.FIELD_EMAIL_REG).send_keys(email)
        browser.find_element(*locators.FIELD_PASSWORD_REG).send_keys(password)
        browser.find_element(*locators.BUTTON_REGISTRATION).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.ERROR_PASS))
