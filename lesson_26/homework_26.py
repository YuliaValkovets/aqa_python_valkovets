import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://localhost:8000/dz.html")

def verify_frame(id_frame, id_input, secret_text):
    driver.switch_to.frame(driver.find_element(By.ID, id_frame))
    input_field_frame = driver.find_element(By.ID, id_input)
    input_field_frame.send_keys(secret_text)

    check_button = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    check_button.click()

    WebDriverWait(driver, 5).until(EC.alert_is_present())
    time.sleep(2)
    alert = driver.switch_to.alert

    if alert.text == "Верифікація пройшла успішно!":
        print("Verification was successful")
    else:
        print(f"Verification was failed:{alert.text}")

    alert.accept()
    driver.switch_to.default_content()

verify_frame("frame1", "input1", "Frame1_Secret")
verify_frame("frame2", "input2", "Frame2_Secret")

driver.quit()