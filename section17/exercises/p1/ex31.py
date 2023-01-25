class Microondas:
    def __init__(self, ligado: bool, porta_fechada: bool) -> None:
        self.__ligado = ligado
        self.__porta_fechada = porta_fechada

    def ligar(self) -> None:
        if self.__porta_fechada:
            self.__ligado = True
        else:
            print("Porta aberta, não é possível ligar o microondas")

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
    microondas = Microondas(False, False)
    microondas.imprimir()

    microondas.ligar()
    microondas.imprimir()

    microondas.fechar_porta()
    microondas.imprimir()

    microondas.ligar()
    microondas.imprimir()
