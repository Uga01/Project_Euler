def prime_number(n):
    i = 0
    number = 2
    while i < n:
        if number == 2:
            i += 1
            number += 1
        elif all(number % x != 0 for x in range(2, number)):
            i += 1
            number += 1
        else:
            number += 1
    return number - 1

print(prime_number(10001)) # 13