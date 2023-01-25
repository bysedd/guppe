class Televisor:
    def __init__(self, ligado: bool, canal: int, volume: int):
        self.ligado = ligado
        self.canal = canal
        self.volume = volume

    def imprimir(self):
        print(f'Televisor está ligado? {self.ligado}')
        print(f'Televisor está no canal: {self.canal}')
        print(f'Televisor está no volume: {self.volume}')


if __name__ == '__main__':
    tv = Televisor(True, 157, 69)
    tv.imprimir()
