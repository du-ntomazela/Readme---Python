from matrizes import logo
from dicionários import noticias
from dicionários import Pilotos


# Funções:


def num_int(msg):
    while True:
        x = input(msg)
        if x.isnumeric():
            x = int(x)
            return x

def opcoes_resposta(lista, msg):
    while True:
        print(f"{msg} (selecione uma das opções abaixo)")
        for i in lista:
            print(f"- {i}")
        x = input("-->  ")
        if x in lista:
            return x

def opcoes_resposta_sem_print(lista, msg):
    while True:
        print(f"{msg} (selecione uma das opções acima)")
        x = input("-->  ")
        if x in lista:
            return x


def login_user (login_matriz, user_list, password_list):
    while True:
        teste = input("Você ja possui uma conta? (responda com sim ou não) \n -> ")
        if teste in ["sim", "não"]:
            break
    if teste == "sim":
        user = input("Informe o seu usuário: ")
        password = input("Informe a sua senha: ")
        if user in user_list and password in password_list:
            return user
        else:
            teste = "não"
            print("Usuario ou senha não correspondentes!")
    if teste == "não":
        print("Vamos criar uma nova conta de acesso!")
        new_user = input("Informe um usuário: ")
        while new_user in user_list:
             new_user = input("Informe um usuário: ")
        new_password = input("Informe uma senha: ")
        confirmn_password = input("Confirme a sua senha")
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
user_list = []
password_list = []
teste_login = 0




# Início do código fonte:

print("Bem vindo a Mahindra Racing!")
login = opcoes_resposta(["sim", "não"], "Deseja fazer o login?")
if login == "sim":
    login = login_user(login_matriz, user_list, password_list)
    teste_login = 1
while True:
    lista_servicos = []
    servico = opcoes_resposta(["Pilotos", "Notícias", "Família MR"], "Selecione um dos serviços disponiveis em nossa aplicação")
    if servico == "Pilotos":
        for x in Pilotos:
            lista_servicos.append(x)
        servico = opcoes_resposta(lista_servicos, "Qual piloto você deseja conhecer melhor?")
        print(Pilotos[servico]["Sobre"])
    elif servico == "Notícias":
        for x in noticias:
            lista_servicos.append(f"{x}")
            print(f"{x} - {noticias[x]["Título"]}")
        servico = opcoes_resposta_sem_print(lista_servicos, "Qual Notícia você deseja consultar?")
        print(noticias[servico]["Título"])
        print(noticias[servico]["Conteúdo"])