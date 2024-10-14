package main

import (
	"fmt"
)

type Produto struct {
	Nome  string
	Preco float64
}

func (p Produto) Somar(outro Produto) float64 {
	return p.Preco + outro.Preco
}

func main() {
	produto1 := Produto{
		Nome:  "Livro",
		Preco: 25.50,
	}

	produto2 := Produto{
		Nome:  "Caderno",
		Preco: 40.00,
	}

	precoTotal := produto1.Somar(produto2)

	fmt.Printf("Preço total de %s e %s é: R$ %.2f\n", produto1.Nome, produto2.Nome, precoTotal)
}
