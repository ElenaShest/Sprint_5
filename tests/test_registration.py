from locators import RegLocators, AuthLocators
reg_locators = RegLocators()
auth_locators = AuthLocators()

from data import Data
data = Data()

from urls import Urls
urls = Urls()

from helpers import open_reg_page

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegistration:

    def test_registration_success(self, browser):
        returned_url = open_reg_page(browser)
        assert returned_url == urls.REG_URL

        browser.find_element(*reg_locators.FIELD_NAME_REG).send_keys(data.USER_NAME)
        browser.find_element(*reg_locators.FIELD_EMAIL_REG).send_keys(data.RANDOM_EMAIL)
        browser.find_element(*reg_locators.FIELD_PASSWORD_REG).send_keys(data.PASSWORD)
        browser.find_element(*reg_locators.BUTTON_REGISTRATION).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(auth_locators.BUTTON_REG))
        assert browser.current_url == urls.AUTO_URL

    def test_registration_short_pass_error(self, browser):
        returned_url = open_reg_page(browser)
        assert returned_url == urls.REG_URL

        browser.find_element(*reg_locators.FIELD_NAME_REG).send_keys(data.USER_NAME)
        browser.find_element(*reg_locators.FIELD_EMAIL_REG).send_keys(data.RANDOM_EMAIL)
        browser.find_element(*reg_locators.FIELD_PASSWORD_REG).send_keys(data.SHORT_PASSWORD)
        browser.find_element(*reg_locators.BUTTON_REGISTRATION).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(reg_locators.ERROR_PASS))
        assert browser.current_url == urls.REG_URL
