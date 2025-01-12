def power_digit_sum(n):
    return sum(int(digit) for digit in str(2**n))

print(power_digit_sum(1000))