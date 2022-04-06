p = float(input('\033[0:37mWhat is the value of the prize?\033[m \033[0:36mR$\033[m'))
a = float(input('\033[0:37mHow much has bettor A (biggest bet) invested?\033[m \033[0:36mR$\033[m'))
b = float(input('\033[0:37mHow much has bettor B (middle bet) invested?\033[m \033[0:36mR$\033[m'))
c = float(input('\033[0:37mHow much has bettor C (smallest bet) invested?\033[m \033[0:36mR$\033[m'))

total = a + b + c
res_a = (a / total) * p
res_b = (b / total) * p
res_c = (c / total) * p

print(f"\n\033[0:37mGambler's Profit\033[m \033[1:36mA\033[m \033[0:32mR${res_a:.2f}\033[m")
print(f"\033[0:37mGambler's Profit\033[m \033[1:36mB\033[m \033[0:32mR${res_b:.2f}\033[m")
print(f"\033[0:37mGambler's Profit\033[m \033[1:36mC\033[m \033[0:32mR${res_c:.2f}\033[m")
