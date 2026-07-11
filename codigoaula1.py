# bibliotecas = pacotes de código
# pip install -  comando para instalar bibliotecas
# pip install pyautogui - biblioteca do python que controla o mouse e teclado

#Passo a passo do programa - pensamento computacionaç
# Passo 1: Entrara no sistema da empresa
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 Produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos

# import - comando para puxar a bliblioteca
# import pyautogui usar isso no início do seu código 
# ele controla seu mouse e teclado, faz ações nele
import pyautogui
import time # biblioteca que controla o tempo do programa, faz pausas, espera, etc
import keyboard

# variável de controle
parar_programa = False

def parar():
    global parar_programa
    parar_programa = True
    print("ESC pressionado! Parando após o produto atual...")

# registra o ESC como "escutador" em segundo plano
keyboard.add_hotkey("esc", parar)

# comandos básicos do pyautogui
# pyautogui.click(x=100, y=200) # clicar em um ponto da tela
# pyautogui.write('meu usuario') # escrever algo no teclado
# pyautogui.press('enter') # apertar uma tecla do teclado
# pyautogui.hotkey('ctrl', 's') # apertar uma combinação de teclas


# Passo 1 : Entrar no sistema da empresa
# abrir o navegador (chrome)
pyautogui.PAUSE = 0.3 # pausa de 0.3 segundos entre cada ação do pyautogui
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2) 
pyautogui.write(link)
time.sleep(2) 
pyautogui.press("enter")
time.sleep(3) #fazer uma pausa maior pro site carregar

# Passo 2: Fazer login
# ir no arquivo auxiliaraula1 para executar código que pega a posição do mouse
# time.sleep(5)
# print(pyautogui.position())

# clicar no campo de email
pyautogui.click(x=3448, y=1126) # clicar no campo de email
pyautogui.write("glaucia.fumes@gmail.com") # escrever o email
pyautogui.press("tab") # apertar a tecla tab para ir pro campo de senha
pyautogui.write("123456") # escrever a senha
pyautogui.press("enter") # apertar enter para logar
# fazer uma pausa maior pro site carregar
time.sleep(3)

# Passo 3: Abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl # instalar biblioteca pandas e openpyxl
# pandas.read_excel(sheet_name="Planilha1") # ler a aba do excel

import pandas as pd # importar a biblioteca pandas
tabela = pd.read_csv("produtos.csv") # ler o arquivo excel 
print(tabela) # mostrar a tabela no terminal

# for linha in tabela.index - repetir um série de comandos  
# depois de inserir "for linha in tabela.indexs" selecionar todas as linhas baixo que eu quero repetir
# e apertar tab - ai essas linhas vão ser agora um identação

# index é selecinar linha por linha - indexando a linha 1 depois a linha 2 e etc..

# no python não conta a linha cabeçalho - então a primeira linha de dados é a linha 0, a segunda linha 
# de dados é a linha 1 e etc..

for linha in tabela.index: 
     # verifica se a tecla ESC foi pressionada, se sim, para o programa (funciona a qualquer momento):
    if parar_programa:
        print("Programa interrompido pelo usuário (ESC pressionado)")
        break
    
    # Passo 4: Cadastrar 1 Produto
    
    pyautogui.click(x=3470, y=871) # clicar no campo do código

    # codigo = tabela.loc[linha, "codigo"] # localizar um informação linha x coluna (ex: coluna: código x linha: 1)
    # o pyautogui entende sempre em texto então passar a informação para testo usar str
    # str trasnforma qlq coisa em texto - str(variavel) - str(1) = "1" - str(1.5) = "1.5" - str(True) = "True"
    # obrigatório o srt apenas em variáveis de número, mas podemos colocar em todos por precaução
    
    # codigo
    codigo = str(tabela.loc[linha, "codigo"]) # pode colocar o srt aqui ou em pyautogui.write(codigo)
    pyautogui.write(codigo) # escrever manual - pode colcocar o srt aqui tb
    pyautogui.press("tab") # apertar a tecla tab para ir pro campo da marca
    
    # marca
    marca = str(tabela.loc[linha, "marca"]) 
    pyautogui.write(marca) # escrever a marca do produto
    pyautogui.press("tab") # apertar a tecla tab para ir pro campo do tipo 

    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo) # escrever o tipo do produto
    pyautogui.press("tab") # apertar a tecla tab para ir pro campo da

    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria) # escrever a categoria do produto
    pyautogui.press("tab") # apertar a tecla tab para ir pro campo do preço unitário

    # preço unitário
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])    
    pyautogui.write(preco_unitario) # escrever o preço unitário do produto
    pyautogui.press("tab") # apertar a tecla tab para ir pro campo do custo

    # custo
    custo = str(tabela.loc[linha, "custo"]) 
    pyautogui.write(custo) # escrever o custo do produto
    pyautogui.press("tab") # apertar a tecla tab para ir pro campo da observação

    # obs
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs) # escrever a observação do produto
    pyautogui.press("tab") # apertar a tecla tab para ir pro campo do botão salvar
    pyautogui.press("enter") # apertar a tecla enter para salvar o produto
    time.sleep(2) 
    
    # scroll voltar para o inicio da página (tela)
    # ir testando o valor ou colocar um valor alto para voltar pro inicio da página "5000"
    # menos vai pra baixo da tela (-100) positivo vai pra cima da tela (100)
    # pyautogui.moveTo(x=1728, y=800)  # ajuste pra um ponto no meio da tela do seu monitor
    # pyautogui.scroll(100000)
    # time.sleep(2)
    pyautogui.hotkey("ctrl", "home")
    time.sleep(2)
    
    
    # Passo 5: Repetir o passo 4 até acabar a lista de produtos


