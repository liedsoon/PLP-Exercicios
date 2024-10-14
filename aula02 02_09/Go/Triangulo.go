package main

import (
    "fmt"
)

type Triangulo struct {
    lado1, lado2, lado3 float64
}

func (t Triangulo) Perimetro() float64 {
    return t.lado1 + t.lado2 + t.lado3
}

func (t Triangulo) Tipo() string {
    if t.lado1 == t.lado2 && t.lado2 == t.lado3 {
        return "Equilátero"
    } else if t.lado1 == t.lado2 || t.lado2 == t.lado3 || t.lado1 == t.lado3 {
        return "Isósceles"
    } else {
        return "Escaleno"
    }
}

func main() {
    triangulo := Triangulo{lado1: 3, lado2: 4, lado3: 5}
    fmt.Printf("Perímetro: %.2f\n", triangulo.Perimetro())
    fmt.Println("Tipo:", triangulo.Tipo())
}
