"""
Crie uma classe base Animal com métodos como som. Derive classes como
Cachorro e Gato que implementam o método som de maneiras diferentes.
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
        return "Au au"

class Gato(Animal):
    def __init__(self, nome):
        super().__init__("Gato", nome)

    def emitir_som(self):
        return "Miau"

def main():
    cachorro = Cachorro("Rex")
    gato = Gato("Michonne")

    print(cachorro.emitir_som())
    print(gato.emitir_som())

if __name__ == "__main__":
    main()
