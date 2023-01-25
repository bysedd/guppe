class Moto:
    center: int = 50
    menor_marcha: int = 0
    maior_marcha: int = 6
    marcha: int = 0
    marca: str = ''
    modelo: str = ''
    cor: str = ''

    @classmethod
    def marcha_acima(cls) -> None:
        if cls.marcha < Moto.maior_marcha:
            cls.marcha += 1
            print(f'Marcha {cls.marcha} atingida'.center(Moto.center))
        else:
            print('Marcha máxima atingida'.center(Moto.center))
        print('-' * Moto.center)

    @classmethod
    def marcha_abaixo(cls) -> None:
        if cls.marcha > Moto.menor_marcha:
            cls.marcha -= 1
            print(f'Marcha {cls.marcha} atingida'.center(Moto.center))
        else:
            print('Marcha mínima atingida'.center(Moto.center))
        print('-' * Moto.center)

    @classmethod
    def imprimir(cls) -> None:
        marcha: str = ''
        match cls.marcha:
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

        print(f'Marca: {cls.marca}'.center(Moto.center))
        print(f'Modelo: {cls.modelo}'.center(Moto.center))
        print(f'Cor: {cls.cor}'.center(Moto.center))
        print(f'Marcha: {marcha}'.center(Moto.center))
        print('-' * Moto.center)


if __name__ == '__main__':
    # Instanciando
    moto = Moto()
    moto.marca = 'Honda'
    moto.modelo = 'CG 125'
    moto.cor = 'Vermelha'
    moto.marcha = 3

    # Testes
    moto.imprimir()
    moto.marcha_acima()
    moto.imprimir()
    moto.marcha_acima()
    moto.imprimir()
    moto.marcha_acima()
    moto.imprimir()
    moto.marcha_acima()
    moto.imprimir()
    moto.marcha_acima()
    moto.imprimir()
    moto.marcha_acima()
    moto.imprimir()
