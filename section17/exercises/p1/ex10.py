class Moto:
    def __init__(self, marca: str, modelo: str, cor: str, marcha: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        match marcha:
            case 0:
                self.marcha = 'Neutro'
            case 1:
                self.marcha = 'Primeira'
            case 2:
                self.marcha = 'Segunda'
            case 3:
                self.marcha = 'Terceira'
            case 4:
                self.marcha = 'Quarta'
            case 5:
                self.marcha = 'Quinta'
            case 6:
                self.marcha = 'Sexta'
            case _:
                self.marcha = 'Marcha inválida'

    def imprimir(self) -> None:
        print(f'Marca: {self.marca}'.center(50))
        print(f'Modelo: {self.modelo}'.center(50))
        print(f'Cor: {self.cor}'.center(50))
        print(f'Marcha: {self.marcha}'.center(50))
        print('-' * 50)


if __name__ == '__main__':
    moto = Moto('Honda', 'CG 125', 'Vermelha', 3)
    moto.imprimir()
