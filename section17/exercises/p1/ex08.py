class Circulo:
    def __init__(self, raio: float) -> None:
        self.raio = raio
        self.area = 3.14 * self.raio ** 2
        self.perimetro = 2 * 3.14 * self.raio

    def __str__(self) -> str:
        return f"Raio: {self.raio} | Área: {self.area} | Perímetro: {self.perimetro}"


if __name__ == '__main__':
    try:
        circulo = Circulo(float(input('Digite o raio: ')))
    except ValueError as err:
        print(err)
    else:
        print(circulo)
