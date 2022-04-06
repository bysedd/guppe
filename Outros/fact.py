from math import factorial

x = int(input("!"))
f = 0

if x < 0:
    print("Fatorial não existe")

elif x == 0:
    f = 1

else:
    f = factorial(x)
    
print(f"!{x} = {f}")
