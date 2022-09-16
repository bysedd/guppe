"""
**kwargs

Poderíamos chamar este parâmetro de '**xix', mas por convenção chamamos de '**kwargs'

Este é so mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige
que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.

# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.capitalize()} é {cor.lower()}')


cores_favoritas(marcos='Verde', julia='Amarelo', fernanda='Azul', vanessa='Branco')

# OBS: os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()
cores_favoritas(geek='Navy')

# Exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs.get('geek')} Geek!"
    return 'Não tenho certeza quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))

# Nas nossas funções, podemos ter (NESTA ORDEM):
    - Parâmetros obrigatórios;
    - *args;
    - Parâmetros default (não obrigatórios);
    - **kwargs


def minha_funcao(idade: int, nome: str, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Compromissado')
    print(kwargs, end='\n\n')


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felippe', eu='Não', vc='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entenda por quê é importante manter a ordem dos parâmetros na declaração


def mostra_info(a, b, *args, instrutor='Geek', **kwargs):  # Função com a ordem correta de parâmetros
    return [a, b, args, instrutor, kwargs]


a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


def mostra_info(a, b, instrutor='Geek', *args, **kwargs):  # Função com a ordem incorreta de parâmetros
    return [a, b, args, instrutor, kwargs]


a = 1
b = 2
instrutor = 'Geek'
args = ()
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    if kwargs.get('sobrenome') is None:
        return f"{kwargs.get('nome')}"
    elif kwargs.get('nome') is None:
        return '\033[31mName is required!\033[m'
    return f"{kwargs.get('nome')} {kwargs.get('sobrenome')}"


nomes = {'nome': 'Felippe', 'sobrenome': 'Andrade'}
print(mostra_nomes(**nomes))
print(mostra_nomes(nome='Arthur'))
print(mostra_nomes(sobrenome='Silva'))

"""


def soma_numeros(a, b, c, **kwargs):
    if kwargs:
        print(a + b + c, end=' => ')
        print(kwargs)
    else:
        print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_numeros(*lista)
soma_numeros(*tupla)
soma_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_numeros(**dicionario)

# OBS! Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função

# dicionario = dict(f=1, d=2, e=3)  # TypeError
# soma_numeros(**dicionario)

dicionario = dict(a=1, b=2, c=3, nome='Geek')

soma_numeros(**dicionario, lang='Python')
