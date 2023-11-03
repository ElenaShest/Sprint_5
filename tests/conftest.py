import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators
locators = Locators()

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def authorization_after():
    driver = webdriver.Chrome()
    yield driver

    email = 'elenashest2356@yandex.ru'
    password = 'Q1w2e3'
    driver.find_element(*locators.FIELD_EMAIL_AUTO).send_keys(email)
    driver.find_element(*locators.FIELD_PASSWORD_AUTO).send_keys(password)
    driver.find_element(*locators.BUTTON_IN).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_ORDER))

    driver.quit()


@pytest.fixture
def authorization_before():
    driver = webdriver.Chrome()

    driver.get(locators.AUTO_URL)
    email = 'elenashest2356@yandex.ru'
    password = 'Q1w2e3'
    driver.find_element(*locators.FIELD_EMAIL_AUTO).send_keys(email)
    driver.find_element(*locators.FIELD_PASSWORD_AUTO).send_keys(password)
    driver.find_element(*locators.BUTTON_IN).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_ORDER))

    yield driver
    driver.quit()
