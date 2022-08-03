real = float(input('R$'))
dolar = float(input('\033[0:36m$1\033[m == R$'))
conversao = real / dolar

print(f'\033[0:32mR${real:.2f}\033[m --> \033[0:32m${conversao:.2f}\033[m')
