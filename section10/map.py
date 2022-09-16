"""
Map

Com map, fazemos mapeamento de valores para função.
Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável

from math import pi


def area(r: float, arr: int = 2):
    Calcula a área de um círculo com raio 'r'.
    :param r: Raio
    :param arr: Arredondar valor
    :return: Área
    return float(f'{(pi * r ** 2):.{arr}f}')


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))
print(areas)

# Forma 2 — Map
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

raios = [2, 5, 7.1, 0.3, 10, 44]

Forma 3 — Map com Lambda
print(list(map(lambda r: round(pi * r ** 2), raios)))

OBS: após utilizar a função map() depois da primeira utilização do resultado, ele zera.

Para fixar — Map

Temos dados iteráveis:
dados: a1, a2, ..., an

Temos uma função:
f(x):
    ...

Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

O Map Object: f(a1), f(a2), f(...), f(an)
"""

# Mais um exemplo

print('Cidade, Temperatura em graus Celsius:')
cidades_c = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokyo', 27), ('Nova York', 28),
             ('Londres', 22)]
[print(cidade) for cidade in cidades_c]

# Fórmula: °F = 9/5 * °C + 32

cidades_f = list(map(lambda dado: (dado[0].strip().capitalize(), round(9 / 5 * dado[1] + 32)), cidades_c))
print('\nCidade, Temperatura em Fahrenheit:')
[print(cidade) for cidade in cidades_f]
