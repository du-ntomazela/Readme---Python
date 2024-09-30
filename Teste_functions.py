
from Listas import Mr, participantes1, participantes2, votos1, votos2


#1 -  essa primeira função recebe um parametro de uma variavel(pode ser um string, booleano, integer, ou float) e recebe uma lista como segundo parametro, e verifica se o primeiro parametro está na lista que foi passada como parametro retornando True para presente e False para ausente.
def existe_na_lista(info, lista):
    for i in lista:
        if i == info:
            return True
    return False


#2 - Essa função recebe um parametro de uma variavel(pode ser um string, booleano, integer, ou float) e recebe um segundo parametro (uma lista), essa função tenta encontrar o valor passado no primeiro paramtro dentro da lista que foi passada como o segundo parametro, e retorna o inice em que o primeiro parametro está na lista.
def acha_index (info, lista):
    for i in range (len(lista)):
        lista[i] = lista[i].lower()
        if info == lista[i]:
            print(i)
            return i

#3 - uma função que recebe um valor de uma string como parametro(uma mensagem para instruir o usuario sobre o que está sendo pedido) e que é ultilizada para pedir ao usuario um número inteiro, e que caso não seja, pede novamente.
def num_int(msg):
    while True:
        x = input(msg)
        if x.isnumeric():
            x = int(x)
            return x
#4 - Essa função recebe dois parametro, uma lista com as possiveis respostas que o usuário pode digitar, e uma mensagem que vai guiar o usuario sobre o que está sendo requisitado, e vai mostrar ao usuario as opções de resposta, e enquanto o input do usuario não estiver presente na lista parametro, pede novamente o input.
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
#5 - Essa função recebe dois parametro, uma lista com as possiveis respostas que o usuário pode digitar, e uma mensagem que vai guiar o usuario sobre o que está sendo requisitado, sem mostrar as opções de respostas, e enquanto o input do usuario não estiver presente na lista parametro, pede novamente o input.

def opcoes_resposta_sem_print(lista, msg):
    while True:
        print(f"{msg} (selecione uma das opções acima)")
        x = input("-->  ")
        if x in lista:
            return x
#6 - Essa função é a principal funcionalidade da nossa aplicação! Ela é ultilizada para entrar a fundo nas informações dos participantes da solução, e assim votar no participante escolhido, essa função não precisa de parametros. Para acessar essa função, o usuário deve estar logado!
def votar ():
    lista_candidatos = []
    resposta = opcoes_resposta(Mr, "Escolha um dos países abaixo: ")
    i = acha_index(resposta, Mr)
    print(i)
    lista_candidatos.append(participantes1[i])
    lista_candidatos.append(participantes2[i])
    resposta = opcoes_resposta(lista_candidatos, "Em qual candidato você deseja votar: ")
    resposta2 = existe_na_lista(resposta, participantes1)
    if resposta2:
        votos1[i] += 1
    else:
        votos2[i] += 1

#7 - Essa função é executada caso o usuário queira ver como está indo a votação, logo após ter votado.
def print_resultados():
    for i in range(len(Mr)):
        print(f"{Mr[i]}: \n  {participantes1[i]} - {votos1[i]} votos \n  {participantes2[i]} - {votos2[i]} votos")

#8 - Essa função é ultilizada para acessar uma das funcionalidades da aplicação, ela precisa de dois parametros: a lista dos serviços disponiveis e uma mensagem de instrução que vai aparecer antes do usuario responder o input.
def opcoes_resposta_servicos(lista1, msg):
    while True:
        print(f"{msg} (selecione uma das opções abaixo)")
        for i in lista1:
            print(f"- {i}")
        x = input("-->  ")
        x = x.lower()
        for i in range(len(lista1)):
            if x == lista1[i].lower():
                return lista1[i]



#9 -  Essa função coordena os casos em que o usuario ja possui um login e senha e o caso em que ainda não possui ambos, e redireciona para outras funções dependendo do caso de haver ou não um login.
def login_user (login_matriz, user_list, password_list):
    while True:
        teste = opcoes_resposta(["sim", "não"], "Você ja possui uma conta?")
        if teste in ["sim", "não"]:
            break
    if teste == "sim":
        teste2 = teste_sim(user_list, password_list)
        if teste2:
            return
    if teste == "não":
        teste_nao(login_matriz, user_list, password_list)
    return login_matriz

#10 - Primeira segmentação da função de login de numero (9), caso em que o usuário selecionou que ja possui um login e uma senha, mas caso não correspondam com nenhum registro da aplicação redireciona para a função de criaqção de um novo login e senha.
def teste_sim ( user_list, password_list):
    user = input("Informe o seu usuário: ")
    password = input("Informe a sua senha: ")
    if user in user_list and password in password_list:
        return True
    else:
        teste = "não"
        print("Usuario ou senha não correspondentes!")

#11 - Segunda segmentação da função de login de numero (9), caso em que o usuario não possui um login e uma senha, essa função registra um novo login, e uma nova senha(essa função exige uma verificação de senha, então é requisitado que o usuário digite duas vezes a mesma senha, e caso não correspondam, pede uma nova senha que tambem será confirmada.).
def teste_nao(login_matriz, user_list, password_list):
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