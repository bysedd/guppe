import random

"""
nomes: list = ["João", "Maria", "Pedro", "Ana", "José", "Paulo"]

versoes: tuple = (3, 4, 7)

opcoes: dict = {"window": True, "fullscreen": False, "sound": True, "music": False}

valores: set = {3, 7, 4, 2, 3, 1, 4}

print(nomes)
print(versoes)
print(opcoes)
print(valores)

print(__annotations__)
# {'nomes': <class 'list'>, 'versoes': <class 'tuple'>, 'opcoes': <class 'dict'>, 'valores': <class 'set'>}
"""

"""
from typing import List, Tuple, Dict, Set

nomes: List[str] = ["João", "Maria", "Pedro", "Ana", "José", "Paulo"]

versoes: Tuple[int, ...] = (3, 4, 7)

opcoes: Dict[str, bool] = {"window": True, "fullscreen": False, "sound": True, "music": False}

valores: Set[int] = {3, 7, 4, 2, 3, 1, 4}

print(nomes)
print(versoes)
print(opcoes)
print(valores)

print(__annotations__)
"""


# https://www.alt-codes.net/suit-cards.php
NAIPES = '♠ ♥ ♦ ♣'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio=False):
    """Cria um baralho com 52 cartas."""
    _baralho = [(n, c) for n in NAIPES for c in CARTAS]
    if aleatorio:
        random.shuffle(_baralho)
    return _baralho


def distribuir_cartas(_baralho):
    """Gerencia a mão de cartas conforme o baralho gerado."""
    return _baralho[::4], _baralho[1::4], _baralho[2::4], _baralho[3::4]


def jogar():
    """Inicia um jogo de cartas para 4 jogadores."""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}
    for jogador, cartas in maos.items():
        cartas = ' '.join('{}{}'.format(*c) for c in cartas)
        print(f'{jogador}: {cartas}')
    return maos


if __name__ == '__main__':
    jogar()
