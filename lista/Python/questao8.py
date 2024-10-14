"""
Modele uma classe Empresa que agregue uma lista de objetos Empregado.
Cada empregado deve ter atributos como nome, cargo, e salario.
"""
class Empregado:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir_detalhes(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}")


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.empregados = []

    def adicionar_empregado(self, empregado):
        if empregado not in self.empregados:
            self.empregados.append(empregado)

    def exibir_empregados(self):
        print(f"Empregados da empresa {self.nome}:")
        for empregado in self.empregados:
            empregado.exibir_detalhes()

def main():
    empresa = Empresa("Serasa Experian")

    empregado1 = Empregado("Maria", "Desenvolvedora", 8000)
    empregado2 = Empregado("Bruno", "Analista", 5000)
    empregado3 = Empregado("Carlos", "Gerente", 15000)

    empresa.adicionar_empregado(empregado1)
    empresa.adicionar_empregado(empregado2)
    empresa.adicionar_empregado(empregado3)

    empresa.exibir_empregados()

if __name__ == "__main__":
    main()
