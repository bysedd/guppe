class Eletrodomestico:
    def __init__(self, ligado: bool) -> None:
        self.__ligado = ligado

    @property
    def ligado(self) -> bool:
        return self.__ligado

    def ligar(self) -> None:
        self.__ligado = True

    def desligar(self) -> None:
        self.__ligado = False

    def imprimir(self) -> None:
        print(f'Eletrodoméstico está ligado? {self.__ligado}')


if __name__ == '__main__':
    eletro = Eletrodomestico(ligado=False)
    eletro.imprimir()
    eletro.ligar()
    eletro.imprimir()
