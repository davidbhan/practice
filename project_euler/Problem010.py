# Runtime: 0.9272933006286621 seconds
# Find sum of all prime numbers below 2 million
import time
start = time.time()
import math

# Checks if n is prime or not
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

# Returns list of prime numbers < n
def primeArray(n):
    primes = []
    i = 2
    while(i < n):
        if(isPrime(i)):
            primes.append(i)
        i += 1
    return primes

# Eratosthenes algorithm
numArray =[]
value = 2000000
for i in range(value):
    numArray.append(i)

#we create a list of prime numbers less than sqrt(value), then remove their multibples
primes = primeArray(int(math.sqrt(value)) + 1)
for i in primes:
    for p in range(i*2, value, i):
        numArray[p] = 0

print(sum(numArray) - 1)
print(time.time()-start, "seconds")
