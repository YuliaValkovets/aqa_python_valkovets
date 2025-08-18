import pytest


@pytest.mark.parametrize("user_email", [
    'ukraine@slava.com',
    'd@a.co',
    'sun+sea@co.ol',
    'he_llo@world.test.ua',
    'FUNNY@TEST.COM'
])
def test_email_with_valid_data(driver, registration_page_opened, valid_user_data, user_email):

    registration_page_opened.fill_form_with_valid_data(valid_user_data)

    registration_page_opened.input_value("email", user_email)

    registration_page_opened.click_button("register_button_form")

    registration_page_opened.check_garage_page()


@pytest.mark.parametrize("user_email, expected_error", [
    ("Funnyday", "Email is incorrect"),
    ("yuliia@", "Email is incorrect"),
    ("@test.ua", "Email is incorrect"),
    ("test@example", "Email is incorrect"),
    ("yulia test@ukr.com", "Email is incorrect"),
    ("example@test..com", "Email is incorrect"),
    ("", "Email required")
])
def test_email_with_invalid_data(driver, registration_page_opened, valid_user_data,
                                      user_email, expected_error):

    registration_page_opened.fill_form_with_valid_data(valid_user_data)

    registration_page_opened.input_value("email", user_email)

    registration_page_opened.check_register_button_disabled()
    registration_page_opened.check_error_msg(expected_error)