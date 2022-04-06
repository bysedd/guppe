value = float(input('Amount: \033[0:36mR$\033[m'))
parcel = int(input('Parcels: '))

discount_10 = value - value * 0.1
parcels_3 = value / parcel

print(f'\n\033[1:32mR${value:.2f}\033[m with \033[0:36m10% discount\033[m: \033[1:32mR${discount_10:.2f}\033[m')
print(f'\033[0:36m{parcel}x\033[m of \033[1:32mR${parcels_3:.2f}\033[m')

if parcel == 1:
    commission = discount_10 * 0.05
    print(f"Seller's commission: \033[1:32mR${commission:.2f}\033[m")
else:
    commission = value * 0.05
    print(f"Seller's commission: \033[1:32mR${commission:.2f}\033[m")
