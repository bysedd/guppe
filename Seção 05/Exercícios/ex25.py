from math import sqrt, pow

print('2nd degree equation')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
print()

if a != 0:
    delta = pow(b, 2) - 4 * a * c
    if delta < 0:
        print('\033[0:31mThere is no root\033[m')
    elif delta == 0:
        print('\033[0:32mSingle root\033[m')
    else:
        x1 = -b + sqrt(delta) / (2 * a)
        x2 = -b - sqrt(delta) / (2 * a)
        print(f'\033[0:34mΔ\033[m = \033[1:32m{delta}\033[m')
        print(f"\033[0:34mx'\033[m = \033[1:32m{x1:.1f}\033[m")
        print(f"\033[0:34mx''\033[m = \033[1:32m{x2:.1f}\033[m")
else:
    print("\033[0:31mIt's not a 2nd degree equation\033[m")
