from locators import Locators
locators = Locators()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestAuthorization():

    def test_authorization_button_login_in_acc(self, authorization_after):
        authorization_after.get(locators.MAIN_URL)
        WebDriverWait(authorization_after, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_LOGIN_IN_ACC))
        authorization_after.find_element(*locators.BUTTON_LOGIN_IN_ACC).click()
        WebDriverWait(authorization_after, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_IN))

    def test_authorization_button_lk(self, authorization_after):
        authorization_after.get(locators.MAIN_URL)
        WebDriverWait(authorization_after, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_LK))
        authorization_after.find_element(*locators.BUTTON_LK).click()

    def test_authorization_form_registration(self, authorization_after):
        authorization_after.get(locators.REG_URL)
        WebDriverWait(authorization_after, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_LOGIN))
        authorization_after.find_element(*locators.BUTTON_LOGIN).click()

    def test_authorization_form_forgot_pass(self, authorization_after):
        authorization_after.get(locators.FORGOT_PASS_URL)
        WebDriverWait(authorization_after, 3).until(expected_conditions.visibility_of_element_located(locators.BUTTON_LOGIN))
        authorization_after.find_element(*locators.BUTTON_LOGIN).click()
