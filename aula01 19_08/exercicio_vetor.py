#lê um vetor de 8 posições e, em seguida, lê dois valores X e Y
#quaisquer correspondentes a duas posições no vetor.
#o programa então imprime a soma dos valores encontrados nas respectivas posições X e Y.

from funcao import lerValores, valoresXeY, somaValores
def main():
    # lê os valores do vetor
    vetor = lerValores()

    # lê os valores de x e y
    x, y = valoresXeY()

    # soma os valores de x e y
    soma = somaValores(vetor, x, y)

    # imprime a soma
    print(f"A soma dos valores encontrados nas respectivas posições {x} e {y} é {soma}.")

main()