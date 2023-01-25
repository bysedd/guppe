class Microondas:
    ligado: bool = False

    @classmethod
    def imprimir(cls) -> None:
        print(f"Microondas ligado? {cls.ligado}\n")


if __name__ == '__main__':
    Microondas.imprimir()
    Microondas.ligado = True
    Microondas.imprimir()
