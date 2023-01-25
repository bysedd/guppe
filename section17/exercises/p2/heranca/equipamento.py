class Equipamento:
    def __init__(self, nome: str, preco: float) -> None:
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco: float) -> None:
        self.__preco = preco

    def exibe(self) -> None:
        print(f'Nome: {self.nome}')
        print(f'Preço: {self.preco}')
