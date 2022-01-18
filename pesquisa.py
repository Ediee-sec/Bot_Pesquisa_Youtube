from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

#Argumentos
options = Options()
options.add_argument("--disable-notifications")

#Acesso
with open('email.txt', 'r') as G:
    email = (G.read())
with open('senha.txt', 'r') as G:
    senha = (G.read())           

#Pesquisa            
pesquisa = input("Pesquisa: ")

#caminhos
clica_fazer_login = ("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button")
digita_email = ("//*[@id='identifierId']")
clica_proximo_email = ("//*[@id='identifierNext']/div/button/span")
digita_senha = ("//*[@id='password']/div[1]/div/div[1]/input")
clica_proximo_senha = ("//*[@id='passwordNext']/div/button/span")
digita_pesquisa = ("//*[@id='search']")
clica_pesquisa = ("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]")
digita_pesquisa = ("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/div/div[2]/input")
botao_pesquisa = ("//*[@id='search-icon-legacy']")
with  open('string_longo.txt') as G:
    clica_video = (G.readlines(0))


#Comandos Para acessar uma conta
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
driver.get("https://www.youtube.com")
driver.set_window_size(1024, 600)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath(clica_fazer_login).click()
driver.find_element_by_xpath(digita_email).send_keys(f'{email}')
time.sleep(2)
driver.find_element_by_xpath(clica_proximo_email).click()
time.sleep(2)
driver.find_element_by_xpath(digita_senha).send_keys(f'{senha}')
time.sleep(1.5)
driver.find_element_by_xpath(clica_proximo_senha).click()
time.sleep(1.5) 
driver.find_element_by_xpath(clica_pesquisa).click()
time.sleep(0.5)
driver.find_element_by_xpath(digita_pesquisa).send_keys(pesquisa)
time.sleep(1.5)
driver.find_element_by_xpath(botao_pesquisa).click()
time.sleep(1.5)
driver.find_element_by_xpath(clica_video).click()
time.sleep(2)
#driver.find_element_by_xpath(pausa_video).click()

#KeyK
