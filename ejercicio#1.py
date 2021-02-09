class Triangulo:
    base = 0
    altura = 0

    def calcular_area(self):
        return (self.base * self.altura) / 2


figura = Triangulo()

figura.base = float(input("Base: "))
figura.altura = float(input("Altura: "))

print ("El area es: ", figura.calcular_area())
