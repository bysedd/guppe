"""
Generator Expression

Em aulas anteriores estudamos:
    - List Comprehension;
    - Dictionary Comprehension;
    - Set Comprehension

Não vimos:
    - Tuple Comprehension... Porque elas se chamam Generators


# Poderíamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Casimiro', 'Cristina', 'Felippe']

# List Comprehension
res = [nome.strip()[0].upper() == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome.strip()[0].upper() == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(92345668823))
print(getsizeof(True))
print(getsizeof(False))

from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dict Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print(f'Para fazer a mesma tarefa gastamos em memória:\n'
      f'List Comprehension: {list_comp} bytes\n'
      f'Set Comprehension: {set_comp} bytes\n'
      f'Dictionary Comprehension: {dict_comp} bytes\n'
      f'Generator Expression: {gen} bytes')
"""

# É possível iterar no Generator Expression? SIM!

gen = (x * 10 for x in range(10))
print(gen)
print(type(gen))

for n in gen:
    print(n, end=' - ')
print('FIM!')
