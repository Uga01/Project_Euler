def special_pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a + 1, n - a):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
            
print(special_pythagorean_triplet(1000))