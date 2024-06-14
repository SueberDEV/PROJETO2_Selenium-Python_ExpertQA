import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/forgotten")
    yield driver
    driver.quit()

def test_forgotten_pass(driver: WebDriver):
    # Espera até que o campo de email esteja visível e interage com ele
    email_address_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-email"))
    )
    email_address_input.clear()
    email_address_input.send_keys("tester@tester.com")

    # Clica no botão de continuar
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()

    # Verifica se a mensagem de sucesso esperada aparece
    message_success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(), 'An email with a confirmation link has been sent your email address.')]")
        )
    ).text

    # Compara a mensagem de sucesso com a esperada
    assert message_success == "An email with a confirmation link has been sent your email address."
