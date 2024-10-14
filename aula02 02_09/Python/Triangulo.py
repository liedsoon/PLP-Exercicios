# um triângulo nas linguagens Python, Java, e Go. Essas classes permitirão instanciar um objeto triângulo, 
# calcular o perímetro, e verificar se o triângulo é equilátero, isósceles ou escaleno.

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

# Instanciando um triângulo
triangulo = Triangulo(3, 4, 5)
print(f"Perímetro: {triangulo.perimetro()}")
print(f"Tipo: {triangulo.tipo()}")
