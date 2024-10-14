"""
 Implemente uma classe ContaBancaria com atributos saldo, titular e
métodos depositar e sacar. Use encapsulamento para proteger o atributo saldo.
"""
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            print(f"Depositando R${valor:.2f}")
            self._saldo += valor
        else:
            print("Valor de depósito inválido")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            print(f"Sacando R${valor:.2f}")
            self._saldo -= valor
        else:
            print("Saldo insuficiente ou valor de saque inválido")

    def exibir_informacoes(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.get_saldo():.2f}")

def main():
    conta = ContaBancaria("Maria", 2000)
    conta.exibir_informacoes()

    conta.sacar(150)
    conta.exibir_informacoes()

    conta.sacar(2000)

if __name__ == "__main__":
    main()
