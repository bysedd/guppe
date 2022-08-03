old_price = float(input('Preço antigo: \033[0:34mR$\033[m'))
aumento = old_price
new_price = 0

if old_price < 50:
    aumento += old_price * 0.05
    print('Aumento de \033[0:34m5%\033[m')
elif old_price <= 100:
    aumento += old_price * 0.10
    print('Aumento de \033[0:34m10%\033[m')
else:
    aumento += old_price * 0.15
    print('Aumento de \033[0:34m15%\033[m')

new_price = aumento
print(f'Novo preço: \033[0:32mR${new_price:.2f}\033[m\033[0:34m')

if new_price < 80:
    print('Barato')
elif new_price <= 120:
    print('Normal')
elif new_price <= 200:
    print('Caro')
else:
    print('Muito caro')
