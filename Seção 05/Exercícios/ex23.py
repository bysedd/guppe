year = int(input('Year: '))

if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
    print(f'\033[0:34m{year}\033[m\033[0:32m is a leap year\033[m')
else:
    print(f"\033[0:34m{year}\033[m\033[0:31m isn't leap year\033[m")
