class Elevador:
    def __init__(self, capacidade: int, total_andares: int) -> None:
        self.__capacidade = capacidade
        self.__total_andares = total_andares
        self.__andar_atual = 0
        self.__pessoas = 0

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int) -> None:
        self.__capacidade = capacidade

    @property
    def total_andares(self) -> int:
        return self.__total_andares

    @total_andares.setter
    def total_andares(self, total_andares: int) -> None:
        self.__total_andares = total_andares

    @property
    def andar_atual(self) -> int:
        return self.__andar_atual

    @andar_atual.setter
    def andar_atual(self, andar_atual: int) -> None:
        self.__andar_atual = andar_atual

    @property
    def pessoas(self) -> int:
        return self.__pessoas

    @pessoas.setter
    def pessoas(self, pessoas: int) -> None:
        self.__pessoas = pessoas

    def entra(self, pessoas: int) -> None:
        if self.pessoas + pessoas <= self.capacidade:
            self.pessoas += pessoas
            print(f"{pessoas} pessoa(s) entrou(ram) no elevador.")
        elif self.pessoas + pessoas > self.capacidade:
            print(f"Só cabem mais {self.capacidade - self.pessoas} pessoa(s) no elevador.")
        else:
            print("O elevador está cheio.")

    def sai(self, pessoas: int) -> None:
        if self.pessoas - pessoas >= 0:
            self.pessoas -= pessoas
            print(f"{pessoas} pessoa(s) saiu(ram) do elevador.")
        elif self.pessoas - pessoas < 0:
            print(f"Só tem {self.pessoas} pessoa(s) no elevador.")
        else:
            print("O elevador está vazio.")

    def sobe(self, andares: int) -> None:
        if self.andar_atual + andares <= self.total_andares:
            self.andar_atual += andares
            print(f"O elevador subiu {andares} andar(es).")
        else:
            print("O elevador já está no último andar.")

    def desce(self, andares: int) -> None:
        if self.andar_atual - andares >= 0:
            self.andar_atual -= andares
            print(f"O elevador desceu {andares} andar(es).")
        else:
            print("O elevador já está no térreo.")

    def __str__(self) -> str:
        print("-" * 60)
        if self.andar_atual == 0:
            return f"O elevador está no térreo com {self.pessoas} pessoa(s) dentro.".center(60)
        return f"O elevador está no {elevador.andar_atual}º andar com {elevador.pessoas} pessoa(s) dentro.".center(60)


if __name__ == "__main__":
    while True:
        try:
            capacidade_elevador = int(input("Capacidade do elevador: "))
            total_andares_elevador = int(input("Total de andares: "))
            break
        except ValueError:
            print("Valor inválido.")

    elevador = Elevador(capacidade_elevador, total_andares_elevador)
    while True:
        print("-" * 60)
        opcao = input("1 - Entrar\n2 - Sair\n3 - Subir\n4 - Descer\n5 - Sair\n"
                      "Opção: ")
        match opcao:
            case "1":
                while True:
                    try:
                        pessoas_elevador = int(input("Quantas pessoas vão entrar: "))
                        break
                    except ValueError:
                        print("Valor inválido.")
                elevador.entra(pessoas_elevador)
            case "2":
                while True:
                    try:
                        pessoas_elevador = int(input("Quantas pessoas vão sair: "))
                        break
                    except ValueError:
                        print("Valor inválido.")
                elevador.sai(pessoas_elevador)
            case "3":
                while True:
                    try:
                        andares_elevador = int(input("Quantos andares vão subir: "))
                        break
                    except ValueError:
                        print("Valor inválido.")
                elevador.sobe(andares_elevador)
            case "4":
                while True:
                    try:
                        andares_elevador = int(input("Quantos andares vão descer: "))
                        break
                    except ValueError:
                        print("Valor inválido.")
                elevador.desce(andares_elevador)
            case "5":
                break
            case _:
                print("Opção inválida.")
        print(elevador)
    print("Fim do programa.")
