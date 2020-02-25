# Runtime: 0.00023794174194335938 seconds
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
import time
start = time.time()

# Takes in string representation of digits, rturmns true if multiplicand,multiplier, and product are 9 pandigital
def isNinePandigital(a, b):
    number = str(a) + str(b) + str(a*b)
    if len(number) != 9:
        return False
    for i in range(1, len(number)+1):
        if str(i) not in number:
            return False
    return True

# Driver
products = []
for first in range(100000): # Only need to loop through half
    for second in range(first, 100000):
        if len(str(first*second) + str(first) + str(second)) > 9: # Automatically skip, since it's not 9 pandigital
            break
        if isNinePandigital(first, second):
            products.append(first*second)

print(sum(set(products)))
print(time.time()-start, "seconds")
