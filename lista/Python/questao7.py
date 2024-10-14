"""
Crie uma classe Escola e uma classe Professor. A associação deve permitir
que uma escola tenha vários professores, e um professor possa lecionar em várias escolas.
"""
class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.escolas = []

    def adicionar_escola(self, escola):
        if escola not in self.escolas:
            self.escolas.append(escola)
            escola.adicionar_professor(self)

    def exibir_escolas(self):
        print(f"Professor {self.nome} ensina nas seguintes escolas:")
        for escola in self.escolas:
            print(f"° {escola.nome}")

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []
    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)
            professor.adicionar_escola(self)

    def exibir_professores(self):
        print(f"A escola {self.nome} tem os seguintes professores:")
        for professor in self.professores:
            print(f"° {professor.nome}")

def main():
    escola1 = Escola("Maria Caxias")
    escola2 = Escola("João da Silva")

    professor1 = Professor("João")
    professor2 = Professor("Maria")
    professor3 = Professor("José")

    escola1.adicionar_professor(professor1)
    escola1.adicionar_professor(professor2)
    escola1.adicionar_professor(professor3)
    escola2.adicionar_professor(professor1)
    escola2.adicionar_professor(professor3)


    professor1.exibir_escolas()
    professor2.exibir_escolas()
    professor3.exibir_escolas()

    escola1.exibir_professores()
    escola2.exibir_professores()

if __name__ == "__main__":
    main()
