def longest_collatz_sequence(n):
    longest_number = 0
    longest_chain = 0

    for i in range(n, 0, -1):
        current_number = i
        chain_length = 0

        while current_number != 1:
            if current_number % 2 == 0:
                current_number //= 2
            else:
                current_number = 3 * current_number + 1
            chain_length += 1

        if chain_length > longest_chain:
            longest_chain = chain_length
            longest_number = i

    return longest_number
print(longest_collatz_sequence(1000000))