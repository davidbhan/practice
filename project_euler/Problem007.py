# Runtime: 0.9184167385101318 seconds
# Find the 10001st prime number
import time
start = time.time()
import math


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

primeIndex = 0
index = 2
while(primeIndex <= 10000):
    if(isPrime(index)):
        primeIndex += 1
    if(primeIndex == 10001):
        break
    index += 1

print(index)
print(time.time()-start, "seconds")
