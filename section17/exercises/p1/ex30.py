class Microondas:
    def __init__(self, ligado: bool, porta_fechada: bool) -> None:
        self.__ligado = ligado
        self.__porta_fechada = porta_fechada

    def ligar(self) -> None:
        self.__ligado = True

    def desligar(self) -> None:
        self.__ligado = False

    def abrir_porta(self) -> None:
        self.__porta_fechada = False

    def fechar_porta(self) -> None:
        self.__porta_fechada = True

    def imprimir(self) -> None:
        print(f"Microondas ligado? {self.__ligado}")
        print(f"Porta fechada? {self.__porta_fechada}\n")


if __name__ == '__main__':
    microondas = Microondas(True, True)
    microondas.imprimir()

    microondas.desligar()
    microondas.imprimir()

    microondas.abrir_porta()
    microondas.imprimir()
