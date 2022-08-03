vi = int(input('Digite o valor inicial: '))
vf = int(input('Digite o valor final: '))
s = 0
if vf > vi:
    for c in range(vi, vf + 1):
        if c % 2 != 0:
            s += c
    print(f'Soma dos ímpares neste intervalo: \033[3:34m{s}\033[m')
else:
    print('\033[1:31mIntervalo de valores inválido\033[m')
