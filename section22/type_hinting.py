# def cumprimentar(nome: str) -> str:
#     return f'Olá {nome}'
#
#
# print(cumprimentar('Geek'))


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    texto = texto.strip().title()
    if alinhamento:
        return f'{"-" * len(texto)}\n' \
               f'{texto}\n' \
               f'{"-" * len(texto)}'
    else:
        return f' {texto} '.center(len(texto) * 3, '#')


print(cabecalho('geek university'))
print(cabecalho('geek university', alinhamento=False))
