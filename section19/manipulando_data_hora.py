"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime.

# print(dir(datetime))

print(datetime.MAXYEAR)  # Retorna o ano máximo que o datetime pode trabalhar
print(datetime.MINYEAR)  # Retorna o ano mínimo que o datetime pode trabalhar

print(datetime.datetime.now())  # Retorna a data e hora atual

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)

# Alterar o horário para 16 horas, 0 minutos, 0 segundos, 0 micro-segundos
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

print(evento := datetime.datetime(year=2019, month=1, day=1, hour=0), type(evento), sep=' -> ')
print(evento := '2019-01-01 00:00:00', type(evento), sep=' -> ')

# Recebendo dados do usuário e convertendo para data
nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ').split('/')
nascimento = [int(x) for x in nascimento]

try:
    nascimento = datetime.datetime(day=nascimento[0], month=nascimento[1], year=nascimento[2])
    print(nascimento, type(nascimento), sep=' -> ')
except ValueError:
    print('Data inválida!')
"""

import datetime

evento = datetime.datetime.now()

# Acessando individualmente os elementos de data e hora
print(evento.year)  # Ano
print(evento.month)  # Mês
print(evento.day)  # Dia

print(evento.hour)  # Hora
print(evento.minute)  # Minuto
print(evento.second)  # Segundo
print(evento.microsecond)  # Micro-segundo
