"""
Conjuntos

— Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos
da matemática.

— Aqui no Python, os conjuntos são chamados Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
— Elementos não são acessados via índice, ou seja, conjuntos não indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos,
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (‘sets’) são referenciados em Python com chaves {}

Diferença entre Conjuntos(‘set’) e Mapas(Dicionários) em Python:
    — Um dicionário tem chave, valor;
    — Um conjunto tem apenas valor;
"""

# Definindo um conjunto:

# Forma 1
s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}  # Repare que temos valores repetidos
print(s, type(s))
# OBS: ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar erro e não fará parte do conjunto.

# Forma 2 — Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s, type(s))
s.pop()
print(s)

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3 na coleção')
else:
    print('Não tem o 3 na coleção')

# Importante lembrar que além de não termos valores duplicados não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos.')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos.')

# Dicionários NÃO aceitam chaves duplicadas, então temos 8 chaves
dicionario = {}.fromkeys({99, 2, 34, 23, 2, 12, 1, 44, 5, 34}, 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos.')

# Conjuntos NÃO aceitam valores duplicados, então temos 8 valores
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos.')

# Assim como qualquer conjunto Python podemos colocar tipos de dados misturados em Sets
s = {1, 'b', False, 34.22, 44}
print(s, type(s))

# Podemos iterar em um ‘set’ normalmente
for valor in s:
    print(valor, end=' ')

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
# O que você faria? Faria um ‘loop’ na lista...?
# Podemos utilizar o ‘set’ para isso:
print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(s)

# Remover elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)  # Não é índice! Informamos o valor a ser removido
print(s)
# OBS: caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado

# Forma 2
s.discard(2)
print(s)
# OBS: Se o valor não for encontrado, nenhum erro é gerado

s = {1, 2, 3}
print(s)
# Copiando um conjunto para outro...

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)

# Forma 2 - Shallow Copy
novo = s
print(novo)
novo.add(4)
print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos matemáticos de Conjuntos

# Imagine que temos dois conjuntos: um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Suellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Gerar um conjunto de estudantes de um curso que não estão no outro
somente_python = estudantes_python.difference(estudantes_java)
print(somente_python)
somente_java = estudantes_java.difference(estudantes_python)
print(somente_java)

# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
# {'Ana', 'Fernando', 'Pedro', 'Gustavo', 'Patricia', 'Guilherme', 'Suellen', 'Julia', 'Marcos'}
# unicos1 = estudantes_java.union(estudantes_python)
# {'Pedro', 'Suellen', 'Guilherme', 'Marcos', 'Fernando', 'Ana', 'Julia', 'Patricia', 'Gustavo'}
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Veja que alguns alunos que estudam Python também estudam Java.
# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 — Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem TODOS inteiros ou reais
s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
