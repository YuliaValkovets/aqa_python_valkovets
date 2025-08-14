from selenium import webdriver
import pytest
from lesson_27.tracking_page import TrackingPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def tracking_number():
    tr_number = 2324242343535
    yield tr_number

@pytest.fixture
def tracking_page(driver):
    return TrackingPage(driver=driver)