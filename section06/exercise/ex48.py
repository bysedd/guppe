from math import sqrt


def f(n: int):
    return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))


def fibonacci(start: int, end: int):
    n, s = 0, 0
    cur = f(n)
    while cur <= end:
        if start <= cur:
            print(int(cur), end=' ')
        if int(cur) % 2 == 0:
            s += int(cur)
        if s > 4000000:
            s -= int(cur)
        n += 1
        cur = f(n)
    print(f'\n\033[1:34m{s}\033[m')


print(fibonacci(0, 4000000))
