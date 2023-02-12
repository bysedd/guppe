from mercado import *
from time import sleep

if __name__ == '__main__':
    mercado: Mercado = Mercado()

    while True:
        try:
            mercado.menu()
        except ValueError as e:
            print(f'{e.__class__.__name__}: {e}')
            break
