from selenium import webdriver
import pytest
from lesson_28.registration_page import RegistrationPage
from faker import Faker

fake = Faker()

@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver=driver)

@pytest.fixture
def registration_page_opened(driver):
    page = RegistrationPage(driver)
    page.open_registration_form()
    return page

@pytest.fixture
def valid_user_data():
    password = fake.password()
    return {
        "name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "password": password,
        "re_password": password,
    }
