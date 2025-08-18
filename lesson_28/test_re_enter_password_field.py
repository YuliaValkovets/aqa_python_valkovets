import pytest


def test_re_password_match_password(driver, registration_page_opened, valid_user_data):

    registration_page_opened.fill_form_with_valid_data(valid_user_data)

    registration_page_opened.input_value("password", "Python2025")
    registration_page_opened.input_value("re_password", "Python2025")

    registration_page_opened.click_button("register_button_form")

    registration_page_opened.check_garage_page()


@pytest.mark.parametrize("re_password, expected_error", [
    ("Password90", "Passwords do not match"),
    ("", "Re-enter password required")
])
def test_re_password_with_invalid_data(driver, registration_page_opened, valid_user_data,
                                      re_password, expected_error):

    registration_page_opened.fill_form_with_valid_data(valid_user_data)

    registration_page_opened.input_value("re_password", re_password)
    registration_page_opened.input_value("name", "Testexample")

    registration_page_opened.check_register_button_disabled()
    registration_page_opened.check_error_msg(expected_error)