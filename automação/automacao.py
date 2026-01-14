# Passo a passo do meu programa
# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer LOgin
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 até abacar a lista de Produtos

#bibliotecas utilizadas:
# pip install pandas openpyxl
# pip install  pyautogui

import pyautogui
import time
pyautogui.PAUSE = 0.5 #esperar 5 segundos a cada comando do pyautogui
# ex: Comandos pyautogui
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

# Passo 1: Entrar no sistema da empresa

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #salvando em uma variavel
pyautogui.write(link)
pyautogui.press("enter")

#fazer uma pausa maior para esperar o site carregar
time.sleep(3)

# Passo 2: Fazer LOgin

#clicar no campo de e-mail
pyautogui.click(x=889, y=398)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passar para o proximo campo
pyautogui.write("senhaAleatoria")
pyautogui.press("enter")
time.sleep(3) #pausa para o site carregar

# Passo 3: Abrir a base de dados

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)


# Passo 4: Cadastrar 1 produto

#clicar em fechar popup
pyautogui.click(x=1711, y=370)

# pegar da tabela o valor do campo que a gente quer preencher
for linha in tabela.index:
    
    # clicar no campo de código
    pyautogui.click(x=917, y=290)
    
    # preencher o codigo
    codigo = tabela.loc[linha, "codigo"] #loc, pega uma informação em especifico, como no nosso caso é uma linha, criamos a variavel linha
    pyautogui.write(str(codigo)) # o str transforma os numeros em textos, evitando erros
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher a marca
    marca = (str(tabela.loc[linha, "marca"]))
    pyautogui.write(marca)
    pyautogui.press("tab")
     # preencher o tipo
    tipo = (str(tabela.loc[linha, "tipo"]))
    pyautogui.write(tipo)
    pyautogui.press("tab")
     # preencher a categoria
    categoria = (str(tabela.loc[linha, "categoria"]))
    pyautogui.write(categoria)
    pyautogui.press("tab")
     # preencher o preco unitario
    preco = (str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.write(preco)
    pyautogui.press("tab")
     # preencher o custo
    custo = (str(tabela.loc[linha, "custo"]))
    pyautogui.write(custo)
    pyautogui.press("tab")
     # preencher a observacao, se nao for nulo
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): #se o campo obs for null, basta ir para o proximo campo
        obs = (str(tabela.loc[linha, "obs"]))
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim