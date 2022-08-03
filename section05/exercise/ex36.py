venda = float(input('Valor da venda: \033[0:34mR$\033[m'))
comissao = 0.0

if venda >= 100000.0:
    comissao += 700 * 0.16
elif venda >= 80000.0:
    comissao += 650 * 0.14
elif venda >= 60000.0:
    comissao += 600 * 0.14
elif venda >= 40000.0:
    comissao += 550 * 0.14
elif venda >= 20000.0:
    comissao += 500 * 0.14
elif venda <= 20000.0:
    comissao += 400 * 0.14

print(f'A comissão que deve ser paga ao vendedor é de \033[0:32mR${comissao:.2f}\033[m')
