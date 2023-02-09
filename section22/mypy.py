"""
Mypy

Mypy é um analisador de tipo estático opcional para o Python. Ele combina o poder do
sistema de tipos do Python com uma análise estática adicional para detectar erros
comuns no código Python sem a necessidade de uma execução de tempo de execução.

Instalação:
pip install mypy

Uso:
mypy <nome_do_arquivo> ou mypy <nome_do_arquivo> --ignore-missing-imports (para ignorar os imports)
"""


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

# Se executarmos o mypy, ele irá nos informar que o código está correto:
# mypy .\section22\mypy.py
# Success: no issues found in 1 source file

# Se alterarmos o código para que ele não esteja mais correto, o mypy irá nos informar
# que o código está incorreto:
print(cabecalho('geek university', alinhamento=1))

# section22\mypy.py:35: error: Argument "alinhamento" to "cabecalho" has incompatible type "int"; expected "bool"
# Found 1 error in 1 file (checked 1 source file)

# Correto
texto: str = 'Geek University'  # texto é do tipo str
print(texto)

Texto = str  # Texto é um alias para str
print(Texto, type(Texto))

nome: Texto = 'Felippe'  # nome é do tipo Texto
print(nome, type(nome))
