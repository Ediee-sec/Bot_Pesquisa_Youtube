## Bot Youtube

* #### *Contexto da aplicação:*

*Bot que acessa o Youtube com E-mail e senha e faz a pesquisa de forma automatica*
****
* #### *Mapa do código:*
****
1. **Bibliotecas Python/ Comandos**
```Python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
```
****
2. **Argumentos que desabilita as notificações do navegador**
```Python
options = Options()
options.add_argument("--disable-notifications")
```
****
3. **Arquivos que contem Email e Senha, para não deixar seu acesso disponível dentro do código, crie duas pastas um Com o nome email.txt e outra com nome senha.txt**
```Python
with open('email.txt', 'r') as G:
    email = (G.read())
with open('senha.txt', 'r') as G:
    senha = (G.read())  
```
****
4. **Input onde você deve especificar qual será a consulta dentro do Yotube**
```Python          
pesquisa = input("Pesquisa: ")
```
****
5. **Variaveis que armazenam os caminhos xpath**
```Python
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
```
****
6. **Comandos que chamam as variaveis que estão com o xpath armazenados**
```Python
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
```