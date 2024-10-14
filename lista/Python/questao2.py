"""
 Adicione um método acelerar e frear à classe Carro que altere um atributo
velocidade. Crie um método para exibir a velocidade atual.

"""
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, potencia):
        print("Acelerando...\n")
        self.velocidade += potencia

    def frear(self):
        print("Freando...\n")
        self.velocidade = self.velocidade // 2

    def exibir_carro(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print()

    def exibir_velocidade(self):
        print(f"Velocidade Atual: {self.velocidade}\n")

def novo_carro(marca, modelo, ano):
    return Carro(marca, modelo, ano)

def main():
    carro1 = novo_carro("Fiat", "Uno", 2020)

    carro1.exibir_carro()

    carro1.acelerar(10)
    carro1.exibir_velocidade()
    carro1.acelerar(30)
    carro1.exibir_velocidade()

    carro1.frear()
    carro1.frear()
    carro1.frear()
    carro1.exibir_velocidade()

if __name__ == "__main__":
    main()
