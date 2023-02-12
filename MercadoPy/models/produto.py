from MercadoPy.utils import helper


class Produto:
    def __init__(self, id: int, nome: str, preco: float, /) -> None:
        self.__id: int = id
        self.__nome: str = nome
        self.__preco: float = preco

    @property
    def id(self) -> int:
        return self.__id

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

    def __str__(self) -> str:
        return f'id: {self.id}\n' \
               f'nome: {self.nome}\n' \
               f'preço: {helper.formata_moeda(self.preco)}'
