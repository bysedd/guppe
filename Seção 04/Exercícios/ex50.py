from datetime import date

idade = int(input('Age: '))
ano_atual = date.today().year
ano_nascimento = ano_atual - idade

x = input('Have you had a birthday this year? (\033[1:32my\033[m/\033[1:31mn\033[m) ')[0]

if x.lower() == 'y':
    print(f'Year of birth: \033[0:34m{ano_nascimento}\033[m')

elif x.lower() == 'n':
    print(f'Year of birth: \033[0:34m{ano_nascimento - 1}\033[m')
