class Televisor:
    def __init__(self, ligado: bool, canal: int, volume: int) -> None:
        self.__ligado = ligado
        self.canal = canal
        self.volume = volume

    def ligar(self) -> None:
        self.__ligado = True

    def desligar(self) -> None:
        self.__ligado = False

    def imprimir(self) -> None:
        print(f'Televisor está ligado? {self.__ligado}')
        print(f'Televisor está no canal: {self.canal}')
        print(f'Televisor está no volume: {self.volume}')


if __name__ == '__main__':
    tv = Televisor(False, 157, 69)
    tv.imprimir()
    tv.ligar()
    tv.imprimir()
