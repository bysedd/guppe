def switch(option: int):
    options = {  # Dicionário
        0: 0,
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }
    return options.get(option, '\033[0:31mInvalid option.\033[m')


op = int(input('Informe um mês de 1 a 12: '))
if switch(op) != '\033[0:31mInvalid option.\033[m':
    print(f'Esse mês é \033[0:34m{switch(op)}\033[m')
else:
    print(switch(op))
