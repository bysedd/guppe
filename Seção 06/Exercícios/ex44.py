from math import sqrt


def f(n: int):
    return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))


def fibonacci(start: int, end: int):
    n = 0
    cur = f(n)
    while cur <= end:
        if start <= cur:
            print(int(cur), end=' ')
        n += 1
        cur = f(n)
    print(int(cur))


num = int(input('Digite um número: '))
fibonacci(0, num)
