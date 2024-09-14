from matrizes import logo
from dicionários import noticias

def num_int(num, msg):
    while True:
        x = input(msg)
        if x.isnumeric():
            break

def login_user ():
    user_list = []
    password_list = []
    while True:
        teste = input("Você ja possui uma conta? (responda com sim ou não) \n ->")
        if teste in ["sim", "não"]:
            break
    if teste == "sim":
        user = input("Informe o seu usuário: ")
        password = input("Informe a sua senha: ")
        if user in user_list and password in password_list:
            return user
        else:
            print("Usuario ou senha não correspondentes!")
    else:
        new_user = input("Informe um usuário: ")
        new_password = input("Informe uma senha: ")
        confirmn_password = input("Confirme a sua senha")
        