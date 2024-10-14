/*
Crie uma classe Carro com atributos como marca, modelo, e
ano. Instancie três objetos dessa classe e exiba os detalhes de cada um.
*/
package main

import (
	"fmt"
)

type Carro struct {
	Marca  string
	Modelo string
	Ano    int
}

func main() {
	carro1 := Carro{Marca: "Fiat", Modelo: "Uno", Ano: 2020}
	carro2 := Carro{Marca: "Chevrolet", Modelo: "Onix", Ano: 2020}
	carro3 := Carro{Marca: "Volkswagen", Modelo: "Gol", Ano: 2010}

	fmt.Println("Detalhes do Carro 1:")
	fmt.Printf("Marca: %s, Modelo: %s, Ano: %d\n", carro1.Marca, carro1.Modelo, carro1.Ano)

	fmt.Println("Detalhes do Carro 2:")
	fmt.Printf("Marca: %s, Modelo: %s, Ano: %d\n", carro2.Marca, carro2.Modelo, carro2.Ano)

	fmt.Println("Detalhes do Carro 3:")
	fmt.Printf("Marca: %s, Modelo: %s, Ano: %d\n", carro3.Marca, carro3.Modelo, carro3.Ano)
}
