# programa em python para gerenciar uma agenda telefônica:
# valida Dados de Contato: Recebe e valida nomes e números de telefone.
# armazena Dados em um Dicionário: Usa um dicionário para armazenar contatos, onde a chave é o nome e o valor é o número de telefone.
# salva e Carrega Dados em Arquivo .json: Grava e lê os dados em um arquivo JSON.

# estrutura do programa
# coletar e validar Dados:
# receber nome e número de telefone do usuário.
# validar o formato do número de telefone.
# manipular dados:
# adicionar, editar e excluir contatos no dicionário.
# salvar e carregar dados:
# gravar e ler dados em um arquivo JSON.

# adicionei a função validar_email para validar o email do contato.
# adicionei a função apagar_dados para apagar todos os contatos no dicionário.
# adicionei a função apagar_contato para apagar um contato específico no dicionário.

from AgendaCompleta_Func import *

nome_arquivo = 'agenda_telefonica.json'
contatos = carregar_do_arquivo(nome_arquivo)

while True:

    print("\nMenu:")
    print("1. Adicionar Contato")
    print("2. Editar Contato")
    print("3. Exibir Contatos")
    print("4. Apagar Contato")
    print("5. Apagar Dados")
    print("6. Salvar e Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        novos_contatos = coletar_dados()
        contatos.update(novos_contatos)
    elif escolha == '2':
        menu_edicao(contatos)
    elif escolha == '3':
        exibir_contatos(contatos)
    elif escolha == '4':
        apagar_contato(contatos)
    elif escolha == '5':
        apagar_dados(contatos)
    elif escolha == '6':
        salvar_em_arquivo(contatos, nome_arquivo)
        break
    else:
        print("Opção inválida. Tente novamente.")
