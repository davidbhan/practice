# Runtime: 0.000244140625 seconds
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
import time
start = time.time()

# Number of days in month
monthLengthsNotLeap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthLengthsLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Checks for leap year
def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# We know jan first is a Monday (denoted by 0), Sunday is denoted by 6
# We can calculated the first day of the following month, knowing the first day of the current month
# Ex: a month of 30 days starts on 0 (Monday), the first day of the next month is (0+30) % 7 = 2 (Wednesday)

# Pass in a year, and the first day of that year, return a list of all the starting days for the months in that year
def getMonthStartDays(year, firstDay):
    if isLeapYear(year):
        monthLengths = monthLengthsLeap
    else:
        monthLengths = monthLengthsNotLeap
    startDays = []
    tempStart = firstDay
    startDays.append(tempStart)
    for month in monthLengths:
        tempStart = (tempStart + month) % 7
        startDays.append(tempStart)
    startDays.pop() # Remove value of first day of following year
    return startDays, tempStart

# Driver
days = []
temp, startDay = getMonthStartDays(1900, 0) # Gets first day of 1901
for year in range(1901, 2001):
    temp, startDay = getMonthStartDays(year, startDay)
    days.extend(temp)
print(days.count(6))
print(time.time()-start, "seconds")
