"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Quando reimplementamos um método presente na classe pai em classes filhas
estamos realizando uma sobrescrita de método (Overriding).

O overriding é a melhor representação do polimorfismo.
"""


class Animal(object):
    def __init__(self, nome: str) -> None:
        self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome

    def falar(self) -> None:
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self) -> None:
        print(f'{self.nome} está comendo...')


class Cachorro(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def falar(self) -> None:
        print(f'{self.nome} fala au au!')


class Gato(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def falar(self) -> None:
        print(f'{self.nome} fala miau!')


class Rato(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def falar(self) -> None:
        print(f'{self.nome} fala algo squeak!')


# Testando
felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

vinicin = Rato('Vinicius')
vinicin.comer()
vinicin.falar()

# OBS: Não podemos criar objetos de uma classe abstrata (classe que possui pelo menos um método abstrato) - Animal
