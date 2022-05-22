data = input('Digite uma data no formato (dd/MM/yyyy): ').split('/')

dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

if 1 <= mes <= 12 and 1 <= dia <= 31:
    if not (ano % 4 == 0 and ano % 400 == 0 and not ano % 100 == 0) and mes == 2 and dia > 28:
        print('\033[0:31mDia inválido.\033[m Anos não bissextos não podem conter 29 dias em fevereiro.')
    elif mes == 4 and dia > 30:
        print('Abril não pode conter 31 dias')
    elif mes == 6 and dia > 30:
        print('Junho não pode conter 31 dias')
    elif mes == 9 and dia > 30:
        print('Setembro não pode conter 31 dias')
    elif mes == 11 and dia > 30:
        print('Novembro não pode conter 31 dias')
    else:
        print('\033[0:32mData válida.\033[m')
else:
    print('\033[0:31mData inválida.\033[m')
