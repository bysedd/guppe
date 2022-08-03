# Uma duração que expressa a diferença entre duas instâncias de
# data, hora ou data e hora para resolução de microssegundos.
from datetime import timedelta

segundos = int(input('Seconds: '))
convert = timedelta(seconds=segundos)

print(convert)
