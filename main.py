import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg

Voto = []
Candidatos = ["Juscelino Kubistchek", "Getulio Vargas", "Jânio Quadros", "João Goulart"]
Sexo = ["M","F"]
Sexo_Entrevistado = []
Mes = [1,2,3,4,5,6,7,8,9,10,11,12]
Mes_da_apuração = []
Numero_Candidato = [10,20,30,40]


def Votação():
    contador = 0
    layout = [
        [sg.Text("Diga o Mês: ")],
        [sg.Combo(values=Mes, key="Mes", size=(20, 1))],
        [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
    ]
    janela = sg.Window('Informe o mês da pesquisa', layout, element_justification='center')
    evento,dados = janela.read()
    Mes_da_apuração.append(dados["Mes"])
    janela.close()
    while contador < 10:
        layout = [
            [sg.Text("Diga o Numero do Candidato(10-Juscelino, 20-Getulio, 30-Jânio, 40-João): ")],
            [sg.Combo(values=Numero_Candidato,key="numero",size=(20,1))],
            [sg.Text("Diga o sexo do entrevistado ")],
            [sg.Combo(values=Sexo,key="sexo",size=(20,1))],
            [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
        ]

        janela = sg.Window('Bem -vindo as eleições', layout, element_justification='center')
        evento, dados = janela.read()
        Voto.append(dados['numero'])
        if dados['sexo'] == "F":
            Sexo_Entrevistado.append(10)
        else:
            Sexo_Entrevistado.append(20)


        janela.close()
        contador+=1

def Serialização():
    file = open("Eleições.txt",'w')
    file.write(str(Mes_da_apuração)+"\n"+str(Voto) + "\n"+str(Sexo_Entrevistado))
    file.close()



def MostraGraficoPizza():
    ContagemVotoJuscelino = 0
    ContagemVotoGetulio = 0
    ContagemVotoJanio = 0
    ContagemVotoJoao = 0
    Votos = []
    layout = [
        [sg.Text("Diga o Mês que você quer saber o resultado: ")],
        [sg.Combo(values=Mes, key="Mes", size=(20, 1))],
        [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
    ]
    janela = sg.Window('Informe o mês da pesquisa', layout, element_justification='center')
    evento, dados = janela.read()
    Mes_Visualizar = dados["Mes"]
    janela.close()
    file = open("Eleições.txt", "r")
    while(str(Mes_Visualizar) not in file.read()):
        layout = [
            [sg.Text("Diga o Mês novamente: ")],
            [sg.Combo(values=Mes, key="Mes", size=(20, 1))],
            [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
        ]
        janela = sg.Window('Informe o mês da pesquisa', layout, element_justification='center')
        evento, dados = janela.read()
        Mes_Visualizar = dados["Mes"]
        janela.close()
    file.close()
    file = open("Eleições.txt","r")
    Trash = file.readline()
    Votos = file.readline()
    for i in range(len(Votos)):
        if Votos[i:i+2] == '10':
            ContagemVotoJuscelino += 1
        elif Votos[i:i+2] == '20':
            ContagemVotoGetulio += 1
        elif Votos[i:i+2] == '30':
            ContagemVotoJanio += 1
        elif Votos[i:i+2] == '40':
            ContagemVotoJoao += 1
    Apuração = [ContagemVotoJuscelino, ContagemVotoGetulio, ContagemVotoJanio, ContagemVotoJoao]
    plt.pie(Apuração, labels=Candidatos, autopct='%1.0f%%')
    plt.show()

def MostraRelaçãogeneroCandidato():
    ContagemVotoJuscelino = 0
    ContagemVotoGetulio = 0
    ContagemVotoJanio = 0
    ContagemVotoJoao = 0
    ContagemFemininoJuscelino = 0
    ContagemFemininoGetulio = 0
    ContagemFemininoJanio = 0
    ContagemFemininoJoao = 0
    file = open("Eleições.txt", "r")
    Trash = file.readline()
    Votos = file.readline()
    Sexo = file.readline()

    for i in range(len(Votos)):
        if Votos[i:i+2] == '10':
                if Sexo[i:i+2] == '10':
                    ContagemFemininoJuscelino+=1
                ContagemVotoJuscelino += 1
        elif Votos[i:i+2] == '20':
            if Sexo[i:i+2] == '10':
                ContagemFemininoGetulio+=1
            ContagemVotoGetulio += 1
        elif Votos[i:i+2] == '30':
            if Sexo[i:i+2] == '10':
                ContagemFemininoJanio+=1
            ContagemVotoJanio += 1
        elif Votos[i:i+2] == '40':
            if Sexo[i:i+2] == '10':
                ContagemFemininoJoao+=1

    Apuração = [ContagemVotoJuscelino, ContagemVotoGetulio, ContagemVotoJanio, ContagemVotoJoao]
    genero_Candidato = [ContagemFemininoJuscelino,ContagemFemininoGetulio,ContagemFemininoJanio,ContagemFemininoJoao]
    plt.bar(Numero_Candidato,Apuração,color='b', label="Votos Masculinos")
    plt.bar(Numero_Candidato,genero_Candidato,color='pink',label="Votos Femininos")
    plt.legend()
    plt.show()

escolha = ''
while escolha != '5-sair':

    opções = ['1 - Fazer votação', '2 - Serializar', '3 - Mostra resultado do mes', '4 - Relação Candidato genero','5-sair']

    layout = [
        [sg.Listbox(values=opções, size=(30, 6), key='esc')],
        [sg.Button('OK')]
    ]
    janela = sg.Window('Menu principal', layout)
    evento, dados = janela.read()

    if len(dados) > 0:
        escolha = dados['esc'][0]
    janela.close()


    if escolha == '1 - Fazer votação':
          Votação()

    if escolha == '2 - Serializar':
          Serialização()

    if escolha == '3 - Mostra resultado do mes':
        MostraGraficoPizza()

    if escolha == '4 - Relação Candiadto genero':
        MostraRelaçãogeneroCandidato()










