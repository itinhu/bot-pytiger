""" botão cancelar "//button[@class='ant-btn ant-btn-default']" """

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import sys
sys.setrecursionlimit(10000)



URL_DO_SITE = "https://1991bet.com/home/event"
CAMINHO_XPATH = "//div[@class='ant-space-item']//button[contains(@class, 'ant-btn-link') and span[text()='Login Agora']]"

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)

def gerar_numeros():
    i = 90000
    while i <= 99999:
        yield f'{i:05d}'
        i += 1

def tentativa():
    texto_para_inserir = next(gerador) 
    
    input_codigo_resgate.send_keys(Keys.BACK_SPACE)
    input_codigo_resgate.send_keys(Keys.BACK_SPACE)
    input_codigo_resgate.send_keys(Keys.BACK_SPACE)
    input_codigo_resgate.send_keys(Keys.BACK_SPACE)
    input_codigo_resgate.send_keys(Keys.BACK_SPACE)
    input_codigo_resgate.send_keys(Keys.BACK_SPACE)
    input_codigo_resgate.send_keys(texto_para_inserir)
    
    print('Tentativa:', texto_para_inserir)

    try:
        reinvindicar_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='ant-btn ant-btn-success oh6QhPDAAa52z_qgqBlJ']"))
        )
        driver.implicitly_wait(10)
        action = ActionChains(driver)
        action.move_to_element(reinvindicar_button).perform()
        
        reinvindicar_button.click()
        
        """ WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='ant-space-item']//button[contains(@class, 'ant-btn ant-btn-default') and span[text()='Cancelar']]"))
        )
        botao_cancelar = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-space-item']//button[contains(@class, 'ant-btn ant-btn-default') and span[text()='Cancelar']]"))
        ) """

        botao_cancelar = driver.find_element(By.XPATH, "//div[@class='ant-modal-confirm-btns']//button[contains(@class, 'ant-btn ant-btn-default') and span[text()='Cancelar']]")
        botao_cancelar.click()

        
        if botao_cancelar.is_displayed():
            tentativa() 
        
    except Exception as e:
        print(f"Erro durante a tentativa: {e}")
    finally:
        print('Achei:', texto_para_inserir)


gerador = gerar_numeros()

try:
    
    driver.get(URL_DO_SITE)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, CAMINHO_XPATH)))

    element = driver.find_element(By.XPATH, CAMINHO_XPATH)
    driver.execute_script("arguments[0].scrollIntoView();", element)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, CAMINHO_XPATH)))

    element.click()

    sleep(5)

    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Nome de Usuário']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Senha']")
    """ Campos para colocar Login e senha. """
    username_field.send_keys("pedrojr010")
    password_field.send_keys("qaz123")

    entrar_button = driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-block kKDcOuN8rOwl8zAHU1CF']")
    entrar_button.click()    

    sleep(5)

    driver.get(URL_DO_SITE)

    sleep(10)
    checkbox_nao_mostrar_hoje2 = driver.find_element(By.XPATH, ".//div[@class='WTY15hpGrP99ziiNSdSp']//input[@type='checkbox']")
    checkbox_nao_mostrar_hoje2.click()

    codigo_div = driver.find_element(By.XPATH, ".//div[@class='ant-spin-nested-loading URYVffVETVSIkPGB9P5E custom-loading__wrap']//li[@data-event-index='2']")
    codigo_div.click()

    input_codigo_resgate = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.ant-input[placeholder="Introduza o código de resgate"]'))
    )

    tentativa()
    

    sleep(50000)
    
finally:
    
    print('Fechou')