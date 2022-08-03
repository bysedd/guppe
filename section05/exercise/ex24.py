value = float(input('Product: R$'))
state = input("""MG 7%; SP 12%; RJ 15%; MS 8%
State: """)[:2].upper()
print()

if state == 'MG':
    print('\033[0:34mMinas Gerais\033[m')
    total = value + value * 0.07
    print(f'Total price of product: \033[0:32mR${total:.2f}\033[m')
elif state == 'SP':
    print('\033[0:34mSão Paulo\033[m')
    total = value + value * 0.12
    print(f'Total price of product: \033[0:32mR${total:.2f}\033[m')
elif state == 'RJ':
    print('\033[0:34mRio de Janeiro\033[m')
    total = value + value * 0.15
    print(f'Total price of product: \033[0:32mR${total:.2f}\033[m')
elif state == 'MS':
    print('\033[0:34mMato Grosso do Sul\033[m')
    total = value + value * 0.08
    print(f'Total price of product: \033[0:32mR${total:.2f}\033[m')
else:
    print('\033[0:31mInvalid state\033[m')
