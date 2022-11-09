"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização passamos apenas um parâmetro
de entrada, caminho neste caso para o arquivo a ser lido. Essa função retorna
um __io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

OBS: por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro 'FileNotFoundError'

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode='r' -> modo de leitura. r -> read() -> ler
"""

# Exemplo
arquivo = open("texto.txt", encoding="UTF-8")
# print(arquivo)
# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()
ret = arquivo.read()

print(type(ret))
print(ret)

# print(arquivo.read())
# OBS: o Python utiliza um recurso para trabalhar com arquivo chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo.

# OBS: a função read() lê o conteúdo completo do arquivo.
