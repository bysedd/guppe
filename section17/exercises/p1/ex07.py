class Circulo:
    raio: float
    area: float
    perimetro: float

    @classmethod
    def calcular_area(cls) -> None:
        cls.area = 3.14 * cls.raio ** 2

    @classmethod
    def calcular_perimetro(cls) -> None:
        cls.perimetro = 2 * 3.14 * cls.raio

    @classmethod
    def __str__(cls) -> str:
        return f"Raio: {cls.raio} | Área: {cls.area} | Perímetro: {cls.perimetro}"


if __name__ == '__main__':
    try:
        raio_circ = float(input('Digite o raio: '))
        Circulo.raio = raio_circ
        Circulo.calcular_area()
        Circulo.calcular_perimetro()
    except ValueError as err:
        print(err)
    else:
        print(circulo := Circulo())
