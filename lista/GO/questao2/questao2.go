package main

import (
	"fmt"
)

// Definindo a estrutura Carro
type Carro struct {
	Marca      string
	Modelo     string
	Ano        int
	Velocidade int
}

// Função para criar um novo Carro
func NovoCarro(marca, modelo string, ano int) Carro {
	return Carro{Marca: marca, Modelo: modelo, Ano: ano, Velocidade: 0}
}

// Método para acelerar o carro
func (c *Carro) Acelerar(potencia int) {
	fmt.Println("Acelerando...\n")
	c.Velocidade += potencia
}

// Método para frear o carro
func (c *Carro) Frear() {
	fmt.Println("Freando...\n")
	c.Velocidade = c.Velocidade / 2
}

// Método para exibir detalhes do carro
func (c Carro) ExibirCarro() {
	fmt.Printf("Marca: %s\n", c.Marca)
	fmt.Printf("Modelo: %s\n", c.Modelo)
	fmt.Printf("Ano: %d\n", c.Ano)
	fmt.Println()
}

func (c Carro) ExibirVelocidade() {
	fmt.Printf("Velocidade Atual: %d\n\n", c.Velocidade)
}

func main() {
	carro1 := NovoCarro("Fiat", "Uno", 2020)

	carro1.ExibirCarro()

	carro1.Acelerar(10)
	carro1.ExibirVelocidade()
	carro1.Acelerar(30)
	carro1.ExibirVelocidade()

	carro1.Frear()
	carro1.Frear()
	carro1.Frear()
	carro1.ExibirVelocidade()
}
