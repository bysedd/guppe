from datetime import timedelta

inicio = input('Start: ')
hora = int(inicio.split(':')[0])
minuto = int(inicio.split(':')[1])
segundo = int(inicio.split(':')[2])

segundo += hora * 3600
segundo += minuto * 60
inicio = timedelta(seconds=float(segundo))

duracao = input('Duration: ')
duracao = timedelta(seconds=float(duracao))

conclusao = timedelta.__add__(inicio, duracao)

print(f"""\nStart: \033[0:36m{inicio}\033[m
Duration: \033[0:31m{duracao}\033[m
Conclusion: \033[0:32m{conclusao}\033[m""")
