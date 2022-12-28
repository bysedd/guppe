letter = input("Enter a capital letter: ").upper()

if letter.isupper():
    lower_letter = chr(ord(letter) + 32)
    print(f"The corresponding lowercase letter is {lower_letter}.")
else:
    print("You did not type a capital letter.")
