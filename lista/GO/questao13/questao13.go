package main

import (
	"fmt"
)

type Matematica struct{}

func (Matematica) Fatorial(n int) int {
	if n < 0 {
		return -1
	}
	if n == 0 || n == 1 {
		return 1
	}
	resultado := 1
	for i := 2; i <= n; i++ {
		resultado *= i
	}
	return resultado
}

func main() {
	m := Matematica{}

	numero := 5
	fatorial := m.Fatorial(numero)

	if fatorial != -1 {
		fmt.Printf("O fatorial de %d é: %d\n", numero, fatorial)
	} else {
		fmt.Println("Erro")
	}
}
