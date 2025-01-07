def sumation_of_primes(n):
    if n < 2:
        return 0  # No primes below 2

    primes_under_n = []
    for i in range(2, n):
        if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
            primes_under_n.append(i)
    return sum(primes_under_n)

print(sumation_of_primes(2000000))