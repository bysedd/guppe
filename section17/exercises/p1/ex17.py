class Eletrodomestico:
    ligado: bool = False

    @classmethod
    def imprimir(cls):
        print(f'Eletrodoméstico está ligado? {cls.ligado}')


if __name__ == '__main__':
    eletro = Eletrodomestico()
    eletro.imprimir()
