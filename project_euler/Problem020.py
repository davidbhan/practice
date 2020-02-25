# Runtime: 0.0008299350738525391 seconds
# Find the sum of the digits in the number 100!
import time
start = time.time()
import math

number = str(math.factorial(100))
sum = 0
for digit in number:
    sum += int(digit)
print(sum)
print(time.time()-start, "seconds")
