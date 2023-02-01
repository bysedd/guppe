"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyy 12:55:34.9939329
data_final = dd/mm/yyy 13:34:23.0948484

delta = data_final - data_inicial

# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento, no caso, o meu aniversário
aniversario = datetime.datetime(day=1, month=6, year=2023)

# Calculando o tempo para o evento (delta)
tempo_para_evento = aniversario - data_hoje

# Imprimindo o tipo de dado e o valor
print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)

print(f"Faltam {tempo_para_evento.days} dias e {tempo_para_evento.seconds // 60 // 60} horas para o evento.")
"""

import datetime

data_da_compra = datetime.datetime.now()
regra_boleto = datetime.timedelta(days=3)
print(f'Data da compra: {data_da_compra.strftime("%d/%m/%Y %H:%M:%S")}')

vencimento_boleto = data_da_compra + regra_boleto
print(f'Vencimento do boleto: {vencimento_boleto.strftime("%d/%m/%Y %H:%M:%S")}')
