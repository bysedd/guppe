"""
Módulo Collections - Default Dict

# Recap Dicionários
dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)  # Imprime o dicionário em si
print(dicionario['curso'])  # Imprime o valor na chave 'curso'
print(dicionario['outro'])  # ??? KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default(padrão),
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar valores.
"""

from collections import defaultdict

dicionario = defaultdict(lambda: 'Chave não está presente')

dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

print(dicionario['outro'])  # KeyError no dicionário comum, mas aqui não.
print(dicionario, type(dicionario))

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for chave, valor in s:
    d[chave].append(valor)
print(sorted(d.items()))

d = {}
for chave, valor in s:
    d.setdefault(chave, []).append(valor)
print(d)

# Contar letras
s = 'Felippe'
d = defaultdict(int)
for chave in s:
    d[chave] += 1
print(d.items())

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)
print(sorted(d.items()))
