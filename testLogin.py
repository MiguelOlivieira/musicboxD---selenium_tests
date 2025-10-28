from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os


caminho_registro = 'http://localhost:5173/#/register'
caminho_login = 'http://localhost:5173/#/login'
caminho_home = 'http://localhost:5173/#/'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


user = {
    "email": "",
    "senha": "",
}

# Função responsável por realizar o teste de cadastro na aplicação
def test_register():

    # Abre a página de cadastro
    driver.get(caminho_registro)

    # Aguarda 3 segundos 
    time.sleep(3)

    # Localiza os campos de nome e email
    # O XPATH permite encontrar elementos HTML com base em atributos ou hierarquia, no caso, atraves do input e o seu placeholder
    campoNome = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui seu nome completo']")
    campoEmail = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui seu Email cadastrado']")

    # Espera 1 segundo 
    time.sleep(1)

    # Digita um nome no campo de nome
    campoNome.send_keys("Renato e Miguel")

    # Aguarda 3 segundos e limpa o campo
    time.sleep(3)
    campoNome.clear()

    # Aguarda mais 3 segundos e insere novamente um nome
    time.sleep(3)
    campoNome.send_keys("Leonardo Oliveira")

    # Digita o email no campo de email
    campoEmail.send_keys("LeoOliveiraBlox@gmail.com")

    # Aguarda 2 segundos antes de prosseguir
    time.sleep(2)

    # Captura o valor digitado no campo de email e armazena na variável usuarioEmail
    usuarioEmail = campoEmail.get_attribute("value")

    # Localiza e clica no botão "Avançar" 
    driver.find_element(By.XPATH, "//input[@value='Avançar']").click()

 
    time.sleep(2)

    # Localiza os campos de senha e confirmação de senha
    campoSenha = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui a sua senha']")
    campoSenhaConfirmar = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui a sua senha novamente']")

    # Digita a senha e a confirmação da senha
    campoSenha.send_keys("12345678")
    campoSenhaConfirmar.send_keys("12345678")

    time.sleep(3)

    # Captura o valor da senha digitada e armazena na variável usuarioSenha
    usuarioSenha = campoSenha.get_attribute("value")

    # Localiza e clica no botão "Cadastrar-se", enviando o formulario de cadastro
    driver.find_element(By.XPATH, "//input[@value='Cadastrar-se']").click()

    # Aguarda 3 seg
    time.sleep(3)

    # Seleciona o alerta exibido pelo navegador (alerta de confirmação de cadastro) e fecha o alerta.
    alert = driver.switch_to.alert
    alert.accept()
    
    # Verifica se o redirecionamento após o cadastro foi feito corretamente para a tela de login
    if(driver.current_url == caminho_login):
        print("Cadastro feito com sucesso!")
        # Armazena os dados de email e senha no dicionário do usuário
        user["email"] = usuarioEmail
        user["senha"] = usuarioSenha
    else:
        print('Não foi possível concluir o cadastro.')

    # Aguarda 5 segundos antes de encerrar a função (visualização do resultado)
    time.sleep(5)
    

# Função responsável por realizar o teste de login na aplicação
def test_login():
    
     # Executa primeiro o teste de cadastro para garantir que o usuário exista
     test_register()

     # Localiza os campos de email e senha da tela de login
     campoEmail = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui seu Email cadastrado']")
     campoSenha = driver.find_element(By.XPATH, "//input[@placeholder='Digite aqui sua senha']")
    
     # Preenche os campos de login com os dados de teste
     campoEmail.send_keys("LeoOliveiraBlox@gmail.com")
     campoSenha.send_keys("12345678")
    
     # Localiza e clica no botão "ENTRAR" para tentar o login
     driver.find_element(By.XPATH, "//input[@value='ENTRAR']").click()
     
     # Aguarda 3 segundos para o redirecionamento
     time.sleep(3)

     # Verifica se o login foi bem-sucedido, validando se a URL atual é a da página inicial
     if(driver.current_url == caminho_home):
        print('Login realizado com sucesso!')
     else:
        print('Não foi possível logar no sistema, verifique o email ou a senha')

# Executa a função de login (que automaticamente executa o cadastro antes)
test_login()
