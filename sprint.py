from matrizes import logo
from dicionários import noticias
from dicionários import Pilotos
from Listas import Mr, participantes1, participantes2, votos1, votos2


# Funções:

def existe_na_lista(info, lista):
    for i in lista:
        if i == info:
            return True
    return False



def acha_index (info, lista):
    for i in range (len(lista)):
        if info == lista[i]:
            return i


def num_int(msg):
    while True:
        x = input(msg)
        if x.isnumeric():
            x = int(x)
            return x

def opcoes_resposta(lista1, msg):
    while True:
        print(f"{msg} (selecione uma das opções abaixo)")
        for i in lista1:
            print(f"- {i}")
        x = input("-->  ")
        x = x.lower()
        lista2 = []
        for i in lista1:
            i = i.lower()
            lista2.append(i)
        if x in lista2:
            return x

def opcoes_resposta_sem_print(lista, msg):
    while True:
        print(f"{msg} (selecione uma das opções acima)")
        x = input("-->  ")
        if x in lista:
            return x

def votar ():
    lista_candidatos = []
    resposta = opcoes_resposta(Mr, "Escolha um dos países acima: ")
    i = acha_index(resposta, Mr)
    lista_candidatos.append(participantes1[i])
    lista_candidatos.append(participantes2[i])
    resposta = opcoes_resposta(lista_candidatos, "Em qual candidato você deseja votar: ")
    resposta2 = existe_na_lista(resposta, participantes1)
    if resposta2:
        votos1[i] += 1
    else:
        votos2[i] += 1

def print_resultados():
    for i in range(len(Mr)):
        print(f"{Mr[i]}: \n  {participantes1[i]} - {votos1[i]} votos \n  {participantes2[i]} - {votos2[i]} votos")

def opcoes_resposta_servicos(lista1, msg):
    while True:
        print(f"{msg} (selecione uma das opções abaixo)")
        for i in lista1:
            print(f"- {i}")
        x = input("-->  ")
        x = x.lower()
        lista2 = []
        for i in lista1:
            i = i.lower()
            lista2.append(i)
        for i in range(len(lista2)):
            if x == lista2[i]:
                return lista1[i]




def login_user (login_matriz, user_list, password_list):
    while True:
        teste = opcoes_resposta(["sim", "não"], "Você ja possui uma conta?")
        if teste in ["sim", "não"]:
            break
    if teste == "sim":
        user = input("Informe o seu usuário: ")
        password = input("Informe a sua senha: ")
        if user in user_list and password in password_list:
            usuário_atual = user
            return True
        else:
            teste = "não"
            print("Usuario ou senha não correspondentes!")
    if teste == "não":
        print("Vamos criar uma nova conta de acesso!")
        new_user = input("Informe um usuário: ")
        while new_user in user_list:
             new_user = input("Informe um usuário: ")
        new_password = input("Informe uma senha: ")
        confirmn_password = input("Confirme a sua senha: ")
        while new_password != confirmn_password or new_password in password_list:
            print("As senhas devem coincidir!")
            new_password = input("Informe uma senha: ")
            confirmn_password = input("Confirme a sua senha: ")
        user_list.append(new_user)
        password_list.append(new_password)
        login_matriz.append(user_list)
        login_matriz.append(password_list)

    return login_matriz




# Listas e variaves padrões:

login_matriz = []

user_list = ["Léo", "Eduardo", "Luiz", "Alexandre", "Herbert"]
password_list = ["4123910784", "74123", "107439", "569324780", "123456-=789"]
teste_login = 0




# Início do código fonte:

print("Bem vindo a Mahindra Racing!")
login = opcoes_resposta(["sim", "não"], "Deseja fazer o login? \n --> ")
if login == "sim":
    login = login_user(login_matriz, user_list, password_list)
    teste_login = 1
while True:
    lista_servicos = []
    servico = opcoes_resposta(["Pilotos", "Notícias", "Família MR"], "Selecione um dos serviços disponiveis em nossa aplicação")
    if servico == "pilotos":
        for x in Pilotos:
            lista_servicos.append(x)
        servico = opcoes_resposta_servicos(lista_servicos, "Qual piloto você deseja conhecer melhor?")
        print(Pilotos[servico]["Sobre"])
    if servico == "notícias":
        for x in noticias:
            lista_servicos.append(f"{x}")
            print(f"{x} - {noticias[x]["Título"]}")
        servico = opcoes_resposta_sem_print(lista_servicos, "Qual Notícia você deseja consultar?")
        print(noticias[servico]["Título"])
        print(noticias[servico]["Conteúdo"])
    if servico == "família mr":
        if teste_login == 1:
            votar()
            resultados = opcoes_resposta(["sim", "não" ], "Deseja ver como está a votação? \n --> ")
            if resultados == "sim":
                print_resultados()
        else:
            print("Você precisa efetuar o login para poder votar!")
            login = opcoes_resposta(["sim", "não"], "Deseja fazer o login para poder votar?")
            if login == "sim":
                login = login_user(login_matriz, user_list, password_list)
                teste_login = 1
                votar()
                resultados = opcoes_resposta(["sim", "não"], "Deseja ver como está a votação? \n --> ")
                if resultados == "sim":
                 print_resultados()
    print()

    continuar = opcoes_resposta(["sim", "não"], "Deseja continuar navegando pela aplicação? \n -->")
    if continuar == "não":
        break

if teste_login == 1:
    print("Obrigado pela visita! Volte sempre")
    logo()
else:
    print("Obrigado pela visita, na próxima vez, cadastre-se para poder votar em nossos candidatos!")
    logo()


