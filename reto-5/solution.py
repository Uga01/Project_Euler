def smallets_evenly_divisible(n):
    i = 1
    divisibles = list(range(1, n + 1))
    while True:
        if all(i % d == 0 for d in divisibles):
            return i
        i += 1

    

# Ejemplo de uso
print(smallets_evenly_divisible(20)) 