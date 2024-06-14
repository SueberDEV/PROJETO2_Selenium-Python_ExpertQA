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
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
    yield driver
    driver.quit()

def fill_input_field(driver, by, value, text):
    # Espera até que o campo de entrada esteja visível, limpa e envia o texto
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((by, value))
    )
    element.clear()
    element.send_keys(text)

def click_element(driver, by, value):
    # Espera até que o elemento seja clicável e clica nele
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((by, value))
    )
    driver.execute_script("arguments[0].click();", element)

def test_register_account(driver: WebDriver):
    # Preenche todos os campos necessários para o registro
    fill_input_field(driver, By.ID, "input-firstname", "User")
    fill_input_field(driver, By.ID, "input-lastname", "Tester")
    fill_input_field(driver, By.ID, "input-email", "user@tester.com")
    fill_input_field(driver, By.ID, "input-telephone", "111222333")
    fill_input_field(driver, By.ID, "input-password", "changepass123#")
    fill_input_field(driver, By.ID, "input-confirm", "changepass123#")

    # Marca a opção de receber newsletter e aceita os termos
    click_element(driver, By.ID, "input-newsletter-yes")
    click_element(driver, By.ID, "input-agree")

    # Clica no botão de continuar para finalizar o registro
    click_element(driver, By.CSS_SELECTOR, "input.btn.btn-primary")
