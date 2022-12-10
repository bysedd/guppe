# Escrevendo um iterador customizado


class Contador:
    def __init__(self, start: int, stop: int, step: int = 1):
        self.start = start
        self.numero = self.start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            self.numero = self.start
            self.start += self.step
            return self.numero
        raise StopIteration


[print(n) for n in Contador(0, 10)]
print('-=' * 10)
[print(n) for n in range(10)]
