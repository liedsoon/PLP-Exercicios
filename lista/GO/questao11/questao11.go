package main

import (
	"fmt"
)

type Funcionario interface {
	CalcularSalario() float64
}

type FuncionarioHorista struct {
	HorasTrabalhadas float64
	ValorHora        float64
}

func (f FuncionarioHorista) CalcularSalario() float64 {
	return f.HorasTrabalhadas * f.ValorHora
}

type FuncionarioAssalariado struct {
	SalarioMensal float64
}

func (f FuncionarioAssalariado) CalcularSalario() float64 {
	return f.SalarioMensal
}

func ExibirSalario(f Funcionario) {
	fmt.Printf("Salário: R$ %.2f\n", f.CalcularSalario())
}

func main() {
	funcionarioHorista := FuncionarioHorista{
		HorasTrabalhadas: 100,
		ValorHora:        35,
	}

	funcionarioAssalariado := FuncionarioAssalariado{
		SalarioMensal: 3500,
	}

	fmt.Println("Funcionário Horista:")
	ExibirSalario(funcionarioHorista)

	fmt.Println("Funcionário Assalariado:")
	ExibirSalario(funcionarioAssalariado)
}
