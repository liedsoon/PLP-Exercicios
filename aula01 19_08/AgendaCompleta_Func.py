import json
import re
def validar_numero(numero):

    #Valida se o número de telefone está no formato correto.
    #Exemplo de formato: (11) 12345-6789

    padrao = re.compile(r"^\(\d{2}\) \d{5}-\d{4}$")
    return bool(padrao.match(numero))

def validar_email(email):

    #Valida se o email está no formato correto.
    #Exemplo de formato: nome@gmail.com

    padrao = re.compile(r"^\w+@\w+\.\w{2,3}$")
    return bool(padrao.match(email))
def coletar_dados():

    #Coleta nome e número de telefone do usuário e os valida.

    contatos = {}
    while True:
        nome = input("Digite o nome do contato (ou 'voltar' para o menu inicial): ")
        if nome.lower() == 'voltar':
            break

        numero = input("Digite o número de telefone (formato: (11) 12345-6789): ")
        if not validar_numero(numero):
            print("Número de telefone inválido. Tente novamente.")
            continue

        email = input("Digite o email: ")
        if not validar_email(email):
            print("Email inválido. Tente novamente.")
            continue

        contatos[nome] = {'numero': numero, 'email': email}
        print(f"Contato '{nome}' adicionado!")

    return contatos

def salvar_em_arquivo(contatos, nome_arquivo):

    #Salva o dicionário de contatos em um arquivo JSON.

    with open(nome_arquivo, 'w') as arquivo:
        json.dump(contatos, arquivo, indent=4)

    print(f"Dados salvos em '{nome_arquivo}'.")

def carregar_do_arquivo(nome_arquivo):

    # Carrega o dicionário de contatos de um arquivo JSON.

    try:
        with open(nome_arquivo, 'r') as arquivo:
            contatos = json.load(arquivo)
    except FileNotFoundError:
        contatos = {}
    return contatos

def exibir_contatos(contatos):

    #Exibe todos os contatos no dicionário.

    if contatos:
        for nome, dado in contatos.items():
            numero = dado['numero']
            email = dado['email']
            print(f"Nome: {nome}, Telefone: {numero}, Email: {email}")
    else:
        print("Nenhum contato encontrado.")


def menu_edicao(contatos):
    while True:
        print("\nMenu de Edição:")
        print("1. Editar Nome")
        print("2. Editar Número de Telefone")
        print("3. Editar Email")
        print("4. Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            editar_nome(contatos)

        elif escolha == '2':
            editar_numero(contatos)

        elif escolha == '3':
            editar_email(contatos)

        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def editar_nome(contatos):

        #Edita o nome de um contato no dicionário.

        nome = input("Digite o nome do contato que deseja editar: ")
        if nome in contatos:
            novo_nome = input("Digite o novo nome: ")
            contatos[novo_nome] = contatos.pop(nome)
            print(f"Nome do contato '{nome}' alterado para '{novo_nome}'.")
        else:
            print(f"Contato '{nome}' não encontrado.")

def editar_numero(contatos):

    #Edita o número de telefone de um contato no dicionário.

    nome = input("Digite o nome do contato que deseja editar: ")
    if nome in contatos:
        novo_numero = input("Digite o novo número de telefone: ")
        if not validar_numero(novo_numero):
            print("Número de telefone inválido. Tente novamente.")
        else:
            contatos[nome]['numero'] = novo_numero
            print(f"Número de telefone do contato '{nome}' alterado para '{novo_numero}'.")
    else:
        print(f"Contato '{nome}' não encontrado.")

def editar_email(contatos):

        #Edita o email de um contato no dicionário.

        nome = input("Digite o nome do contato que deseja editar: ")
        if nome in contatos:
            novo_email = input("Digite o novo email: ")
            if not validar_email(novo_email):
                print("Email inválido. Tente novamente.")
            else:
                contatos[nome]['email'] = novo_email
                print(f"Email do contato '{nome}' alterado para '{novo_email}'.")
        else:
            print(f"Contato '{nome}' não encontrado.")

def apagar_contato(contatos):

    #Apaga um contato do dicionário.
    nome = input("Digite o nome do contato que deseja apagar: ")

    if nome in contatos:
        del contatos[nome]
        print(f"Contato '{nome}' apagado.")
    else:
        print(f"Contato '{nome}' não encontrado.")

def apagar_dados(contatos):

    #apaga todos os contatos no dicionário.

    contatos.clear()
    print("Todos os dados foram apagados.")