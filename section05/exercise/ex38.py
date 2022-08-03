from datetime import datetime

nascimento = input('Data de nascimento(dd/MM/yyyy):\t').split('/')
dt = datetime.now()

dia = int(nascimento[0])
mes = int(nascimento[1])
ano = int(nascimento[2])

dia_atual = datetime.now().day
mes_atual = datetime.now().month
ano_atual = datetime.now().year

if 1 <= mes <= 12 and 1 <= dia <= 31 and not (ano > ano_atual or ano < 1910):
    if not (ano % 4 == 0 and ano % 400 == 0 and not ano % 100 == 0) and mes == 2 and dia > 28:
        print('\033[0:31mDia inválido. Anos não bissextos não podem conter 29 dias em fevereiro\033[m')
    elif mes == 4 and dia > 30:
        print('Abril não pode conter 31 dias')
    elif mes == 6 and dia > 30:
        print('Junho não pode conter 31 dias')
    elif mes == 9 and dia > 30:
        print('Setembro não pode conter 31 dias')
    elif mes == 11 and dia > 30:
        print('Novembro não pode conter 31 dias')
    elif dia > dia_atual and mes > mes_atual:
        print('\033[0:31mData inválida\033[m')
    else:
        print('\033[0:32mData válida\033[m')
else:
    if not 1 <= dia <= 31:
        print('\033[0:31mDia inválido\033[m')
        if not 1 <= mes <= 12:
            print('\033[0:31mMês inválido\033[m')
        if not ano > ano_atual or ano < 1910:
            print('\033[0:31mAno inválido\033[m')
    elif not 1 <= mes <= 12:
        if not 1 <= dia <= 31:
            print('\033[0:31mDia inválido\033[m')
        print('\033[0:31mMês inválido\033[m')
        if not ano > ano_atual or ano < 1910:
            print('\033[0:31mAno inválido\033[m')
    elif ano > ano_atual or ano < 1910:
        if not 1 <= dia <= 31:
            print('\033[0:31mDia inválido\033[m')
        if not 1 <= mes <= 12:
            print('\033[0:31mMês inválido\033[m')
        print('\033[0:31mAno inválido\033[m')
