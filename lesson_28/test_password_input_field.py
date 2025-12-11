import pytest


@pytest.mark.parametrize("password", [
    'TestTes1',
    'Example345Test',
    'HeLlOWorl2789He',
    'Yulia@test23'
])
def test_password_with_valid_data(driver, registration_page_opened, valid_user_data, password):

    registration_page_opened.fill_form_with_valid_data(valid_user_data)

    registration_page_opened.input_value("password", password)
    registration_page_opened.input_value("re_password", password)

    registration_page_opened.click_button("register_button_form")

    registration_page_opened.check_garage_page()


@pytest.mark.parametrize("password, expected_error", [
    ("HappYD8", "Password has to be from 8 to 15 characters long and contain "
                "at least one integer, one capital, and one small letter"),
    ("PasswordPa45ssWo", "Password has to be from 8 to 15 characters long and contain "
                "at least one integer, one capital, and one small letter"),
    ("pythonnn098", "Password has to be from 8 to 15 characters long and contain "
                "at least one integer, one capital, and one small letter"),
    ("HELLOWORLD123", "Password has to be from 8 to 15 characters long and contain "
                "at least one integer, one capital, and one small letter"),
    ("", "Password required"),
])
def test_password_with_invalid_data(driver, registration_page_opened, valid_user_data,
                                      password, expected_error):

    registration_page_opened.fill_form_with_valid_data(valid_user_data)

    registration_page_opened.input_value("password", password)
    registration_page_opened.input_value("re_password", password)

    registration_page_opened.check_register_button_disabled()
    registration_page_opened.check_error_msg(expected_error)