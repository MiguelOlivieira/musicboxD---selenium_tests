from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os


caminho_servidor = 'http://localhost:5173/#/register'

# Iniciar o Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Abrir a pagina da apliccacao
driver.get(caminho_servidor)

time.sleep(5)

                                        #Nota: o xpath permite  localizar pontos específicos do documento HTML com “endereços“
usuarioNome = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui seu nome completo']")
usuarioEmail = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui seu Email cadastrado']")

time.sleep(1)



usuarioNome.send_keys("Leonardo Oliveira")
usuarioEmail.send_keys("LeoOliveiraBlox@gmail.com")

time.sleep(3)