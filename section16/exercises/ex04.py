from random import randint


class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = randint(0, 100)

    def __str__(self) -> str:
        return f'Canal: {self.canal} - Volume: {self.volume} - Ligada: {self.ligada}'


class ControleRemoto:
    def __init__(self, televisao: Televisao) -> None:
        self.televisao = televisao

    def power(self) -> None:
        self.televisao.ligada = not self.televisao.ligada

    def aumenta_volume(self) -> None:
        if self.televisao.volume < 100:
            self.televisao.volume += 1
        else:
            print("Volume máximo.")

    def diminui_volume(self) -> None:
        if self.televisao.volume > 0:
            self.televisao.volume -= 1
        else:
            print("Volume mínimo.")

    def aumenta_canal(self) -> None:
        self.televisao.canal += 1

    def diminui_canal(self) -> None:
        if self.televisao.canal > 1:
            self.televisao.canal -= 1
        else:
            print("Canal inválido.")

    def muda_canal(self, canal: int) -> None:
        if canal > 0:
            self.televisao.canal = canal
        else:
            print("Canal inválido.")


if __name__ == '__main__':
    tv = Televisao()
    controle = ControleRemoto(tv)

    while True:
        try:
            opcao = int(input("1 - Power\n"
                              "2 - Aumenta volume\n"
                              "3 - Diminui volume\n"
                              "4 - Aumenta canal\n"
                              "5 - Diminui canal\n"
                              "6 - Muda canal\n"
                              "7 - Consultar\n"
                              "8 - Sair\n"
                              "Opção: "))
            print("-" * 60)

            match opcao:
                case 1:
                    controle.power()
                case 2:
                    controle.aumenta_volume()
                case 3:
                    controle.diminui_volume()
                case 4:
                    controle.aumenta_canal()
                case 5:
                    controle.diminui_canal()
                case 6:
                    while True:
                        try:
                            canal_tv = int(input("Canal: "))
                            controle.muda_canal(canal_tv)
                            break
                        except ValueError:
                            print("Canal inválido.")
                case 7:
                    print(tv)
                    print("-" * 60)
                case 8:
                    break
                case _:
                    print("Opção inválida.")
        except ValueError:
            print("Opção inválida.")
    print("Fim do programa.")
