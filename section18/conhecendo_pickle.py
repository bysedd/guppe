"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

Este processo é chamado serialização/deserialização

OBS: O módulo Pickle não é seguro contra dados maliciosos e desta forma
não é recomendado trabalhar com arquivos pickle vindos de outras pessoas
que você não conheça ou de fontes desconhecidas.

    # Fazendo a leitura em um arquivo pickle
    with open('animais.pickle', 'rb') as f:
        gato, cachorro = pickle.load(f)
        print(f'O gato chama-se: {gato.nome}')
        gato.mia()
        print(f'O tipo do gato é {type(gato)}\n')

        print(f'O cachorro chama-se: {cachorro.nome}')
        cachorro.late()
        print(f'O tipo do cachorro é: {type(cachorro)}')
"""

import pickle


class Animal:
    def __init__(self, nome: str):
        self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome

    def comer(self) -> None:
        print(f'{self.__nome} está comendo...')


class Gato(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def mia(self) -> None:
        print(f'{self.nome} está miando...')


class Cachorro(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def late(self) -> None:
        print(f'{self.nome} está latindo...')


if __name__ == '__main__':
    gato = Gato('Garfield')
    cachorro = Cachorro('Pluto')

    # Fazendo a escrita em um arquivo pickle
    with open('animais.pickle', 'wb') as f:
        pickle.dump((gato, cachorro), f)

    # Fazendo a leitura em um arquivo pickle
    with open('animais.pickle', 'rb') as f:
        for obj in pickle.load(f):
            print(f'O {obj.__class__.__name__.lower()} chama-se {obj.nome} e é do tipo {type(obj)}')
