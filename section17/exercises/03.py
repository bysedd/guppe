class Quadrado:
    lado: int = 4
    area: int = 0
    perimetro: int = 0

    def calcular_area(self) -> None:
        self.area = self.lado * self.lado

    def calcular_perimetro(self) -> None:
        self.perimetro = self.lado * 4

    def imprimir(self) -> None:
        print(f'Lado: {self.lado}')
        print(f'Área: {self.area}')
        print(f'Perímetro: {self.perimetro}')


quadrado = Quadrado()
quadrado.calcular_area()
quadrado.calcular_perimetro()
quadrado.imprimir()
