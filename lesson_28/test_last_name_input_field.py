import pytest


@pytest.mark.parametrize("user_last_name", [
    'JansonJAnson',
    'JK',
    'HelloworldHelloworldHelloworl'
])
def test_last_name_with_valid_data(driver, registration_page_opened, valid_user_data, user_last_name):

    registration_page_opened.fill_form_with_valid_data(valid_user_data)

    registration_page_opened.input_value("last_name", user_last_name)

    registration_page_opened.click_button("register_button_form")

    registration_page_opened.check_garage_page()


@pytest.mark.parametrize("last_name, expected_error", [
    ("Scotish Straight", "Last name is invalid"),
    ("Gon78ka", "Last name is invalid"),
    ("Hand-'some'^-&", "Last name is invalid"),
    ("ВасильЧук", "Last name is invalid"),
    ("        ", "Last name is invalid"),
    ("o", "Last name has to be from 2 to 20 characters long"),
    ("HelloworldHelloworldHelloworld", "Last name has to be from 2 to 20 characters long"),
    ("", "Last name required"),
])
def test_last_name_with_invalid_data(driver, registration_page_opened, valid_user_data,
                                      last_name, expected_error):

    registration_page_opened.fill_form_with_valid_data(valid_user_data)

    registration_page_opened.input_value("last_name", last_name)

    registration_page_opened.check_register_button_disabled()
    registration_page_opened.check_error_msg(expected_error)

