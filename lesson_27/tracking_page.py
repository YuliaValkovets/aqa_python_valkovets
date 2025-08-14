from lesson_27.base_page import BasePage
from lesson_27.tracking_page_locators import TrackingPageLocators


class TrackingPage(BasePage):

    def __init__(self, driver, url = 'https://tracking.novaposhta.ua/#/uk'):
        super().__init__(driver, url)


    def input_tr_number(self, tr_number):
        tracking_number_input = self._input(locator=TrackingPageLocators.input_field_loc,
                                            message="Can't find input field for entering tracking number")
        tracking_number_input.send_keys(tr_number)
        return self


    def click_search_button(self):
        self._button_is_clickable(locator=TrackingPageLocators.search_button_loc, timeout=2,
                                  message="Can't find or click search button on Tracking page").click()
        return self


    def check_error_message(self):
        error_el = self._input(locator=TrackingPageLocators.error_message_loc, timeout=5,
                               message="Can't find error message on Tracking page")
        actual_text = error_el.text.strip()
        expected_text = (
            "Ми не знайшли посилку за таким номером. Якщо ви шукаєте інформацію "
            "про посилку, якій більше 3 місяців, будь ласка, зверніться у контакт-центр: 0 800 500 609"
        )
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
