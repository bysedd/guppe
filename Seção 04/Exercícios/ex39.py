award = 780_000.00

first = award * 0.46
second = award * 0.32
third = award * 0.22

print(f"""\033[0:32mFirst: R${first:.2f}\033[m
\033[0:33mSecond: R${second:.2f}\033[m
\033[0:34mThird: R${third:.2f}\033[m""")
