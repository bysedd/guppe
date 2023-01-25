class Microondas:
    def __init__(self, ligado: bool) -> None:
        self.ligado = ligado

    def imprimir(self) -> None:
        print(f"Microondas ligado? {self.ligado}\n")


if __name__ == '__main__':
    microondas = Microondas(False)
    microondas.imprimir()
    microondas.ligado = True
    microondas.imprimir()
