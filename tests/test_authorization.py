from locators import MainLocators, AuthLocators, RegLocators
main_locators = MainLocators()
auth_locators = AuthLocators()
reg_locators = RegLocators()

from urls import Urls
urls = Urls()

from data import Data
data = Data()

from helpers import authorization

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestAuthorization:

    def test_authorization_button_login_in_acc(self, browser):
        browser.get(urls.MAIN_URL)
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(main_locators.BUTTON_LOGIN_IN_ACC))
        browser.find_element(*main_locators.BUTTON_LOGIN_IN_ACC).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(auth_locators.BUTTON_IN))
        button_in = browser.find_element(*auth_locators.BUTTON_IN)
        assert button_in is not None
        button_order = authorization(browser)

        assert button_order is not None

    def test_authorization_button_lk(self, browser):
        browser.get(urls.MAIN_URL)
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(main_locators.BUTTON_LK))
        browser.find_element(*main_locators.BUTTON_LK).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(auth_locators.BUTTON_IN))
        button_in = browser.find_element(*auth_locators.BUTTON_IN)
        assert button_in is not None
        button_order = authorization(browser)

        assert button_order is not None

    def test_authorization_form_registration(self, browser):
        browser.get(urls.REG_URL)
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(reg_locators.BUTTON_LOGIN))
        browser.find_element(*reg_locators.BUTTON_LOGIN).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(auth_locators.BUTTON_IN))
        button_in = browser.find_element(*auth_locators.BUTTON_IN)
        assert button_in is not None
        button_order = authorization(browser)

        assert button_order is not None

    def test_authorization_form_forgot_pass(self, browser):
        browser.get(urls.FORGOT_PASS_URL)
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(reg_locators.BUTTON_LOGIN))
        browser.find_element(*reg_locators.BUTTON_LOGIN).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(auth_locators.BUTTON_IN))
        button_in = browser.find_element(*auth_locators.BUTTON_IN)
        assert button_in is not None
        button_order = authorization(browser)

        assert button_order is not None
