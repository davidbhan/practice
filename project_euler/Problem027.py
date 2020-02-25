# Runtime: 7.877299070358276 seconds
# Find the product of the coefficients, aa and bb, for the quadratic expression that produces the maximum number of primes for consecutive values of nn, starting with n=0n=0.
import time
start = time.time()
import math

# TODO: OPTIMIZE THIS TO < 3 SECONDS

# Returns if a number is prime or not
def isPrime(n):
    if(n<2):
        return False
    elif(n==2 or n==3):
        return True
    else:
        x = 2
        while(x < int(math.sqrt(n)) + 1):
            if(n%x == 0):
                return False
            x+=1
        return True

# Returns numbers of consecutive primes generated starting n = 0
def countPrimes(a, b):
    numPrimes = 0
    n = 0
    while(isPrime(n**2 + a*n + b)):
        numPrimes += 1
        n += 1
    return numPrimes

# Driver
maxLength = 0
first, second = 0, 0
for a in range(-999, 1000): # Loop through all possible values of a
    for b in range(1, 1001): # Loop through all values of b (b must be positive)
        length = countPrimes(a,b)
        if(length > maxLength):
            maxLength = length
            first = a
            second = b

print(first*second)
print(time.time()-start, "seconds")
