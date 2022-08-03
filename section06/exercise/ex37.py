for c in range(1000, 9999 + 1):
    baixa_ordem = str(c)[:2]
    alta_ordem = str(c)[2:]
    total = int(baixa_ordem) + int(alta_ordem)
    total_elevado = pow(total, 2)
    if str(total_elevado) == baixa_ordem + alta_ordem:
        print(f'\033[3:34m{baixa_ordem + alta_ordem}\033[m')
        print(f'{baixa_ordem} + {alta_ordem} = \033[1:32m{total}\033[m')
        print(f'{total}² = \033[1:32m{total_elevado}\033[m')
