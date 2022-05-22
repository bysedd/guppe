salario = float(input('Salário atual do funcionário: \033[0:34mR$\033[m'))
tempo = int(input('Ano(s) de serviço na empresa: '))
salario_final = 0.0

# Reajuste
if 0 < salario <= 500.0:
    salario_final = salario + salario * 0.25
elif salario <= 1000.0:
    salario_final = salario + salario * 0.20
elif salario <= 1500.0:
    salario_final = salario + salario * 0.15
elif salario <= 2000.0:
    salario_final = salario + salario * 0.10
elif salario > 2000.0:
    salario_final = salario

# Tempo de serviço
if 1 <= tempo <= 3:
    salario_final += 100.0
elif tempo <= 6:
    salario_final += 200.0
elif tempo <= 10:
    salario_final += 300.0
elif tempo > 10:
    salario_final += 500.0

print(f'Valor do salário reajustado: \033[0:34mR${salario_final:.2f}\033[m')
