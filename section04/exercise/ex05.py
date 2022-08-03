cyan = '\033[1:36m'
green = '\033[1:32m'
stop = '\033[m'

real_number = float(input('Enter a real number: '))
fifth_part = real_number / 5.0
decimal_places = len(str(real_number).split('.')[1])

print(f'The fifth part of {cyan}{real_number}{stop} is '
      f'{green}{fifth_part:.{decimal_places}f}{stop}')
