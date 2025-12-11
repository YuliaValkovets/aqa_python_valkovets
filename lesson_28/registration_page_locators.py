from selenium.webdriver.common.by import By

class PageLocators:

    locators = {
        "sign_in_button": (By.XPATH, '//button[@class="btn btn-outline-white header_signin"]',
                           "Can't find or click 'Sign in' button on page"),
        "registration_button": (By.XPATH, '//div[@class="modal-footer d-flex justify-content-between"]/button['
                                          '@class="btn btn-link"]',
                                "Can't find or click 'Registration' button on page"),
        "register_button_form": (By.XPATH, '//button[@class="btn btn-primary"]',
                                 "Can't find or click 'Register' button on page" ),
        "name": (By.ID, 'signupName', "Can't find 'Name' input field in Registration form"),
        "last_name": (By.ID, 'signupLastName', "Can't find 'Last name' input field in Registration form"),
        "email": (By.ID, 'signupEmail', "Can't find 'Email' input field in Registration form"),
        "password": (By.ID, 'signupPassword', "Can't find 'Password' input field in Registration form"),
        "re_password": (By.ID, 'signupRepeatPassword',
                        "Can't find 'Re-enter password' input field in Registration form"),
        "message_garage_page": (By.XPATH, '//p[@class="h3 panel-empty_message"]',
                                "Can't find the message on Garage page"),
        "error_invalid_data": (By.XPATH, '//div[@class="invalid-feedback"]/p',
                               "Can't find the error message")
    }

