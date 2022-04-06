def switch(option: int):
    options = {  # Dicionário
        1: 'Domingo',
        2: 'Segunda-feira',
        3: 'Terça-feira',
        4: 'Quarta-feira',
        5: 'Quinta-feira',
        6: 'Sexta-feira',
        7: 'Sábado',
    }
    return options.get(option, 'Invalid option.')


op = int(input('Informe um dia da semana de 1 a 7: '))
if switch(op) != 'Invalid option.':
    print(f'Esse dia é \033[0:34m{switch(op)}\033[m')
else:
    print(switch(op))
