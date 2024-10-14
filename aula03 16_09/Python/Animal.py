class Animal:
    def __init__(self, especie, nome):
        self.especie = especie
        self.nome = nome
    def emitir_som(self):
        pass #Método a ser implementado nas subclasses

class Cachorro(Animal):
    def emitir_som(self):
        return 'Au au'

class Gato(Animal):
    def emitir_som(self):
        return 'Miau'

if __name__ == '__main__':

    cachorro = Cachorro('Cachorro', 'Rex')
    gato = Gato('Gato', 'Michonne')
    print(cachorro.emitir_som())
    print(gato.emitir_som())
