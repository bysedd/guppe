from datetime import datetime

salario = 2000.0
aumento = 0.015
ano, ano_atual = 1995, datetime.now().year
print(f'Ano: \033[1:37m{ano}\033[m | '
      f'Salário: \033[0:32mR${salario:.2f}\033[m | '
      f'Aumento: \033[0:34m0.00%\033[m')
while ano <= ano_atual:
    if ano == 1996:
        salario += salario * aumento
    else:
        aumento *= 2
        salario += salario * aumento
    print(f'Ano: \033[1:37m{ano}\033[m | '
          f'Salário: \033[0:32mR${salario:.2f}\033[m | '
          f'Aumento: \033[0:34m{aumento:.2f}%\033[m')
    ano += 1
