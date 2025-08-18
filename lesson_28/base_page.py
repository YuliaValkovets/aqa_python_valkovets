from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self._driver = driver
        self.url = url

    def open_page(self):
        self._driver.get(self.url)

    def _input(self, locator, timeout=10, message=None):
        el = WebDriverWait(self._driver, timeout). until(
            EC.visibility_of_element_located(locator), message=message)

        return el

    def _button_is_clickable(self, locator, timeout=10, message=None):
        el = WebDriverWait(self._driver, timeout). until(
            EC.element_to_be_clickable(locator), message=message)

        return el