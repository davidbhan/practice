# Runtime: 1.7624280452728271 seconds
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
import time
start = time.time()

total = 0
# We only need to check up to (9^5) * 6 = 354294, which is the maximum value for the sum of fifth powers for 6-digits
# Highest possible value for a 7-digit number is (9^5) * 7 = 413,343, which is only 6 digits
for i in range(2,354294):
    sum = 0
    for j in str(i):
        sum += int(j) ** 5
    if sum == i:
        total += i

print(total)
print(time.time()-start, "seconds")
