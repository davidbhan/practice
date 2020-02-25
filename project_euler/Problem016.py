# Runtime: 0.00014328956604003906 seconds
# What is the sum of the digits of the number 2^1000?
import time
start = time.time()

num = str(pow(2, 1000))
sum = 0
for digit in num:
    sum += int(digit)
print(sum)
print(time.time()-start, "seconds")
