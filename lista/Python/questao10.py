"""
Métodos com Nomes Diferentes (Python, Go)
Implemente uma classe Calculadora com métodos somar que aceita diferentes números
de parâmetros (dois ou três números). Em Golang, use funções com nomes diferentes
para diferentes quantidades de parâmetros.
"""
class Calculadora:
    def somar_dois(self, a, b):
        return a + b

    def somar_tres(self, a, b, c):
        return a + b + c

def main():
    calc = Calculadora()

    resultado1 = calc.somar_dois(10, 10)
    print(f"Soma de 10 + 10: {resultado1}")

    resultado2 = calc.somar_tres(10, 10, 10)
    print(f"Soma de 10 + 10 + 10: {resultado2}")

if __name__ == "__main__":
    main()
