def lerValores():
    vetor = [0] * 8
    for i in range(8):
        vetor[i] = int(input("Digite o valor da posição {}: ".format(i)))
    return vetor

def valoresXeY():
    x = int(input("Digite o número x: "))
    y = int(input("Digite o número y: "))
    return x, y

def somaValores(vetor, x, y):
    soma = vetor[x] + vetor[y]
    return soma