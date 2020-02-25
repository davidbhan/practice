# Runtime: 0.3105180263519287 seconds
# Find the value of the first triangle number to have over five hundred divisors
import time
start = time.time()
import math

# Returns number of divisors in a number
def numDivisors(n):
    numDivisors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            numDivisors += 2
        if i * i == n:
            numDivisors -= 1
    return numDivisors

# Makes use of the property that two consecutive numbers, n and n+1 are coprime
# Thus, number of devisors for (n)(n+1) is number of divisors (n) * number of divisors (n+1)
for n in range(1,1000000):
    triangleNum = int((n*(n+1))/2)
    if n % 2 == 0:
        count = numDivisors(n/2) * numDivisors(n+1)
    else:
        count = numDivisors(n) * numDivisors((n+1)/2)
    if count >= 500:
        print(triangleNum)
        break
print(time.time()-start, "seconds")
