from matrizes import logo
from dicionários import noticias

def num_int(num, msg):
    while True:
        x = input(msg)
        if x.isnumeric():
            break

def login_user ():
    login_matriz = []
    user_list = []
    password_list = []
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

