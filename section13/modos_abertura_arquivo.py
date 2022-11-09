"""
Modos de abertura de arquivo

r -> Abre para leitura - padrão
r -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita - somente se o arquivo não existir, senão gera FileExistsError
a -> Abre para escrita - adicionando o conteúdo ao final do arquivo
+ -> Abre para atualização - leitura e escrita, temos controle do cursor

OBS: abrindo no modo "a" (append), se o arquivo não existir será criado. Caso exist, o novo conteúdo
SEMPRE será adicionado no final do arquivo, não importa a posição do cursor.

https://docs.python.org/3/library/functions.html#open

# Exemplo com modo "x"
try:
    with open("university.txt", "x", encoding="UTF-8") as f:
        f.write("Teste de conteúdo.\n")
except FileExistsError:
    print("Arquivo já existente.")

# Exemplo com modo "a"
with open("frutas.txt", "a", encoding="UTF-8") as f:
    while True:
        fruta = input("Informe uma fruta ou (sair): ").title()
        if fruta != "Sair":
            f.write(f"{fruta}\n")
        else:
            break

# Exemplo com modo "r+"
with open("outro.txt", "r+", encoding="UTF-8") as f:
    f.write("Adicionada!\n")
    f.seek(11)
    f.write("Nova linha.\n")
    f.seek(32)
    f.write("Mais uma linha.\n")

"""
