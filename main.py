import os
import requests
import wget
from time import sleep
import platform

os_used = platform.system()

if (os_used == "Windows"):
    cleanScreen = "cls"
elif (os_used == "Linux"):
    cleanScreen = "clear"
else:
    cleanScreen = "clear"

messageDownload = "\n\033[1;32mDownload realizado!\033[0;0m"

def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=5)
        return True
    except requests.ConnectionError:
        print("\033[1;31mSem conexão de rede\033[0;0m.\n Encerrando...")
        exit()
    return False

def topic_cybersecurity():
    print("Papers disponiveis.")
    print(" 1 - Red Teaming (PT_BR)\n 2 - Threat Hunting (PT_BR)")
    while True:
        try:
            resp = int(input("Selecione um Paper... > "))
            break
        except ValueError:
            print("Selecione uma opção valida!")

    if (resp == 1):
        url = "https://raw.githubusercontent.com/SharpBlueRU/templo-ITA/main/artigos/paper_kosu.txt"
        wget.download(url, "Red_Teaming_Templo7k.txt")
        print(messageDownload)
    elif (resp == 2):
        url = "https://raw.githubusercontent.com/SharpBlueRU/templo-ITA/main/artigos/paper_black.txt"
        wget.download(url, "Threat_Hunting_Templo7k.txt")
        print(messageDownload)
    else:
        print("Esta paper não existe!")        

def topic_programming():
    print("Papers disponiveis.")
    print(" 1 - Bit shift operator")
    while True:
        try:
            resp = int(input("Selecione um Paper... > "))
            break
        except ValueError:
            print("Selecione uma opção valida!")

    if (resp == 1):
        url = "https://raw.githubusercontent.com/SharpBlueRU/templo-ITA/main/artigos/paper_lups.txt"
        wget.download(url, "Bit_shift_operator_Templo7k.txt")
        print(messageDownload)
    else:
        print("Este paper não existe!")        

def topic_math():
    print("Sem paper no momento...")

def download_papers():
    print(" 1 - Cybersecurity\n 2 - Programação\n 3 - Matemática")
    while True:
        try:
            resp = int(input("Selecione um tópico... > "))
            break
        except ValueError:
            print("Selecione uma opção valida!")

    if (resp == 1):
        topic_cybersecurity()
    elif (resp == 2):
        topic_programming()
    elif (resp == 3):
        topic_math()
    else:
        print("Tópico invalido!")        

def visualizer_members():
    try:
        test = open('membros.txt')
        test.close()
    except:    
        url = "https://raw.githubusercontent.com/SharpBlueRU/templo-ITA/main/artigos/membros.txt"
        wget.download(url, "membros.txt")

    viwer = open("membros.txt", "r")
    os.system(cleanScreen)
    print(viwer.read())

def menu():
    print(" 1 - Baixar papers\n 2 - Visualizar membros")

while True:
    os.system(cleanScreen)
    print("Testando conexão de rede...")
    check_internet()
    print("Conexão, \033[1;32m OK!\033[0;0m")
    sleep(1.2)
    os.system(cleanScreen)

    print("========   \033[1;34m Templo7K cli\033[0;0m   ========")
    print("  Menu Templo7k   -   by SharpBlue\n")
    menu()

    while True:
        try:
            resp = int(input("O que deseja fazer? Escolha umas das opções... > "))
            break
        except ValueError:
            print("Selecione uma opção válida!")

    if (resp == 1):
        download_papers()
    elif (resp == 2):
        visualizer_members()

    respExit = int(input("Deseja sair? [1]sair [2]Voltar ao menu. > "))

    if (respExit == 1):
        os.remove("membros.txt")
        print("Saindo...")
        sleep(1.2)
        exit()
    else:
        os.system(cleanScreen)       