def toupper(arquivo: str, arquivo2: str):
    with open(arquivo) as file:
        f = file.read()
        with open(arquivo2, "w") as file2:
            for i in range(len(f) - 1):
                file2.write(f[i])
            file2.write("\n")


toupper("animals.txt", "animals-toupper.txt")
