entrada = input('Chegada(hh:mm): ').split(':')
saida = input('Saída(hh:mm): ').split(':')

h_entrada = int(entrada[0])
m_entrada = int(entrada[1])
h_saida = int(saida[0])
m_saida = int(saida[1])

if h_entrada > h_saida:
    hora_final = h_saida + 24 - h_entrada
else:
    hora_final = h_saida - h_entrada

if m_entrada > m_saida:
    minuto_final = m_saida + 60 - m_entrada
else:
    minuto_final = m_saida - m_entrada

print(f'\nA permanência foi de: \033[0:34m{hora_final} horas\033[m e \033[0:34m{minuto_final} minutos\033[m')

tempo_minutos = hora_final * 60 + minuto_final

if 1 <= tempo_minutos <= 60:
    preco = 1.0
    print(f'O valor a ser pago será de \033[0:34mR${preco:.2f}\033[m')
elif tempo_minutos <= 120:
    preco = 2.0
    print(f'O valor a ser pago será de \033[0:34mR${preco:.2f}\033[m')
elif tempo_minutos <= 180:
    preco = 4.2
    print(f'O valor a ser pago será de \033[0:34mR${preco:.2f}\033[m')
elif tempo_minutos <= 240:
    preco = 5.6
    print(f'O valor a ser pago será de \033[0:34mR${preco:.2f}\033[m')
elif tempo_minutos > 240:
    preco = hora_final * 2
    print(f'O valor a ser pago será de \033[0:34mR${preco:.2f}\033[m')
else:
    print(f'Tempo de permanência mínimo, não será necessário pagar!')
