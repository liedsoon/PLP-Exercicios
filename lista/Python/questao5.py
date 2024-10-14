"""
Utilize polimorfismo para criar uma função que receba uma lista de
objetos Animal e chame o método som de cada um, demonstrando comportamento
diferente para cada subclasse
"""
class Animal:
    def __init__(self, especie, nome):
        self.especie = especie
        self.nome = nome

    def emitir_som(self):
        return ""

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__("Cachorro", nome)

    def emitir_som(self):
        return "O cachorro faz Au au"

class Gato(Animal):
    def __init__(self, nome):
        super().__init__("Gato", nome)

    def emitir_som(self):
        return "O gato faz Miau"

class Galinha(Animal):
    def __init__(self, nome):
        super().__init__("Galinha", nome)

    def emitir_som(self):
        return "A galinha faz Có có"

def emitir_som_animais(animais):
    for animal in animais:
        print(animal.emitir_som())

def main():
    animais = []

    cachorro = Cachorro("Rex")
    gato = Gato("Michonne")
    galinha = Galinha("Rafinha")

    animais.append(cachorro)
    animais.append(gato)
    animais.append(galinha)

    emitir_som_animais(animais)

if __name__ == "__main__":
    main()
