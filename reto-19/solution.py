def counting_sundays():
    days = 0
    sundays = 0
    for year in range(1900, 2001):
        for month in range(1, 13):
            if year > 1900 and days % 7 == 6:
                sundays += 1
            if month in [1, 3, 5, 7, 8, 10, 12]:
                days += 31
            elif month in [4, 6, 9, 11]:
                days += 30
            elif month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    days += 29
                else:
                    days += 28
    return sundays

print(counting_sundays())