import pytest
from selenium import webdriver

from urls import Urls
urls = Urls()

from data import Data
data = Data()

@pytest.fixture
def browser():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()


