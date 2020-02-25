# Runtime: 0.10146212577819824 seconds
# Evaluate the sum of all the amicable numbers under 10000.
import time
start = time.time()
import math

# Sums divisors of a number
def sumDivisors(num):
    sum = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            sum += (i + num/i)
    sum -= num
    if int(math.sqrt(num))**2 == num: # Checks for squares
        sum -= int(math.sqrt(num))  
    return sum

# Sums all amicable numbers < limit via iteration
def sumAmicableNumbers(limit):
    sum = 0
    for i in range(limit):
        a = i + 1
        b = sumDivisors(a)
        if sumDivisors(b) == a and a != b:
            sum += a        
    return sum

# Driver
print(sumAmicableNumbers(10000))
print(time.time()-start, "seconds")
