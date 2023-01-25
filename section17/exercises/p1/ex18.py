class Eletrodomestico:
    def __init__(self, ligado: bool):
        self.ligado = ligado

    def imprimir(self):
        print(f'Eletrodoméstico está ligado? {self.ligado}')


if __name__ == '__main__':
    eletro = Eletrodomestico(ligado=False)
    eletro.imprimir()
    eletro.ligado = True
    eletro.imprimir()
