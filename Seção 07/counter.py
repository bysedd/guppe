"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datatypes
               Tipo de dados container de alta performance

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.
"""

# Realizando o import
from collections import Counter

# Exemplo 1
# Podemos utilizar qualquer iterável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

# <class 'collections.Counter'>
# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 2, 45: 2, 66: 2, 43: 1, 34: 1})
# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2
print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3
texto = '''A Área de Comando Oriental foi um de vários comandos geográficos criados pela Real Força Aérea Australiana 
(RAAF) durante a Segunda Guerra Mundial. Foi formada em Maio de 1942 e controlava as unidades localizadas em 
Nova Gales do Sul e no sul de Queensland. Com sede em Sydney, as responsabilidades da Área de Comando Oriental 
incluíam a defesa  aérea, o reconhecimento aéreo e a proteção das rotas marítimas dentro dos seus limites. 
As suas unidades aéreas  operavam caças, bombardeiros de reconhecimento e bombardeiros de mergulho, e concentravam-se 
na escolta de comboios marítimos, patrulha marítima e guerra anti-submarina. O tamanho da área era tal que a RAAF 
considerou por duas vezes dividi-la, porém esta ideia nunca se concretizou.'''
palavras = texto.split(' ')  # Separa o texto pelos espaços e adiciona em uma lista
periodos = texto.split('.')
print(f'Esse texto contém {len(periodos)} períodos.')
print(Counter(palavras))
print(Counter('a=4, b=2)'))

# Encontrando as 5 palavras com mais ocorrência no texto
print(Counter(palavras).most_common(5))
