"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.

arquivo = open("texto.txt", encoding="UTF-8")

print(arquivo.read())

# seek() -> É utilizada para movimentação do cursor pelo arquivo. Ela recebe um
# parâmetro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek() -> Procurar
arquivo.seek(0)
print(arquivo.read())

arquivo.seek(22)
print(arquivo.read())

# readline() -> Função que lê o arquivo linha por linha
ret = arquivo.readline()
print(type(ret), ret, sep=" => ")
print(ret.split())

# readlines()
ret = arquivo.readlines()
print(type(ret), ret, sep=" => ")
print(len(ret))

OBS: quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e o nosso programa essa conexão é chamada streaming. Ao finalizar
os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:
    1 - Abrir o arquivo;
    2 - Trabalhar com o arquivo;
    3 - Fechar o arquivo.

# 1 - Abrir o arquivo
arquivo = open("texto.txt", encoding="UTF-8")

# 2 - Trabalhar com o arquivo
print(arquivo.read())
print(f"O arquivo está aberto? {arquivo.closed}")  # Verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo
arquivo.close()
print(f"O arquivo está aberto? {arquivo.closed}")  # Verifica se o arquivo está aberto ou fechado

# print(arquivo.read())
# Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError
"""

arquivo = open("texto.txt", encoding="UTF-8")

# Com o parâmetro no read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(37))
