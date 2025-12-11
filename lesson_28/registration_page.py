from lesson_28.base_page import BasePage
from lesson_28.registration_page_locators import PageLocators


class RegistrationPage(BasePage):

    def __init__(self, driver, url='https://guest:welcome2qauto@qauto2.forstudy.space'):
        super().__init__(driver, url)

    def input_value(self, field_name, value):

        by, locator, message = PageLocators.locators[field_name]

        input_field = self._input(locator=(by, locator), timeout=10, message=message)
        input_field.clear()
        input_field.send_keys(value)

        return self

    def click_button(self, field_name):

        by, locator, message = PageLocators.locators[field_name]
        self._button_is_clickable(locator=(by, locator), timeout=3,
                                  message=message).click()
        return self


    def open_registration_form(self):

        self.open_page()
        self.click_button('sign_in_button')
        self.click_button('registration_button')

        return self

    def check_garage_page(self):

        by, locator, message = PageLocators.locators["message_garage_page"]
        message_el = self._input(locator=(by, locator), timeout=3,
                               message=message)

        actual_text = message_el.text.strip()
        expected_text = "You don’t have any cars in your garage"

        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"

    def check_error_msg(self, error_msg):

        by, locator, message = PageLocators.locators["error_invalid_data"]
        error_el = self._input(locator=(by, locator), timeout=10,
                               message=message)

        actual_text = error_el.text.strip()
        expected_text = error_msg

        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"

    def check_register_button_disabled(self):
        by, locator, message = PageLocators.locators["register_button_form"]
        button = self._input(locator=(by, locator), timeout=10, message=message)

        assert not button.is_enabled(), "Register button should be disabled for invalid data"

    def fill_form_with_valid_data(self, user):
        self.input_value("name", user["name"])
        self.input_value("last_name", user["last_name"])
        self.input_value("email", user["email"])
        self.input_value("password", user["password"])
        self.input_value("re_password", user["re_password"])
