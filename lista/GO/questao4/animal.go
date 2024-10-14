package main

import (
	"fmt"
)

type Animal interface {
	Som() string
}

type Cachorro struct {
	Nome string
}

func (c Cachorro) Som() string {
	return "Au au"
}

type Gato struct {
	Nome string
}

func (g Gato) Som() string {
	return "Miau"
}

func main() {
	cachorro := Cachorro{Nome: "Rex"}
	gato := Gato{Nome: "Michonne"}

	animais := []Animal{cachorro, gato}

	for _, animal := range animais {
		fmt.Println(animal.Som())
	}
}
