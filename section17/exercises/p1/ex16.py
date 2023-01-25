class Moto:
    center: int = 50

    def __init__(self, marca: str, modelo: str, cor: str, marcha: int, maior_marcha: int, ligada: bool) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha
        self.menor_marcha: int = 0
        self.maior_marcha = maior_marcha
        self.ligada = ligada
        self.marchas: dict[int, str] = {
            0: 'Neutro',
            1: 'Primeira',
            2: 'Segunda',
            3: 'Terceira',
            4: 'Quarta',
            5: 'Quinta',
            6: 'Sexta'
        }

    def ligar(self) -> None:
        if self.ligada:
            print('Moto já está ligada'.center(Moto.center))
            print('-' * Moto.center)
        else:
            self.ligada = True
            print('Moto ligada'.center(Moto.center))
            print('-' * Moto.center)

    def desligar(self) -> None:
        self.ligada = False
        print('Moto desligada'.center(Moto.center))
        print('-' * Moto.center)

    def marcha_acima(self) -> None:
        if self.ligada:
            if self.marcha < self.maior_marcha:
                self.marcha += 1
                print(f'Marcha {self.marcha} atingida'.center(Moto.center))
            else:
                print('Marcha máxima atingida'.center(Moto.center))
            print('-' * Moto.center)
        else:
            print('Moto desligada'.center(Moto.center))
            print('-' * Moto.center)

    def marcha_abaixo(self) -> None:
        if self.ligada:
            if self.marcha > self.menor_marcha:
                self.marcha -= 1
                print(f'Marcha {self.marcha} atingida'.center(Moto.center))
            else:
                print('Marcha mínima atingida'.center(Moto.center))
            print('-' * Moto.center)
        else:
            print('Moto desligada'.center(Moto.center))
            print('-' * Moto.center)

    def imprimir(self) -> None:
        print(f'Marca: {self.marca}'.center(Moto.center))
        print(f'Modelo: {self.modelo}'.center(Moto.center))
        print(f'Cor: {self.cor}'.center(Moto.center))
        print(f'Marcha: {self.marchas[self.marcha]}'.center(Moto.center))
        print(f'Ligada: {self.ligada}'.center(Moto.center))
        print('-' * Moto.center)


if __name__ == '__main__':
    # Instanciando e imprimindo
    moto = Moto('Honda', 'CG 125', 'Vermelha', 0, 6, False)
    moto.imprimir()

    # Ligando
    moto.ligar()

    # Testando
    moto.marcha_acima()
    moto.marcha_acima()
    moto.marcha_acima()
    moto.marcha_acima()
    moto.marcha_abaixo()
    moto.imprimir()
