package main

import (
	"fmt"
)

type Empregado struct {
	Nome    string
	Cargo   string
	Salario float64
}

func (e Empregado) ExibirInformacoes() {
	fmt.Printf("Nome: %s\nCargo: %s\nSalário: R$%.2f\n", e.Nome, e.Cargo, e.Salario)
}

type Empresa struct {
	Nome       string
	Empregados []*Empregado
}

func (e *Empresa) AdicionarEmpregado(empregado *Empregado) {
	e.Empregados = append(e.Empregados, empregado)
}

func (e Empresa) ExibirEmpregados() {
	fmt.Printf("Empresa: %s\n", e.Nome)
	fmt.Println("Empregados:")
	for _, empregado := range e.Empregados {
		empregado.ExibirInformacoes()
		fmt.Println()
	}
}

func main() {
	empresa := Empresa{Nome: "Serasa"}

	// Criando empregados
	empregado1 := Empregado{Nome: "João", Cargo: "Desenvolvedor", Salario: 6000.00}
	empregado2 := Empregado{Nome: "Maria", Cargo: "Gerente ", Salario: 8000.00}
	empregado3 := Empregado{Nome: "José", Cargo: "Designer", Salario: 5500.00}

	empresa.AdicionarEmpregado(&empregado1)
	empresa.AdicionarEmpregado(&empregado2)
	empresa.AdicionarEmpregado(&empregado3)

	empresa.ExibirEmpregados()
}
