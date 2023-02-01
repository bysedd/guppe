"""
Métodos de data e hora

# Com now() podemos especificar um timezone (fuso horário)
agora = datetime.datetime.now()  # now == agora, retorna a data e hora atual
print(agora)
print(type(agora))
print(repr(agora))

# Com today() não podemos especificar um timezone (fuso horário)
hoje = datetime.datetime.today()  # today == hoje, retorna a data e hora atual
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo à meia-noite combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrando o dia da semana, weekday()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

dias_semana = {
    0: 'Segunda-feira',
    1: 'Terça-feira',
    2: 'Quarta-feira',
    3: 'Quinta-feira',
    4: 'Sexta-feira',
    5: 'Sábado',
    6: 'Domingo'
}

print(manutencao.weekday())  # Retorna o número do dia da semana (0 a 6)
print(manutencao, dias_semana[manutencao.weekday()], sep=', ')

aniversario = input('Informe sua data de nascimento (yyyy/mm/dd): ').split('/')
aniversario = [int(x) for x in aniversario]
aniversario = datetime.datetime(*aniversario)

print('Você nasceu', end=' ')
match aniversario.weekday():
    case 0:
        print('em uma segunda-feira')
    case 1:
        print('em uma terça-feira')
    case 2:
        print('em uma quarta-feira')
    case 3:
        print('em uma quinta-feira')
    case 4:
        print('em uma sexta-feira')
    case 5:
        print('no sábado')
    case 6:
        print('no domingo')

# Formatando datas/horas com strftime (String Format Time)
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)

def formatar_data(data: datetime.datetime) -> str:
    meses = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }
    return f'{data.day} de {meses[data.month]} de {data.year}'

def formatar_data(data: datetime.datetime) -> str:
    import requests

    # Configurações da API
    url = 'http://api.mymemory.translated.net/get'
    source_lang = 'en'
    target_lang = 'pt'

    # Traduzindo o mês
    response = requests.get(url, params={
        'q': data.strftime('%B'),
        'langpair': f'{source_lang}|{target_lang}'
    })
    response.raise_for_status()
    result = response.json()

    # Retornando a data formatada
    return f"{data.day} de {result['responseData']['translatedText']} de {data.year}"


hoje = datetime.datetime.today()
print(formatar_data(hoje))

nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)

almoco = datetime.time(12, 30)
print(almoco)

from timeit import timeit

# Marcando tempo de execução do nosso código com timeit

# Loop for
tempo = timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo.__round__(2))

# List comprehension
tempo = timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo.__round__(2))

# Map
tempo = timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo.__round__(2))
"""

from timeit import timeit
import functools


def teste(n) -> int:
    soma = 0
    for num in range(n * 200):
        soma += num ** num + 4
    return soma


print(timeit(functools.partial(teste, 2), number=10000))
# partial() é uma função que retorna outra função com alguns parâmetros pré-definidos
