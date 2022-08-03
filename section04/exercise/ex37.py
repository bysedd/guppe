price = float(input('Price of the product: $'))
discount = price - price * 0.12

print(f'Discount price: \033[0:32m${discount:.2f}\033[m')
