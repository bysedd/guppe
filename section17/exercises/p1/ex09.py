class Moto:
    marca: str
    modelo: str
    cor: str
    marcha: int

    @classmethod
    def imprimir(cls) -> None:
        if not cls.marca:
            print('Nenhuma moto cadastrada.')
        else:
            print(f"Marca: {cls.marca} | Modelo: {cls.modelo} | Cor: {cls.cor} | Marcha: ", end="")
            match cls.marcha:
                case 0:
                    print("Neutro")
                case 1:
                    print("Primeira")
                case 2:
                    print("Segunda")
                case 3:
                    print("Terceira")
                case 4:
                    print("Quarta")
                case 5:
                    print("Quinta")
                case 6:
                    print("Sexta")
                case _:
                    print('Marcha inválida.')


if __name__ == '__main__':
    Moto.marca = 'Honda'
    Moto.modelo = 'CG 150'
    Moto.cor = 'Vermelha'
    Moto.marcha = 3
    Moto.imprimir()
    Moto.marcha = 7
    Moto.imprimir()
    Moto.marcha = 0
    Moto.cor = 'Azul'
    Moto.imprimir()
