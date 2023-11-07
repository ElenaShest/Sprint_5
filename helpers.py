from locators import AuthLocators, MainLocators, RegLocators
auth_locators = AuthLocators()
main_locators = MainLocators()
reg_locators = RegLocators()

from data import Data
data = Data()

from urls import Urls
urls = Urls()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def authorization(driver):
    email = data.EMAIL
    password = data.PASSWORD

    driver.find_element(*auth_locators.FIELD_EMAIL_AUTH).send_keys(email)
    driver.find_element(*auth_locators.FIELD_PASSWORD_AUTH).send_keys(password)
    driver.find_element(*auth_locators.BUTTON_IN).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(main_locators.BUTTON_ORDER))
    button_order = driver.find_element(*main_locators.BUTTON_ORDER)

    return button_order

def open_reg_page(driver):
    driver.get(urls.MAIN_URL)
    driver.find_element(*main_locators.BUTTON_LK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(auth_locators.BUTTON_REG))
    driver.find_element(*auth_locators.BUTTON_REG).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(reg_locators.BUTTON_REGISTRATION))
    button_registration = driver.find_element(*reg_locators.BUTTON_REGISTRATION)

    return button_registration
