package main

import (
	"fmt"
)

type Animal interface {
	EmitirSom() string
}

type Cachorro struct {
	Nome string
}

func (c Cachorro) EmitirSom() string {
	return "O cachorro faz Au au"
}

type Gato struct {
	Nome string
}

func (g Gato) EmitirSom() string {
	return "O gato faz Miau"
}

type Galinha struct {
	Nome string
}

func (g Galinha) EmitirSom() string {
	return "A galinha faz Có có"
}

func EmitirSomAnimais(animais []Animal) {
	for _, animal := range animais {
		fmt.Println(animal.EmitirSom())
	}
}

func main() {
	cachorro := Cachorro{Nome: "Rex"}
	gato := Gato{Nome: "Michonne"}
	galinha := Galinha{Nome: "Rafinha"}

	animais := []Animal{cachorro, gato, galinha}

	EmitirSomAnimais(animais)
}
