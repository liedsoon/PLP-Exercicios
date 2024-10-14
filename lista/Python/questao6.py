"""
Implemente uma classe Motor e associe-a a uma classe Carro. A classe
Carro deve ter um objeto do tipo Motor como um de seus atributos.
"""
class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def exibir_detalhes(self):
        print(f"Tipo do Motor: {self.tipo}")
        print(f"Potência do Motor: {self.potencia}")

class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        self.motor.exibir_detalhes()
def main():
    motorV8 = Motor("V8", "400 HP")
    carro = Carro("Ford", "Mustang", motorV8)

    carro.exibir_detalhes()

if __name__ == "__main__":
    main()
