from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# --- Configuração Inicial ---
caminho_home = 'http://localhost:5173/#'

# Inicia o driver do Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1. Navega para a página inicial
driver.get(caminho_home)
time.sleep(2)

# 2. Clica no elemento "pesquisar"
driver.find_element(By.ID, "pesquisar").click()
time.sleep(2)

# 3. Clica no elemento "em alta"
driver.find_element(By.ID, "emAlta").click()
time.sleep(2)

# 4. Clica no elemento "perfil"
driver.find_element(By.ID, "perfil").click()

# --- Voltando ---
time.sleep(3)

driver.back()
time.sleep(2)

driver.back()
time.sleep(2)

driver.back()
time.sleep(2)

driver.quit()
