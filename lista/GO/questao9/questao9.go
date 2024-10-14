package main

import (
	"fmt"
)

type Imprimivel interface {
	Imprimir()
}

type Relatorio struct {
	Titulo   string
	Conteudo string
}

func (r Relatorio) Imprimir() {
	fmt.Printf("Relatório: %s\nConteúdo: %s\n", r.Titulo, r.Conteudo)
}

type Contrato struct {
	Nome     string
	Conteudo string
}

func (c Contrato) Imprimir() {
	fmt.Printf("Contrato:\nNome: %s\nConteudo: %s\n", c.Nome, c.Conteudo)
}

func ImprimirDocumentos(documentos []Imprimivel) {
	for _, doc := range documentos {
		doc.Imprimir()
		fmt.Println()
	}
}

func main() {
	relatorio := Relatorio{
		Titulo:   "Relatório de Vendas",
		Conteudo: "idncfojwebfjrbfoesfbvolrbfjwebf.",
	}

	// Criando um contrato
	contrato := Contrato{
		Nome:     "Termos e Condições",
		Conteudo: "wjerbfojwebfujebfienfe",
	}

	documentos := []Imprimivel{relatorio, contrato}

	ImprimirDocumentos(documentos)
}
