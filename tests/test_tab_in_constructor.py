from locators import Locators
locators = Locators()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestTabs:

    def test_navigate_through_tabs(self, browser):
        browser.get(locators.MAIN_URL)
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']")))
        browser.find_element(*locators.TAB_SAUCES).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']")))
        browser.find_element(*locators.TAB_FILLINGS).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']")))
        browser.find_element(*locators.TAB_BUNS).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']")))
