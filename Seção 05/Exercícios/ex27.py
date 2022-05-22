idade = int(input('Idade: '))

print('\nCategoria:\033[0:34m')
if 5 <= idade <= 7:
    print('Infantil A')
elif idade <= 10:
    print('Infantil B')
elif idade <= 13:
    print('Juvenil A')
elif idade <= 17:
    print('Juvenil B')
else:
    print('Sênior')
