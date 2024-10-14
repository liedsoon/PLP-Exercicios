"""
Em Java e Golang, defina uma interface para imprimível que
tenha um método imprimir. Implemente essa interface em classes como Relatório e
Contrato. Em Python, use a abordagem de protocolo ou classes abstratas
"""
from abc import ABC, abstractmethod
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass
class Relatorio(Imprimivel):
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def imprimir(self):
        print(f"Relatório: {self.titulo}")
        print(f"Conteúdo:\n{self.conteudo}")

class Contrato(Imprimivel):
    def __init__(self, titulo, termos):
        self.titulo = titulo
        self.termos = termos

    def imprimir(self):
        print("Contrato:")
        print(f"Titulo: {self.titulo}")
        print("Termos do Contrato:")
        print(self.termos)

def main():
    relatorio = Relatorio("Relatório Mensal", "Este é o conteúdo do relatório mensal.....")
    contrato = Contrato("Emprego", "Os termos do contrato são......")

    relatorio.imprimir()
    print("\n")
    contrato.imprimir()

if __name__ == "__main__":
    main()
