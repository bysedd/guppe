from functions import error_message

arquivo_entrada = input('Digite o nome do arquivo de entrada (animals.txt): ')
arquivo_saida = input('Digite o nome do arquivo de saída (arquivo-de-saida.txt): ')

try:
    with open(arquivo_entrada, encoding='utf-8') as f:
        string = f.read()
except FileNotFoundError as err:
    print(error_message(err))
else:
    with open(arquivo_saida, "w", encoding='utf-8') as f:
        f.write(string[::-1])
