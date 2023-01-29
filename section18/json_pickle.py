"""
JSON e Pickle

JSON: JavaScript Object Notation

API - São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, Youtube, etc.) e terceiros (nós desenvolvedores).


import json

ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])
print(type(ret), ret, sep='\n')


class Gato:
    def __init__(self, nome: str, raca: str):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def raca(self) -> str:
        return self.__raca


felix = Gato('Felix', 'Angorá')
print(felix.__dict__)

ret = json.dumps(felix.__dict__)
print(ret)

Integrando JSON e Pickle

pip install jsonpickle

felix = Gato('Felix', 'Angorá')
ret = jsonpickle.encode(felix)
print(ret)
"""

import jsonpickle


class Gato:
    def __init__(self, nome: str, raca: str):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def raca(self) -> str:
        return self.__raca


if __name__ == '__main__':
    felix = Gato('Felix', 'Angora')

    # Fazendo a escrita em um arquivo JSON
    with open('felix.json', 'w') as f:
        f.write(jsonpickle.encode(felix))

    # Fazendo a leitura de um arquivo JSON
    with open('felix.json', 'r') as f:
        felix_json = f.read()
        ret = jsonpickle.decode(felix_json)
        print(ret.__dict__)
        print(ret.nome, ret.raca, sep='\n')
