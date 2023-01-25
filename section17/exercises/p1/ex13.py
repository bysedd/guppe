class Moto:
    center: int = 50

    def __init__(self, marca: str, modelo: str, cor: str, marcha: int, maior_marcha: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha
        self.menor_marcha: int = 0
        self.maior_marcha = maior_marcha

    def marcha_acima(self) -> None:
        if self.marcha < self.maior_marcha:
            self.marcha += 1
            print(f'Marcha {self.marcha} atingida'.center(Moto.center))
        else:
            print('Marcha máxima atingida'.center(Moto.center))
        print('-' * Moto.center)

    def marcha_abaixo(self) -> None:
        if self.marcha > self.menor_marcha:
            self.marcha -= 1
            print(f'Marcha {self.marcha} atingida'.center(Moto.center))
        else:
            print('Marcha mínima atingida'.center(Moto.center))
        print('-' * Moto.center)

    def imprimir(self) -> None:
        marcha: str = ''
        match self.marcha:
            case 0:
                marcha = 'Neutro'
            case 1:
                marcha = 'Primeira'
            case 2:
                marcha = 'Segunda'
            case 3:
                marcha = 'Terceira'
            case 4:
                marcha = 'Quarta'
            case 5:
                marcha = 'Quinta'
            case 6:
                marcha = 'Sexta'

        print(f'Marca: {self.marca}'.center(Moto.center))
        print(f'Modelo: {self.modelo}'.center(Moto.center))
        print(f'Cor: {self.cor}'.center(Moto.center))
        print(f'Marcha: {marcha}'.center(Moto.center))
        print('-' * Moto.center)


if __name__ == '__main__':
    moto = Moto('Honda', 'CG 125', 'Vermelha', 0, 6)
    moto.imprimir()
    moto.marcha_acima()
    moto.marcha_acima()
    moto.marcha_acima()
    moto.marcha_acima()
    moto.marcha_abaixo()
    moto.imprimir()
