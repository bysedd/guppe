class Quadrado:
    def __init__(self, lado: int) -> None:
        self.lado = lado
        self.area = 0
        self.perimetro = 0

    def calcular_area(self) -> None:
        self.area = self.lado * self.lado

    def calcular_perimetro(self) -> None:
        self.perimetro = self.lado * 4

    def imprimir(self) -> None:
        print(f'Lado: {self.lado}')
        print(f'Área: {self.area}')
        print(f'Perímetro: {self.perimetro}')


quadrado = Quadrado(4)
quadrado.calcular_area()
quadrado.calcular_perimetro()
quadrado.imprimir()
