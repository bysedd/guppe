"""
Sistema de Arquivos e Navegação

Para usar a manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

os -> Operation System - Sistema Operacional

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())  # /home/lopov/Documentos/guppe/section13

# chdir() -> para mudar o diretório
while os.getcwd() != "/":
    os.chdir("..")
    print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo
print(os.path.isabs("/home/lopov/"))
print(os.path.isabs("home/lopov/"))

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix (linux, mac), nt (windows)

# Podemos ter mais detalhes no sistema operacional
print(os.uname())

import sys
print(sys.platform)

print(os.getcwd())  # /home/lopov/Documentos/guppe/section13
res = os.path.join(os.getcwd(), "exercises")
os.chdir(res)
print(os.getcwd())  # /home/lopov/Documentos/guppe/section13/exercises

# Veja que o os.path.join() recebe dois ou mais parâmetros, sendo o primeiro o diretório atual e o demais o diretório
# que será juntado ao primeiro.

# listdir() -> Podemos listar os arquivos e diretórios
print(os.listdir("/etc"))
print(len(os.listdir("/etc")))

"""

import os

# scandir() -> Podemos listar os arquivos e diretórios com mais detalhes
with os.scandir() as f:
    f = list(f)

    # print(arquivos)

    # print(dir(arquivos[0]))

    print(f[0].inode())  # ??
    print(f[0].is_dir())  # é um diretório?
    print(f[0].is_file())  # é um arquivo?
    print(f[0].is_symlink())  # é um link simbólico?
    print(f[0].name)  # nome do arquivo
    print(f[0].path)  # caminho do arquivo
    print(f[0].stat())  # estatísticas...

    # OBS: quando utilizamos a função scandir() nós precisamos fecha-la, assim quando abrimos um arquivo
