while True:
    op = int(input("""\t\033[1:34m Menu\033[m
\033[0:34m1\033[m km/h --> m/s
\033[0:34m2\033[m m/s --> km/h
\033[0:31m3\033[m Finalizar
Opção: """))
    if op == 1:
        km_h = float(input('Quilômetro por hora: '))
        m_s = km_h / 3.6
        print(f'\033[0:32m{m_s:.1f}\033[m metro por segundo\n')
    elif op == 2:
        m_s = float(input('Metro por segundo: '))
        km_h = m_s * 3.6
        print(f'\033[0:32m{km_h:.1f}\033[m quilômetro por hora\n')
    elif op == 3:
        break
