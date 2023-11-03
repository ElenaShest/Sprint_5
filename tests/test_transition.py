from locators import Locators
locators = Locators()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestTransition():

    def test_transition_from_main_to_lk(self, authorization_before):
        authorization_before.find_element(*locators.BUTTON_LK).click()
        WebDriverWait(authorization_before, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_EXIT))

    def test_transition_from_lk_to_constructor(self, authorization_before):
        authorization_before.find_element(*locators.BUTTON_LK).click()
        WebDriverWait(authorization_before, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_EXIT))
        authorization_before.find_element(*locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(authorization_before, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_ORDER))

    def test_transition_from_lk_to_logo(self, authorization_before):
        authorization_before.find_element(*locators.BUTTON_LK).click()
        WebDriverWait(authorization_before, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_EXIT))
        authorization_before.find_element(*locators.LOGO).click()
        WebDriverWait(authorization_before, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_ORDER))

