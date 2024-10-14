"""
Em Python, sobrecarregue o operador + para somar dois objetos Produto
baseados no preço.
"""
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __add__(self, other):
        if isinstance(other, Produto):
            return Produto(f"{self.nome} e {other.nome}", self.preco + other.preco)
        return NotImplemented

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}"

def main():
    produto1 = Produto("Livro", 25.90)
    produto2 = Produto("Caderno", 40.90)

    produto3 = produto1 + produto2

    print(produto1)
    print(produto2)
    print(produto3)

if __name__ == "__main__":
    main()
