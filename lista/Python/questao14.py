"""
Implemente o padrão de projeto Singleton para garantir que apenas uma
instância de uma classe Configuracao seja criada.
"""
class Configuracao:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Configuracao, cls).__new__(cls)
            cls._instancia.parametro = "Padrão"
        return cls._instancia

    def get_parametro(self):
        return self.parametro

    def set_parametro(self, parametro):
        self.parametro = parametro

if __name__ == "__main__":
    configuracao1 = Configuracao()
    configuracao2 = Configuracao()

    print(configuracao1 is configuracao2)  # Saída: True

    print(configuracao1.get_parametro())  # Saída: "Padrão"
    configuracao1.set_parametro("Novo Valor")
    print(configuracao2.get_parametro())  # Saída: "Novo Valor"
