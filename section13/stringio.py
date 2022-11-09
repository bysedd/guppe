"""
StringIO

ATENÇÃO: para ler ou escrever dados em arquivos do sistema operacional, o software precisa
ter permissão:
    - permissão de leitura -> para ler o arquivo
    - permissão de escrita -> para escrever o arquivo

StringIO -> Utilizado para ler e criar arquivos em memória.

# Primeiro fazemos o import
from io import StringIO

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos o texto depois.
arquivo = StringIO("Esta é apenas uma string normal.\n")

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos
print(arquivo.read())

# Escrevendo outro texto
arquivo.write("Outro texto.\n")

# Podemos inclusive movimentar o cursor
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

"""

from io import StringIO

with StringIO("Esta é apenas uma string normal.\n") as f:
    print(f.read())
    f.write("Outro texto.\n")
    f.seek(0)
    print(f.read())
