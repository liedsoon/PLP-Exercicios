package main

import (
	"fmt"
)

func main() {

	//Cria um vetor de 10 elementos inteiros
	vetor := []int{5, 12, 7, 20, 15, 8, 3, 11, 6, 9}

	// Calcula a media, o maior valor e o menor valor

	soma := 0
	maiorValor := vetor[0]
	menorValor := vetor[0]

	for _, valor := range vetor {
		soma += valor

		if valor > maiorValor {
			maiorValor = valor
		}

		if valor < menorValor {
			menorValor = valor
		}
	}

	media := float64(soma) / float64(len(vetor))
	//Exibe os resultados

	fmt.Printf("Media: %.2f\n", media)
	fmt.Printf("Maior valor: %d\n", maiorValor)
	fmt.Printf("Menor valor: %d\n", menorValor)

}