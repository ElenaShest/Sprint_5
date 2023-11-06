from locators import MainLocators, LkLocators, AuthLocators
main_locators = MainLocators()
lk_locators = LkLocators()
auth_locators = AuthLocators()

from urls import Urls
urls = Urls()

from data import Data
data = Data()

from helpers import authorization

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestExit:

    def test_exit_button_exit(self, browser):
        browser.get(urls.AUTO_URL)
        returned_url = authorization(browser)
        assert returned_url == urls.MAIN_URL

        browser.find_element(*main_locators.BUTTON_LK).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(lk_locators.BUTTON_EXIT))
        browser.find_element(*lk_locators.BUTTON_EXIT).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(auth_locators.BUTTON_IN))
        assert browser.current_url == urls.AUTO_URL

