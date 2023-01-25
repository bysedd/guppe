class Moto:
    center: int = 50
    marca: str = 'Honda'
    modelo: str = 'CG 125'
    cor: str = 'Vermelha'
    marcha: int = 0
    menor_marcha: int = 0
    maior_marcha: int = 6
    ligada: bool = True
    marchas: dict[int, str] = {
        0: 'Neutro',
        1: 'Primeira',
        2: 'Segunda',
        3: 'Terceira',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta'
    }

    @classmethod
    def marcha_acima(cls) -> None:
        if cls.marcha < cls.maior_marcha:
            cls.marcha += 1
            print(f'Marcha {cls.marcha} atingida'.center(Moto.center))
        else:
            print('Marcha máxima atingida'.center(Moto.center))
        print('-' * Moto.center)

    @classmethod
    def marcha_abaixo(cls) -> None:
        if cls.marcha > cls.menor_marcha:
            cls.marcha -= 1
            print(f'Marcha {cls.marcha} atingida'.center(Moto.center))
        else:
            print('Marcha mínima atingida'.center(Moto.center))
        print('-' * Moto.center)

    @classmethod
    def imprimir(cls) -> None:
        print(f'Marca: {cls.marca}'.center(Moto.center))
        print(f'Modelo: {cls.modelo}'.center(Moto.center))
        print(f'Cor: {cls.cor}'.center(Moto.center))
        print(f'Marcha: {cls.marchas[cls.marcha]}'.center(Moto.center))
        print(f'Ligada: {cls.ligada}'.center(Moto.center))
        print('-' * Moto.center)


if __name__ == '__main__':
    # Instanciando
    moto = Moto()

    # Imprimindo
    moto.imprimir()
