from math import pow

s, i = 0, 0
for c in range(1, 101):
    s += int(pow(c, 2))
    i += c
sq = int(pow(i, 2))
total = sq - s
print(f'Diferença entre a soma dos quadrados dos 100 primeiros números naturais e o quadrado da soma: '
      f'\033[3:34m{sq} - {s} = {total}\033[m')
