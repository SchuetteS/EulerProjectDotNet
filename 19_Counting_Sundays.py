# https://projecteuler.net/problem=19

# You are given the following information, but you may prefer to do some research for yourself.

#   - 1 Jan 1900 was a Monday.
#   - Thirty days has April, June, September and November.
#     All the rest have thirty-one,
#     Saving February alone, Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
#   - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def isLeapYear(year):
    # Das Jahr ist durch 4 teilbar, und es ist nicht durch 100 teilbar, außer es ist durch 400 teilbar.
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        daysPerMonth[2] = 29
        # return True
    else:       
        daysPerMonth[2] = 28
        # return False

daysPerMonth = {1: 31,
                2: 28,
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31}

i = 1
sundays = 0

# go through every year
for year in range(1900, 2001):
    isLeapYear(year)

    # go through every month
    for month in daysPerMonth.values():
        i += month
        if year != 1900 and i % 7 == 0:
            sundays += 1

print(sundays)

# Solution: 171