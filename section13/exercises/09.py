with open("animals.txt") as file:
    with open("animals_without_vowels.txt") as file2:
        with open("animals_combo", "w") as file3:
            while True:
                if file.readline():
                    file3.write(file.readline())
                if file2.readline():
                    file3.write(file2.readline())
                else:
                    break
