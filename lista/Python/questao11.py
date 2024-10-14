"""
Crie uma classe abstrata Funcionario com um método abstrato
calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
implementam calcularSalario de formas distintas.

"""
from abc import ABC, abstractmethod
class Funcionario(ABC):
    @abstractmethod
    def calcularSalario(self):
        pass
class FuncionarioHorista(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
    def calcularSalario(self):
        return self.horas_trabalhadas * self.valor_hora

class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome, salario_mensal):
        self.nome = nome
        self.salario_mensal = salario_mensal

    def calcularSalario(self):
        return self.salario_mensal

def main():
    funcionario1 = FuncionarioHorista("Carlos", 100, 35)
    print(f"Salário de {funcionario1.nome}(Funcionario Horista): R${funcionario1.calcularSalario():.2f}")

    funcionario2 = FuncionarioAssalariado("Maria", 3500)
    print(f"Salário de {funcionario2.nome} (Funcionario Assalariado): R${funcionario2.calcularSalario():.2f}")

if __name__ == "__main__":
    main()
