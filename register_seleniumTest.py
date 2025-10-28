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

time.sleep(10)