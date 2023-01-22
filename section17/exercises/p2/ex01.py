exercicios = list(range(2, 9))

for ex in exercicios:
    if ex < 10:
        ex = str(0) + str(ex)
    with open(f"ex{ex}.py", "w") as f:
        f.write(f"# Path: section17\\exercises\\p2\\ex{ex}.py\n")
