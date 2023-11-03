from locators import Locators
locators = Locators()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestExit:

    def test_exit_button_exit(self, authorization_before):
        authorization_before.find_element(*locators.BUTTON_LK).click()
        WebDriverWait(authorization_before, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_EXIT))
        authorization_before.find_element(*locators.BUTTON_EXIT).click()
        WebDriverWait(authorization_before, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_IN))

