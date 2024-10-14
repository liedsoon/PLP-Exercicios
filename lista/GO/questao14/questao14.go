package main

import (
	"fmt"
	"sync"
)

type Configuracao struct {
	Valor string
}

var instance *Configuracao
var once sync.Once

// Função que retorna a instância Singleton
func GetInstance() *Configuracao {
	once.Do(func() {
		instance = &Configuracao{}
		fmt.Println("Configuração Padrão")
	})
	return instance
}

// Exemplo de uso
func main() {
	config := GetInstance()
	config2 := GetInstance()

	fmt.Println(config == config2)
	fmt.Println("Valor da Configuração: ", config.Valor)
	config.Valor = "Nova Configuração"
	fmt.Println("Valor da Configuração após alteração:", config2.Valor)
}
