from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os


caminho_registro = 'http://localhost:5173/#/register'

caminho_login = 'http://localhost:5173/#/login'

caminho_home = 'http://localhost:5173/#/'

 # Iniciar o Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


user = {
    "email": "",
    "senha": "",
}

def test_register():

    # Abrir a pagina da apliccacao
    driver.get(caminho_registro)

    time.sleep(3)

                                            #Nota: o xpath permite  localizar pontos específicos do documento HTML com “endereços“
    campoNome = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui seu nome completo']")
    campoEmail = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui seu Email cadastrado']")

    time.sleep(1)

    campoNome.send_keys("Renato e Miguel")
    time.sleep(3)
    campoNome.clear()
    time.sleep(3)
    campoNome.send_keys("Leonardo Oliveira")
    campoEmail.send_keys("LeoOliveiraBlox@gmail.com")

    time.sleep(2)

    usuarioEmail = campoEmail.get_attribute("value")
    driver.find_element(By.XPATH, "//input[@value='Avançar']").click()


    time.sleep(2)

    campoSenha = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui a sua senha']")
    campoSenhaConfirmar = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui a sua senha novamente']")

    campoSenha.send_keys("12345678")
    campoSenhaConfirmar.send_keys("12345678")

    time.sleep(3)
    
    usuarioSenha = campoSenha.get_attribute("value")
    driver.find_element(By.XPATH, "//input[@value='Cadastrar-se']").click()

    time.sleep(3)

    alert = driver.switch_to.alert
    alert.accept()
    
    if(driver.current_url == caminho_login ) :
        print("Cadastro feito com sucesso!")
        user["email"] = usuarioEmail
        user["senha"] = usuarioSenha
    else:
        print('Não foi possível concluir o cadastro.')

    time.sleep(5)
    
    

def test_login():
    
     test_register()
                                            #Nota: o xpath permite  localizar pontos específicos do documento HTML com “endereços“
     campoEmail = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui seu Email cadastrado']")
     campoSenha = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui sua senha']")
    
     campoEmail.send_keys("LeoOliveiraBlox@gmail.com")
     campoSenha.send_keys("12345678")
    
     driver.find_element(By.XPATH, "//input[@value='ENTRAR']").click()
     
     time.sleep(3)
     if(driver.current_url == caminho_home ):
        print('Login realizado com sucesso!')
     else:
        print('Não foi possível logar no sistema, verifique o email ou a senha')


# test_register()
test_login()