import os.path
from unittest.mock import patch
import pytest
from homework_10 import log_event

log_file = "login_system.log"

@pytest.fixture
def clear_log_file(): # clean log_file before every test
    with open(log_file, "w"):
        pass



@pytest.mark.parametrize("username, status", [
    ("Yuliia", "success"),
    ("Ivan", "expired"),
    ("James", "failed"),
])

def test_login_system_with_valid_status(clear_log_file, username, status):

    log_event(username,status)
    assert os.path.exists(log_file) # check that log_file was created or already exists after calling log_event

    with open(log_file, "r") as file_with_logs:
        actual_result = file_with_logs.read() # read the content of the log_file
        expected_result = f"Login event - Username: {username}, Status: {str(status)}"
        assert expected_result in actual_result



@pytest.mark.parametrize("username, status", [
    ("Kate", "ailed"),
    ("Roman", ""),
    ("Liam", False),
    ("Max", None),
    ("Rex", 890),
    ("Tom", ["expired"])
])

def test_login_system_with_invalid_status(clear_log_file, username, status):

    log_event(username,status)
    assert os.path.exists(log_file) # check that log_file was created or already exists after calling log_event

    with open(log_file, "r") as file_with_logs:
        actual_result = file_with_logs.read() # read the content of the log_file
        expected_result = f"Login event - Username: {username}, Status: {str(status)}"
        assert expected_result in actual_result



@pytest.mark.parametrize("username, status, expected_log_level", [
    ("Max", "success", "info"),
    ("Richard", "expired", "warning"),
    ("Anna", "failed", "error"),
    ("Yuliia", "none", "error"),
])

def test_log_level(username, status, expected_log_level):
    # create mocks for logging methods info, warning, and error
    with patch("logging.Logger.info") as mock_level_info, \
        patch("logging.Logger.warning") as mock_level_warning,\
        patch("logging.Logger.error") as mock_level_error:

        log_event(username, status)

        if expected_log_level == "info":
            mock_level_info.assert_called_once()
            mock_level_warning.assert_not_called()
            mock_level_error.assert_not_called()

        elif expected_log_level == "warning":
            mock_level_warning.assert_called_once()
            mock_level_info.assert_not_called()
            mock_level_error.assert_not_called()

        elif expected_log_level == "error":
            mock_level_error.assert_called_once()
            mock_level_info.assert_not_called()
            mock_level_warning.assert_not_called()





