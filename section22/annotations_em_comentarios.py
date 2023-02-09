import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(8))


def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    texto = texto.strip().title()
    if alinhamento:
        return f'{texto}\n' \
               f'{"-" * len(texto)}'
    else:
        return f' {texto} '.center(len(texto) * 3, '#')


print(cabecalho1('cabeçalho 1', alinhamento=False))


def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    texto = texto.strip().title()
    if alinhamento:
        return f'{texto}\n' \
               f'{"-" * len(texto)}'
    else:
        return f' {texto} '.center(len(texto) * 3, '#')


print(cabecalho2('cabeçalho 2', alinhamento=False))
