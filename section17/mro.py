"""
POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem de Métodos), é a ordem
de execução dos métodos (quem será executado primeiro).

Em Python, podemos conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help

"""


class Animal:
    def __init__(self, nome: str) -> None:
        self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome

    def cumprimentar(self) -> str:
        return f'Olá! Eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def nadar(self) -> str:
        return f'{self.nome} está nadando'


class Terrestre(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def andar(self) -> str:
        return f'{self.nome} está andando'

    def cumprimentar(self) -> str:
        return f'Olá! Eu sou {self.nome} da terra!'


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)


# Testando

tux = Pinguim('Tux')
print(tux.cumprimentar())  # Method Resolution Order (MRO)

"""
Pinguim(Aquatico, Terrestre)
tux.cumprimentar() -> Eu sou Tux do mar!

Pinguim(Terrestre, Aquatico)
tux.cumprimentar() -> Eu sou Tux da terra!
"""
