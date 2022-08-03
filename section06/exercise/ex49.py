s_carlos = 9000
s_joao = 3000
p_carlos = s_carlos * 0.02
rf_joao = s_joao * 0.01
m = 0

while rf_joao <= s_carlos:
    rf_joao += s_joao * 0.01
    m += 1
    print(f'Fundo de renda fixa de João: \033[0:32mR${rf_joao:.2f}\033[m | \033[0:34m{m}º mês\033[m')
