"""
Escrevendo em arquivos

OBS: ao abrir um arquivo para leitura não podemos realizar a escrita nele, apenas ler.
Da mesma forma, se abrimos um arquivo para escrita, não podemos lê-lo, somente escrever.

OBS: ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, primeiro abrimos o arquivo e utilizamos a função write().
Esta função recebe UMA STRING como parâmetro, caso contrário teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso ele já exista, ele será substituído.

# Exemplo de escrita - modo 'w' - write (escrever)

# Forma tradicional de escrita em arquivo (não Pythonica)
arquivo = open("mais.txt", mode="w", encoding="UTF-8")
arquivo.write("Um texto qualquer.\n")
arquivo.write("Mais um texto.\n")
arquivo.close()

# Forma Pythonica
with open("novo.txt", mode="w", encoding="UTF-8") as f:
    f.write("Escrever dados em arquivo é muito fácil.\n")
    f.write("Podemos colocar quantas linhas quisermos.\n")
    f.write("Esta é a última linha.")

with open("geek.txt", "w", encoding="UTF-8") as f:
    f.write("Geek\n" * 1000)

"""

with open("frutas.txt", "w", encoding="UTF-8") as f:
    while True:
        fruta = input("Informe uma fruta ou digite 'sair': ").title()
        if fruta != 'Sair':
            f.write(f"{fruta}\n")
        else:
            break
