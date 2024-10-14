package main

import (
	"fmt"
)

type Motor struct {
	Potencia int
	Tipo     string
}

func (m Motor) ExibirDetalhes() {
	fmt.Printf("Motor: %d VC, Tipo: %s\n", m.Potencia, m.Tipo)
}

type Carro struct {
	Marca  string
	Modelo string
	Motor  Motor
}

func (c Carro) ExibirDetalhes() {
	fmt.Printf("Carro: %s %s\n", c.Marca, c.Modelo)
	c.Motor.ExibirDetalhes()
}

func main() {
	motor := Motor{
		Potencia: 150,
		Tipo:     "Flex",
	}

	carro := Carro{
		Marca:  "Toyota",
		Modelo: "Corolla",
		Motor:  motor,
	}

	carro.ExibirDetalhes()
}
