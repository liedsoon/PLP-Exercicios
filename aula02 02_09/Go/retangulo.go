package main

import "fmt"

//Define a estrutura Retangulo
type Retangulo struct {
	comprimento, largura float64
}

// função para calcular a area do retangulo
func (r Retangulo) calcularArea() float64 {
	return r.comprimento * r.largura
}

// func para calcular o perimetro do retangulo

func (r Retangulo) calcularPerimetro() float64 {
	return 2 * (r.comprimento + r.largura)
}

func main() {
	// Criando uma instância da estrutura Retangulo
	ret := Retangulo{comprimento: 200, largura: 300}
	fmt.Printf("Area do retangulo: %.2f\n", ret.calcularArea())
	fmt.Printf("Perimetro do retangulo: %.2f\n", ret.calcularPerimetro())

}
