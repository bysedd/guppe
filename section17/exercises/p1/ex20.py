class Televisor:
    ligado: bool = True
    canal: int = 157
    volume: int = 69

    @classmethod
    def imprimir(cls):
        print(f'Televisor está ligado? {cls.ligado}')
        print(f'Televisor está no canal: {cls.canal}')
        print(f'Televisor está no volume: {cls.volume}')


if __name__ == '__main__':
    tv = Televisor()
    tv.imprimir()
