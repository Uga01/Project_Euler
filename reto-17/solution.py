def number_letter_counts(n):
    units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundred = "hundred"
    thousand = "thousand"
    and_ = "and"
    total = 0

    for i in range(1, n + 1):
        if i < 10:  
            total += len(units[i - 1])
        elif i < 20:  
            total += len(teens[i - 10])
        elif i < 100:  
            total += len(tens[i // 10 - 2])
            if i % 10 != 0:  
                total += len(units[i % 10 - 1])
        elif i < 1000: 
            total += len(units[i // 100 - 1]) + len(hundred)
            if i % 100 != 0: 
                remainder = i % 100
                if remainder < 10: 
                    total += len(and_) + len(units[remainder - 1])
                elif remainder < 20:  
                    total += len(and_) + len(teens[remainder - 10])
                else:  
                    total += len(and_) + len(tens[remainder // 10 - 2])
                    if remainder % 10 != 0:
                        total += len(units[remainder % 10 - 1])
        else:  
            total += len(units[i // 1000 - 1]) + len(thousand)

    return total

print(number_letter_counts(1000))
