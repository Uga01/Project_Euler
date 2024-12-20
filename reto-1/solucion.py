def multiples_below_n(n):
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

n = 1000
resultado = multiples_below_n(n)
print(resultado)