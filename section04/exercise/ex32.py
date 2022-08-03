num = int(input("Enter an integer: "))
triplo = num * 3 + 1
dobro = num * 2 - 1
total = triplo + dobro

print(f"The sum of the successor of it's triple and the predecessor of it's double is: "
      f'\033[0:36m{total}\033[m')
