# Runtime: 0.003818035125732422 seconds
# Finds largest prime factor of the number 600851475143
import time
start = time.time()
import math

def factorPrime(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
    return factors[len(factors)-1]

value = 600851475143
print(factorPrime(value))
print(time.time()-start, "seconds")
