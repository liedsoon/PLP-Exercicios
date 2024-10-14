package main

import (
	"fmt"
)

type Escola struct {
	Nome        string
	Professores []*Professor
}

func (e *Escola) AdicionarProfessor(p *Professor) {
	e.Professores = append(e.Professores, p)
}

func (e Escola) ExibirProfessores() {
	fmt.Printf("Escola: %s\n", e.Nome)
	fmt.Println("Professores:")
	for _, professor := range e.Professores {
		fmt.Printf("° %s\n", professor.Nome)
	}
}

type Professor struct {
	Nome    string
	Escolas []*Escola
}

func (p *Professor) AdicionarEscola(e *Escola) {
	p.Escolas = append(p.Escolas, e)
}

func (p Professor) ExibirEscolas() {
	fmt.Printf("Professor: %s\n", p.Nome)
	fmt.Println("Escolas:")
	for _, escola := range p.Escolas {
		fmt.Printf("° %s\n", escola.Nome)
	}
}

func main() {
	escola1 := Escola{Nome: "Escola A"}
	escola2 := Escola{Nome: "Escola B"}

	professor1 := Professor{Nome: "Maria"}
	professor2 := Professor{Nome: "João"}

	escola1.AdicionarProfessor(&professor1)
	escola1.AdicionarProfessor(&professor2)
	escola2.AdicionarProfessor(&professor2)

	professor1.AdicionarEscola(&escola1)
	professor2.AdicionarEscola(&escola1)
	professor2.AdicionarEscola(&escola2)

	escola1.ExibirProfessores()
	escola2.ExibirProfessores()

	professor1.ExibirEscolas()
	professor2.ExibirEscolas()
}
