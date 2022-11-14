"""
Sistema de Arquivos - Manipulação

Path relativo

# Descobrindo se um arquivo existe
print(os.path.exists("arquivo.txt")) -> False
print(os.path.exists("frutas.txt")) -> True

# Descobrindo se um diretório existe
print(os.path.exists("exercises")) -> True
print(os.path.exists("exercises/exemplos")) -> False

Path absoluto

print(os.path.exists("/home/visitante/imagem.png")) -> False
print(os.path.exists("/home/bysedd/Documentos/guppe/others/upgrade_packages.py")) -> True

print(os.path.exists("/home/visitante")) -> False
print(os.path.exists("/home/bysedd/Documentos/guppe")) -> True

# Criando arquivos - forma 1
open("arquivos-teste1.txt", "w").close()

# Criando arquivos - forma 2
open("arquivos-teste2.txt", "a").close()

# Criando arquivos - forma 3
with open("arquivo-teste3.txt", "w") as f:
    pass

# Criando arquivos - forma4
os.mknod("arquivo-teste4.txt")
os.mknod("/home/bysedd/Documentos/guppe/section13/arquivo-teste5.txt")
# OBS: criando o arquivo via mknod() se ele já existir teremos o erro FileExistsError

# Cria um único diretório

os.mkdir("/home/bysedd/Documentos/guppe/section13/templates")
# OBS: a função mkdir() cria um diretório se este não existir, caso contrário retorna o erro FileExistsError

os.mkdir("/etc/templates")
# OBS: se não tivermos permissão para criarmos o diretório teremos um PermissionError

# Criando múltiplos diretórios - árvore de diretórios
# os.mkdir("exercises/exemplos/primeiro-exemplo") -> FileNotFoundError
os.makedirs("exercises/exemplos/primeiro-exemplo")
os.makedirs("exercises/exemplos/segundo_exemplo", exist_ok=True) -> não lança o erro se o arquivo já existir

# Renomear diretórios
os.rename("exercises", "exercicios")
# OBS: se o diretório não existir teremos um FileNotFoundError
os.rename("exercicios", "exercises")
# OBS: se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Renomear arquivos
os.rename("geek.txt", "geek-university.txt")
os.rename("/home/bysedd/Documentos/guppe/section13/mais.txt", "/home/bysedd/Documentos/guppe/section13/more.txt")

# Removendo arquivos
# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles
# não vão para a lixeira, eles somem.
os.remove("novo.txt")
# OBS: caso o arquivo não exista, teremos o FileNotFoundError
# OBS: se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

# Removendo diretórios vazios
os.rmdir("templates")
# OBS: se o diretório tiver qualquer conteúdo, teremos um OSError
# OBS: se o diretório não existir, teremos um FileNotFoundError

# Removendo uma árvore de arquivos
for arquivo in os.scandir("exercises2"):
    if arquivo.is_file():
        os.remove(arquivo.path)
        print(f"\033[32marquivo '{arquivo.name}' removido\033[m")
    else:
        print(f"\033[31marquivo '{arquivo.name}' não removido\033[m")
else:
    print("\nfim")

# Podemos remover uma árvore de diretórios vazios
os.removedirs("exercises2/outro/teste")
# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

from send2trash import send2trash
send2trash("arquivo-teste5.txt")
# OBS: se o arquivo ou diretório não existir teremos OSError

# Importando o tempfile
import tempfile

# Criando um diretório temporário
with tempfile.TemporaryDirectory() as tmp_dir:
    print(f"Criei o diretório temporário em: {tmp_dir}")
    with open(os.path.join(tmp_dir, "arquivo_temporario.txt"), "w") as f:
        f.write("Geek University\n")
    input()
# Estamos criando um diretório temporário, abrindo, e criado um arquivo para escrevermos um texto.
# No final estamos usando um input() só para não deletarmos os arquivos instantaneamente.

# Criando um arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b"Geek University\n")
    tmp.seek(0)
    print(tmp.read())
# OBS: em arquivos temporários, só conseguimos escrever bits. Por isso, utilizamos o 'b' antes da string

# Sem o bloco with
f = tempfile.TemporaryFile()
f.write(b"Geek University\n")
f.seek(0)
print(f.read())
f.close()

https://docs.python.org/3/library/os.html?highlight=os#module-os
"""
