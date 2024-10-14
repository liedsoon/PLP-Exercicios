# coleta dados do usuario: recebe uma lista de nomes e idades.
# armazena dados em um dicionário: usa um dicionario para associar cada nome a uma idade.
#salva dados em um arquivo .txt: grava os dados armazenados no dicionario em um arquivo texto.

def coletar_dados():

    dados = []
    while True:
        nome = input("Digite o nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        idade = input("Digite a idade: ")
        try:
            idade = int(idade)
        except ValueError:
            print("Idade deve ser um número inteiro. Tente novamente.")
            continue

        dados.append({'nome': nome, 'idade': idade})
    return dados

def salvar_em_arquivo(dados, nome_arquivo):

    with open(nome_arquivo, 'w') as arquivo:
        for item in dados:
            linha = f"Nome: {item['nome']}, Idade: {item['idade']}\n"
            arquivo.write(linha)


def main():
    dados = coletar_dados()
    if dados:
        salvar_em_arquivo(dados, 'dados_pessoas.txt')
        print("Dados salvos no arquivo 'dados_pessoas.txt'.")
    else:
        print("Nenhum dado foi coletado.")

if __name__ == "__main__":
    main()
