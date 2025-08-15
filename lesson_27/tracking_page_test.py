
def test_wrong_tracking_number(driver, tracking_number, tracking_page):

    tracking_page.open_page()
    tracking_page.input_tr_number(tracking_number).click_search_button()
    tracking_page.check_error_message()






