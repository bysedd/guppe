"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:
1 - As tuplas são representadas por parênteses ()
print(type(()))

2 - As tuplas são imutáveis. Isso significa que ao se criar uma tupla ela não muda, toda
operação em uma tupla gera uma nova tupla.
"""

# CUIDADO 1: As tuplas são representadas por parênteses, mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1, type(tupla1))
tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2, type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento:
# noinspection PyRedundantParentheses
tupla3 = (4)  # Isso não é uma tupla!
print(tupla3, type(tupla3))
tupla4 = (4,)  # Isso é uma tupla!
print(tupla4, type(tupla4))
tupla5 = 4,
print(tupla5, type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do parênteses
"""
(4) -> Não é tupla
(4, ) -> É tupla
4, -> É tupla
"""
# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla, type(tupla))

# Desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla
print(escola)
print(curso)
# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos/variáveis para desempacotar.

# Métodos para: adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho
# * Se os valores forem todos inteiros ou reais.
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(tupla2)
print(tupla1 + tupla2)  # Tuplas são imutáveis
tupla1 += tupla2
tupla3 = (1, 2, 3) + tupla1  # mas podemos sobrescrever seus valores.
print(tupla3)
print((1, 2, 3) + tupla1)
print(tupla1)
print(tupla2)

# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(tupla.__contains__(3))
print(3 in tupla)

# Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n, end=' ')
print('\n')
for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))
escola = tuple('Geek University')
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# O acesso a elementos de uma tupla também é semelhante a de uma lista
print(meses[5])

# Slicing
print(f'Tamanho da tupla: 0-{len(meses) - 1}')
# tupla[inicio:fim:passo]
print(meses[:-5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i], end=' ')
    i += 1

# Verificamos em qual índice um elementos está na tupla
print(meses.index('Junho'))
# OBS: Caso o elemento não exista, setá gerado: ValueError: tuple.index(x): x not in tuple

# Por quê utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro*.

# * Isso porque trabalhar com elementos imutáveis traz segurança para o código.

# Copiando uma tupla para outra

tupla = (1, 2, 3)
nova = tupla  # Na tupla não temos o problema de Shallow Copy
print(tupla)
print(nova)

outra = (4, 5, 6)
nova += outra
print(nova)
print(tupla)
