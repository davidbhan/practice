# Runtime: 0.0003848075866699219 seconds
# Find the first ten digits of the sum of the one-hundred 50-digit numbers.
import time
start = time.time()

text = open("Problem013.txt", "r")
data = [int(line) for line in text]

sum = 0
for number in data:
    sum += number
print(str(sum)[:10])
print(time.time()-start, "seconds")
