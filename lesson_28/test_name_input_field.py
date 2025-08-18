import pytest


@pytest.mark.parametrize("user_name", [
    'Yuliia',
    'aa',
    'fgaJkhYgfrjUkgdhjnmU'
])
def test_name_with_valid_data(driver, registration_page_opened, valid_user_data, user_name):

    registration_page_opened.fill_form_with_valid_data(valid_user_data)

    registration_page_opened.input_value("name", user_name)

    registration_page_opened.click_button("register_button_form")

    registration_page_opened.check_garage_page()


@pytest.mark.parametrize("user_name, expected_error", [
    ("Yu li", "Name is invalid"),
    ("Yu349", "Name is invalid"),
    ("*(&*&^&^*", "Name is invalid"),
    ("мавампвпв", "Name is invalid"),
    ("        ", "Name is invalid"),
    ("h", "Name has to be from 2 to 20 characters long"),
    ("dHdksjdksjdksjdksjdJl", "Name has to be from 2 to 20 characters long"),
    ("", "Name required"),
])
def test_name_with_invalid_data(driver, registration_page_opened, valid_user_data,
                                      user_name, expected_error):

    registration_page_opened.fill_form_with_valid_data(valid_user_data)

    registration_page_opened.input_value("name", user_name)

    registration_page_opened.check_register_button_disabled()
    registration_page_opened.check_error_msg(expected_error)

