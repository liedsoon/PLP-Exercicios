#Faça um programa em python que receba do usuario dois vetores, a e b, com 10 numeros inteiros cada.
#Crie um novo vetor denominado c calculando c = a + b.
#Mostre na tela os dados do vetor c.

def main():
    vetor_a = []
    vetor_b = []
    vetor_c = []

    for i in range(10):
        vetor_a.append(int(input("Digite o elemento %d do vetor na posição A: " % i)))
        vetor_b.append(int(input("Digite o elemento %d do vetor na posição B: " % i)))

    for i in range(10):
        vetor_c.append(vetor_a[i] + vetor_b[i])

    print("Vetor C: ")
    for i in range(10):
        print(vetor_c[i])

main()