"""
Reversed

OBS: não confunda com a função reverse() que estudamos nas listas.
A função reverse() só funciona em listas.
Já a função reversed() funciona com qualquer iterável.
Sua função é inverter qualquer iterável.
A função reversed() retorna um iterável chamado 'list_reverseiterator'
"""

# Exemplos

lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res, type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto.
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))  # Em conjuntos não definimos a ordem dos elementos.

# Podemos iterar sobre o reversed()
[print(letra, end='') for letra in reversed('Geek University')]

# Podemos fazer o mesmo sem o uso do for
print('\n' + ''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais fácil com o slice de strings
print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
[print(n, end=' ') for n in reversed(range(0, 11))]
print()

# Apesar que também já vimos como fazer isso utilizando o próprio range()
[print(n, end=' ') for n in range(10, -1, -1)]
