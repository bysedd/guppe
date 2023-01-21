"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, fazendo
com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

A herança múltipla pode ser feita de duas formas:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;

# Exemplo 1 - Multiderivação Direta

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base4:
    pass


class Base5(Base4):
    pass


class Base6(Base5):
    pass


class MultiDerivada(Base6):
    pass


OBS: não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará
os atributos e métodos de todas as classes herdadas.

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

    def cumprimentar(self) -> str:
        return f'Olá! Eu sou {self.nome} do mar!'


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
baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())
print()

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())
print()

tux = Pinguim('Tux')
print(tux.nadar())
print(tux.andar())
print(tux.cumprimentar())  # Method Resolution Order (MRO)
print()

# Objeto é instância de...
print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instância de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')
print(f'Tux é instância de object? {isinstance(tux, object)}')
