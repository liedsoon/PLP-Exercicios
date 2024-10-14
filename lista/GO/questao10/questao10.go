package main

import (
	"fmt"
)

type Calculadora struct{}

func (calc Calculadora) SomarDois(a, b float64) float64 {
	return a + b
}

func (calc Calculadora) SomarTres(a, b, c float64) float64 {
	return a + b + c
}

func main() {
	calculadora := Calculadora{}

	resultadoDois := calculadora.SomarDois(10, 10)
	fmt.Printf("A soma de 10 + 10 é: %.2f\n", resultadoDois)

	resultadoTres := calculadora.SomarTres(10, 10, 10)
	fmt.Printf("A soma de 10 + 10 + 10 é: %.2f\n", resultadoTres)
}
