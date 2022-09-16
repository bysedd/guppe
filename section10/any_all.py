"""
Any e All

all() --> Retorna True se todos os elementos do iterável forem True ou ainda se o iterável está vazio.

# Exemplo all()
print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False
print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True
print(all([]))  # Iterável vazio? True
print(all((1, 2, 3, 4)))  # Tupla
print(all({1, 2, 3, 4}))  # Set
print(all('Geek'))  # String

nomes = ['Carlos', 'Camila', 'Carla', 'Casimiro', 'Cristina']
print(all([nome.strip()[0].upper() == 'C' for nome in nomes]))

# OBS: Um iterável vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

any() --> Retorna True se qualquer elemento do iterável for True. Se o iterável estiver vazio, retorna False.
"""

print(any([0, 1, 2, 3, 4]))  # True
print(any([0, False, {}, (), '']))  # False

nomes = ['Carlos', 'Camila', 'Carla', 'Casimiro', 'Cristina', 'Felippe']
print(any([nome.strip()[0].upper() == 'C' for nome in nomes]))  # True

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))  # True
print(any([num for num in [1, 5, 3, 9, 7, 11] if num % 2 == 0]))  # False
