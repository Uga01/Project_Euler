def sum_square_difference(n):
    return sum(range(1, n + 1)) ** 2 - sum((i ** 2) for i in range(1, n + 1))

#Example
print(sum_square_difference(100))