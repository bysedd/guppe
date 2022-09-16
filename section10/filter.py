"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção

# Biblioteca para trabalhar com dados estatísticos
import statistics as st

# Dados coletados de algum sensor
dados = 1.3, 2.7, -0.1, 4.3, 4.1, 0.8

# Calculando a média dos dados utilizando a função mean()
media = st.mean(dados)
print(f'Média = {media}')

# OBS: assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável.
res = filter(lambda dado: dado >= media, dados)
print(sorted(list(res)))

# OBS: assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.

# Possível solução
res = filter(lambda dado: dado >= media, dados)
res = list(res)
res.sort()
print(res)
print(f'Novamente: {res}')

paises = [' ', ' Argentina ', ' ', 'brasil', 'Chile', '', 'Colômbia', '', 'equador', '', '', '  venezuela']

# res = filter(None, paises)
# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(lambda pais: pais != '', paises)
res = map(lambda pais: pais.strip().title(), filter(lambda pais: pais.strip(), paises))
print(list(res))

A diferença entre map() e filter() é:
    map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento
             do iterável.
    filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos
                conforme a função.

# Exemplo mais complexo

print('Usuários no Twitter:')
usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []},
]
[print(usuario) for usuario in usuarios]

print('\nUsuários que estão inativos no Twitter:')
inativos = filter(lambda usuario: not usuario['tweets'], usuarios)
[print(usuario) for usuario in inativos]

print('\nUsuários que estão ativos no Twitter:')
ativos = filter(lambda usuario: usuario['tweets'], usuarios)
[print(usuario) for usuario in ativos]
"""

# Combinar filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria', 'a']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) >= 3, nomes)))
print(lista)
