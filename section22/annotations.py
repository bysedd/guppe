"""
import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


# print(circunferencia.__annotations__)
# {'raio': <class 'float'>, 'return': <class 'float'>}

nome: str = 'Geek University'
peso: float = 67.9
ativo: bool = True

print(nome)
print(peso)
print(ativo)

print(__annotations__)
"""


class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def idade(self) -> int:
        return self.__idade

    @property
    def peso(self) -> float:
        return self.__peso

    def andar(self: 'Pessoa') -> str:
        return f'{self.nome} está andando...'


p: Pessoa = Pessoa('Geek', 37, 69.5)
print(p.__dict__)

# print(p.__annotations__)  AttributeError: 'Pessoa' object has no attribute '__annotations__'
print(p.andar.__annotations__)

print(p.__init__.__annotations__)
