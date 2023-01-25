class Microondas:
    def __init__(self, ligado: bool, porta_fechada: bool) -> None:
        self.__ligado = ligado
        self.__porta_fechada = porta_fechada

    def ligar(self) -> None:
        self.__ligado = True

    def desligar(self) -> None:
        self.__ligado = False

    def imprimir(self) -> None:
        print(f"Microondas ligado? {self.__ligado}")
        print(f"Porta fechada? {self.__porta_fechada}\n")


if __name__ == '__main__':
    microondas = Microondas(False, True)
    microondas.imprimir()

    microondas.ligar()
    microondas.imprimir()

    microondas.desligar()
    microondas.imprimir()
