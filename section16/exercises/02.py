class Agenda:
    def __init__(self):
        self.__pessoas = []  # lista vazia para armazenar as pessoas

    @property
    def pessoas(self):
        return self.__pessoas

    def armazena_pessoa(self, nome: str, idade: int, altura: float) -> None:
        nome = nome.strip().title()
        pessoa = {"nome": nome, "idade": idade, "altura": altura}
        self.pessoas.append(pessoa)  # adiciona a pessoa na lista
        print(f"{nome} foi adicionado com sucesso!")

    def remove_pessoa(self, nome: str) -> None:
        nome = nome.strip().title()
        pessoa = self._busca_pessoa(nome)
        if pessoa:
            self.pessoas.remove(pessoa)
            print(f"{nome} foi removido com sucesso!")
        else:
            print(f"{nome} não está na agenda.")

    def busca_pessoa(self, nome: str):
        nome = nome.strip().title()
        pessoa = self._busca_pessoa(nome)
        if pessoa:
            print(f"{nome} está na posição {self.pessoas.index(pessoa)} da agenda.")
        else:
            print(f"{nome} não está na agenda.")

    def _busca_pessoa(self, nome: str) -> dict:
        nome = nome.strip().title()
        for pessoa in self.pessoas:
            if pessoa["nome"] == nome:
                return pessoa  # retorna a pessoa encontrada

    def imprime_agenda(self) -> None:
        if self.pessoas:
            for pessoa in self.pessoas:
                print(str(pessoa).center(60))
        else:
            print("Não há pessoas na agenda.")

    def imprime_pessoa(self, index: int) -> None:
        if 0 <= index < len(self.pessoas):
            print(self.pessoas[index])
        else:
            print("Index inválido.")


if __name__ == '__main__':
    agenda = Agenda()

    try:
        while True:
            opcao = int(input("1 - Adicionar pessoa\n"
                              "2 - Remover pessoa\n"
                              "3 - Buscar pessoa\n"
                              "4 - Imprimir agenda\n"
                              "5 - Imprimir pessoa\n"
                              "6 - Sair\n"
                              "Opção: "))
            print("-" * 60)

            match opcao:
                case 1:
                    nome_pessoa = input("Nome: ")
                    idade_pessoa = int(input("Idade: "))
                    altura_pessoa = float(input("Altura: "))
                    agenda.armazena_pessoa(nome_pessoa, idade_pessoa, altura_pessoa)
                case 2:
                    nome_pessoa = input("Nome: ")
                    agenda.remove_pessoa(nome_pessoa)
                case 3:
                    nome_pessoa = input("Nome: ")
                    agenda.busca_pessoa(nome_pessoa)
                case 4:
                    agenda.imprime_agenda()
                case 5:
                    index_pessoa = int(input("Index: "))
                    agenda.imprime_pessoa(index_pessoa)
                case 6:
                    break
                case _:
                    print("Opção inválida.")

            print("-" * 60)
    except ValueError:
        print("Valor inválido.")
    else:
        print("Fim do programa.")
