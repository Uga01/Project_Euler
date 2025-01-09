def count_divisors(num):
    divisors = 0
    sqrt_num = int(num**0.5)
    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            divisors += 2  # i and num // i
    if sqrt_num * sqrt_num == num:  # If num is a perfect square, avoid double-counting
        divisors -= 1
    return divisors

def highly_divisible_triangular_number(n):
    i = 1
    while True:
        triangular_number = i * (i + 1) // 2
        if count_divisors(triangular_number) >= n:
            return triangular_number
        else:
            i += 1
print(highly_divisible_triangular_number(500))