"""
Crie uma classe de exceção personalizada SaldoInsuficienteException em Java e Python,
que seja lançada quando houver uma tentativa de saque superior ao saldo disponível na classe
ContaBancaria.
"""
class SaldoInsuficienteException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depositado: R${valor:.2f}. \nSaldo atual: R${self._saldo:.2f}.\n")
        else:
            print("Valor de depósito inválido.\n")

    def sacar(self, valor):
        if valor > self._saldo:
            raise SaldoInsuficienteException("Saldo insuficiente para realizar o saque.\n")
        elif valor <= 0:
            print("Valor de saque inválido.\n")
        else:
            self._saldo -= valor
            print(f"Sacado: R${valor:.2f}.\nSaldo atual: R${self._saldo:.2f}.\n")

def main():
    conta = ContaBancaria("João", 1000)

    print(f"Saldo inicial: R${conta.get_saldo():.2f}\n")

    try:
        conta.depositar(500)
        conta.sacar(300)
        conta.sacar(1500)
    except SaldoInsuficienteException as e:
        print(e)

if __name__ == "__main__":
    main()
