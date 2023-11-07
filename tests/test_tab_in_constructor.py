from locators import MainLocators
main_locators = MainLocators()

from urls import Urls
urls = Urls()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestTabs:

    def test_navigate_through_tabs_buns_sauces(self, browser):
        browser.get(urls.MAIN_URL)
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(main_locators.BUTTON_LK))
        active_tab_text = browser.find_element(*main_locators.ACTIVE_TAB).text
        assert active_tab_text == 'Булки'
        browser.find_element(*main_locators.TAB_SAUCES).click()
        new_active_tab_text = browser.find_element(*main_locators.ACTIVE_TAB).text
        assert new_active_tab_text == 'Соусы'

    def test_navigate_through_tabs_buns_fillings(self, browser):
        browser.get(urls.MAIN_URL)
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(main_locators.BUTTON_LK))
        browser.find_element(*main_locators.TAB_FILLINGS).click()
        new_active_tab_text = browser.find_element(*main_locators.ACTIVE_TAB).text
        assert new_active_tab_text == 'Начинки'

    def test_navigate_through_tabs_sauces_fillings(self, browser):
        TestTabs.test_navigate_through_tabs_buns_sauces(browser, browser)
        browser.find_element(*main_locators.TAB_FILLINGS).click()
        last_active_tab_text = browser.find_element(*main_locators.ACTIVE_TAB).text
        assert last_active_tab_text == 'Начинки'

    def test_navigate_through_tabs_sauces_buns(self, browser):
        TestTabs.test_navigate_through_tabs_buns_sauces(browser, browser)
        browser.find_element(*main_locators.TAB_BUNS).click()
        last_active_tab_text = browser.find_element(*main_locators.ACTIVE_TAB).text
        assert last_active_tab_text == 'Булки'


