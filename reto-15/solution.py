import math
def lattice_path(n, m):
    return math.factorial(n + m) // (math.factorial(n) * math.factorial(m))

print(lattice_path(20, 20))