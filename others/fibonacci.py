qtd = int(input())

for _ in range(qtd):
    n = int(input())
    ultimo = 1
    penultimo = 1
    fibo = [0, 1]

    for count in range(2, n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        fibo.append(termo)
    print(f"Fib({n}) = {fibo[n] if n < 2 else fibo[n - 1]}")
