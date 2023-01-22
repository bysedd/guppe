class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, idade: int) -> None:
        self.__idade = idade

    def __str__(self) -> str:
        return f'Nome: {self.__nome} - Idade: {self.__idade}'


p1 = Pessoa('João', 20)
print(p1)
p1.nome = 'Maria'
p1.idade = 30
print(p1)
