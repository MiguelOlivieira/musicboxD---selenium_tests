from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# --- Configuração Inicial ---
caminho_home = 'http://localhost:5173/#'
caminho_pesquisar = 'http://localhost:5173/#/explore'
caminho_emAlta = 'http://localhost:5173/#/trendig'
caminho_perfil = 'http://localhost:5173/#/profile'

# Inicia o driver do Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1. Navega para a página inicial
driver.get(caminho_home)
time.sleep(2)

# 2. Clica no elemento "pesquisar"
driver.find_element(By.ID, "pesquisar").click()
time.sleep(2)

if driver.current_url != caminho_pesquisar:
    print("Erro: Não navegou para a página de pesquisa corretamente.")
else:
    print("Navegação para a página de pesquisar bem-sucedida.")

# 3. Clica no elemento "em alta"
driver.find_element(By.ID, "emAlta").click()
time.sleep(2)

if driver.current_url != caminho_emAlta:
    print("Erro: Não navegou para a página de tendências corretamente.")
else:
    print("Navegação para a página de em alta bem-sucedida.")

# 4. Clica no elemento "perfil"
driver.find_element(By.ID, "perfil").click()

if driver.current_url != caminho_perfil:
    print("Erro: Não navegou para a página de perfil corretamente.")
else:
    print("Navegação para a página de perfil bem-sucedida.")
    
# --- Voltando ---
time.sleep(3)

driver.back()
time.sleep(2)

driver.back()
time.sleep(2)

driver.back()
time.sleep(2)

driver.quit()