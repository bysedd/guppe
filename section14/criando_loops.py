"""
Criando sua própria versão de loop

[print(num) for num in [1, 2, 3, 4, 5]]
[print(letra) for letra in 'Geek University']
iter([1, 2, 3, 4, 5])
iter('Geek University')
"""


def meu_for(iterable):
    try:
        iterable = iter(iterable)
        while True:
            try:
                print(next(iterable))
            except StopIteration:
                break
    except TypeError:
        print('Interável inválido')


# meu_for('Geek University')
numeros = [1, 2, 3, 4, 5]
meu_for(numeros)
