vogais = {
    "a": "*",
    "e": "*",
    "i": "*",
    "o": "*",
    "u": "*",
}

with open("animals.txt") as ler:
    with open("animals_without_vowels.txt", "w") as f:
        for animal in ler.readlines():
            for k, v in vogais.items():
                animal = animal.replace(k, v)
            f.write(animal)

with open("animals_without_vowels.txt") as f:
    print(f.read())
