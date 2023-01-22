class Retangulo:
    def __init__(self, comprimento: float, largura: float) -> None:
        self.comprimento = comprimento
        self.largura = largura
        self.area = self.calcular_area()
        self.perimetro = self.calcular_perimetro()

    def calcular_area(self) -> float:
        return self.comprimento * self.largura

    def calcular_perimetro(self) -> float:
        return 2 * (self.comprimento + self.largura)

    def __str__(self) -> str:
        return f"Comprimento: {self.comprimento} | Largura: {self.largura} | " \
               f"Área: {self.area} | Perímetro: {self.perimetro}"


if __name__ == '__main__':
    try:
        comprimento_ret = float(input('Digite o comprimento: '))
        largura_ret = float(input('Digite a largura: '))
        retangulo = Retangulo(comprimento_ret, largura_ret)
    except ValueError as err:
        print(err)
    else:
        print(retangulo)
