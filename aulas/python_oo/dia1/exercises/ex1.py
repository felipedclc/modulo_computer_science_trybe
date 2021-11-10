class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcula_perimetro(self):
        return 4 * self.lado

    def calcula_area(self):
        return self.lado * self.lado


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcula_perimetro(self):
        return (self.base + self.altura) * 2

    def calcula_area(self):
        return self.base * self.altura


# testando (apenas esse arquivo irá reconhecer)
if __name__ == "__main__":
    retangulo1 = Retangulo(10, 5)
    print(f"Area retangulo1 = {retangulo1.calcula_area()}")
