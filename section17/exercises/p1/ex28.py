class Microondas:
    def __init__(self, ligado: bool) -> None:
        self.__ligado = ligado

    def ligar(self) -> None:
        self.__ligado = True

    def desligar(self) -> None:
        self.__ligado = False

    def imprimir(self) -> None:
        print(f"Microondas ligado? {self.__ligado}\n")


if __name__ == '__main__':
    microondas = Microondas(False)
    microondas.imprimir()

    microondas.ligar()
    microondas.imprimir()

    microondas.desligar()
    microondas.imprimir()
