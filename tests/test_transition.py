from locators import MainLocators, LkLocators
main_locators = MainLocators()
lk_locators = LkLocators()

from urls import Urls
urls = Urls()

from data import Data
data = Data()

from helpers import authorization

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestTransition:

    def test_transition_from_main_to_lk(self, browser):
        browser.get(urls.AUTO_URL)
        returned_url = authorization(browser)
        assert returned_url == urls.MAIN_URL

        browser.find_element(*main_locators.BUTTON_LK).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(lk_locators.BUTTON_EXIT))
        assert browser.current_url == urls.LK_URL

    def test_transition_from_lk_to_constructor(self, browser):
        browser.get(urls.AUTO_URL)
        returned_url = authorization(browser)
        assert returned_url == urls.MAIN_URL

        browser.find_element(*main_locators.BUTTON_LK).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(lk_locators.BUTTON_EXIT))
        browser.find_element(*lk_locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(main_locators.BUTTON_ORDER))
        assert browser.current_url == urls.MAIN_URL

    def test_transition_from_lk_to_logo(self, browser):
        browser.get(urls.AUTO_URL)
        returned_url = authorization(browser)
        assert returned_url == urls.MAIN_URL

        browser.find_element(*main_locators.BUTTON_LK).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(lk_locators.BUTTON_EXIT))
        browser.find_element(*lk_locators.LOGO).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(main_locators.BUTTON_ORDER))
        assert browser.current_url == urls.MAIN_URL
