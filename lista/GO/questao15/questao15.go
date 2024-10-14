package main

import (
	"fmt"
)

type SaldoInsuficienteError struct {
	Valor float64
}

func (e *SaldoInsuficienteError) Error() string {
	return fmt.Sprintf("Saldo insuficiente para saque de R$%.2f", e.Valor)
}

type ContaBancaria struct {
	Titular string
	Saldo   float64
}

func (c *ContaBancaria) Depositar(valor float64) {
	if valor > 0 {
		c.Saldo += valor
	} else {
		fmt.Println("Valor inválido.")
	}
}

func (c *ContaBancaria) Sacar(valor float64) error {
	if valor > c.Saldo {
		return &SaldoInsuficienteError{Valor: valor}
	}
	c.Saldo -= valor
	return nil
}

func (c *ContaBancaria) ExibirConta() {
	fmt.Printf("Titular: %s\n", c.Titular)
	fmt.Printf("Saldo: R$%.2f\n", c.Saldo)
}

func main() {
	conta := ContaBancaria{Titular: "João", Saldo: 1000}
	conta.ExibirConta()

	if err := conta.Sacar(300); err == nil {
		fmt.Println("Saque realizado com sucesso.")
	} else {
		fmt.Println("Erro:", err)
	}

	conta.ExibirConta()

	if err := conta.Sacar(1000); err != nil {
		fmt.Println("Erro:", err)
	}
}
