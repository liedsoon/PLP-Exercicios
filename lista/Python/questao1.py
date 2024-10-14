"""
1. Crie uma classe Carro com atributos como marca, modelo, e ano.
Instancie três objetos dessa classe e exiba os detalhes de cada um.
"""
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}")

def main():
    carro1 = Carro("Fiat", "Uno", 2020)
    carro2 = Carro("Chevrolet", "Onix", 2019)
    carro3 = Carro("Volkswagen,", "Gol", 2010)

    carro1.exibir_detalhes()
    carro2.exibir_detalhes()
    carro3.exibir_detalhes()

if __name__ == "__main__":
    main()
