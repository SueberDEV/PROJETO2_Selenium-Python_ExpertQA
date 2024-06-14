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
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    yield driver
    driver.quit()

def login(driver, username, password):
    # Espera até que o campo de email esteja visível e interage com ele
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-email"))
    )
    email_input.clear()
    email_input.send_keys(username)

    # Interage com o campo de senha
    password_input = driver.find_element(By.ID, "input-password")
    password_input.clear()
    password_input.send_keys(password)

    # Clica no botão de login
    login_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary")
    login_button.click()

def test_exceeded_allowed_logins(driver: WebDriver):
    # Realiza o login com credenciais inválidas repetidamente até que a conta seja bloqueada
    login(driver, "standard_user", "secret_sauce")

    # Verifica se a mensagem de erro esperada aparece
    message_fail = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(), 'Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.')]")
        )
    ).text

    # Compara a mensagem de erro com a esperada
    assert message_fail == "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
