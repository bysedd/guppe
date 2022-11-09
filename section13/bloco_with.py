"""
with

Passos para se trabalhar com arquivos:
    1 - Abrir o arquivo
    2 - Trabalhar com o arquivo
    3 - Fechar o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with.

'with' significa 'com'

"""

# O bloco with - forma Pythonica de manipular arquivos

with open("texto.txt", encoding="UTF-8") as f:
    print(f.readlines())
    print(f.closed)

print(f.closed)
