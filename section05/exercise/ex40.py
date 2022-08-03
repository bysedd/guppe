fabrica = float(input('Custo de fábrica: \033[0:34mR$\033[m'))
distribuidor, impostos, consumidor = 0, 0, 0

if 0 < fabrica <= 12000.0:
    distribuidor = 0.05
    consumidor = fabrica + fabrica * distribuidor
elif fabrica <= 25000.0:
    distribuidor = 0.10
    impostos = 0.15
    consumidor = fabrica + fabrica * distribuidor * impostos
elif fabrica > 25000.0:
    distribuidor = 0.15
    impostos = 0.20
    consumidor = fabrica + fabrica * distribuidor * impostos

print(f'Custo ao consumidor: \033[0:34mR${consumidor:.2f}\033[m')
