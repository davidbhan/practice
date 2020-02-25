# Runtime: 0.026377201080322266 seconds
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
import time
start = time.time()

# Note that the longest recurring cycle of a denominator d is d-1 since there are only d-1 possible remainders
# Returns the decimal value and length of a given denominator, up to denominator-1
def getDecimalLength(denominator):
    result = ""
    start = 1
    length = 0

    for i in range(denominator-1):
        start *= 10
        result += str(start // denominator)
        start %= denominator
        length += 1
        # If start is 1, we end up with our initial condition, so we know it loops again
        # If start is 0, we end our pattern
        if start == 0:
            length = 0
            break
        if start == 1:
            break
    return result, length


maxLength = 1
maxDenominator = 1
limit = 1000
# We know that long repeating cycles won't be divisible by 2 or 5
for i in range(7, limit, 2):
    if i % 5 == 0:
        continue
    length = getDecimalLength(i)[1]
    if length > maxLength:
        maxLength = length
        maxDenominator = i
print(maxDenominator)
print(time.time()-start, "seconds")
