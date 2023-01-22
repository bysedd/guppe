class Retangulo:
    comprimento: float
    largura: float
    area: float
    perimetro: float

    @classmethod
    def calcular_area(cls, comprimento, largura):
        return comprimento * largura

    @classmethod
    def calcular_perimetro(cls, comprimento, largura):
        return 2 * (comprimento + largura)

    def __str__(self):
        return f"Comprimento: {self.comprimento} | Largura: {self.largura} | " \
               f"Área: {self.area} | Perímetro: {self.perimetro}"


if __name__ == '__main__':
    retangulo = Retangulo()
    try:
        retangulo.comprimento = float(input('Digite o comprimento: '))
        retangulo.largura = float(input('Digite a largura: '))
        retangulo.area = Retangulo.calcular_area(retangulo.comprimento, retangulo.largura)
        retangulo.perimetro = Retangulo.calcular_perimetro(retangulo.comprimento, retangulo.largura)
    except ValueError as err:
        print(err)
    else:
        print(retangulo)
