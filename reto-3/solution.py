import numpy as np
def largest_prime_factor(n):
    def trial_division(n):
        factor = 2
        while factor * factor <= n:
            if n % factor:
                factor += 1
            else:
                n //= factor
        if n > 1:
            return n
        return factor

    return trial_division(n)

print(largest_prime_factor(600851475143))

    
    