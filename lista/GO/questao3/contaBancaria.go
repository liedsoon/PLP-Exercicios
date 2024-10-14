package main

import (
	"fmt"
)

type ContaBancaria struct {
	Titular string
	saldo   float64
}

func NovaContaBancaria(titular string, saldoInicial float64) ContaBancaria {
	return ContaBancaria{Titular: titular, saldo: saldoInicial}
}

func (c *ContaBancaria) GetSaldo() float64 {
	return c.saldo
}

func (c *ContaBancaria) SetSaldo(novoSaldo float64) {
	c.saldo = novoSaldo
}

func (c ContaBancaria) ExibirConta() {
	fmt.Printf("Titular: %s\n", c.Titular)
	fmt.Printf("Saldo: R$%.2f\n", c.GetSaldo())
}

func (c *ContaBancaria) Depositar(valor float64) {
	if valor > 0 {
		fmt.Printf("Depositando R$%.2f\n", valor)
		c.saldo += valor
	} else {
		fmt.Println("Valor inválido")
	}
}

func (c *ContaBancaria) Sacar(valor float64) {
	if c.saldo >= valor && valor > 0 {
		fmt.Printf("Sacando R$%.2f\n", valor)
		c.saldo -= valor
	} else {
		fmt.Println("Saldo insuficiente ou valor inválido\n")
	}
}

func (c ContaBancaria) ExibirSaldo() {
	fmt.Printf("Saldo Atual: R$%.2f\n\n", c.saldo)
}

func main() {
	c1 := NovaContaBancaria("João", 1000)

	c1.ExibirConta()

	c1.ExibirSaldo()
	c1.Depositar(500)
	c1.ExibirSaldo()
	c1.Sacar(300)
	c1.ExibirSaldo()

	c1.ExibirConta()
}
