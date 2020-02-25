# Runtime: 0.0006279945373535156 seconds
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?
import time
start = time.time()

# Reads in a dimension, and counts the corner value from the outside in
def sumCorners(dimension):
    sum = 1 # Initialize center value of 1
    value = dimension**2 # Find highest number
    for layer in range(int(dimension/2), 0, -1): # Loop through every layer, starting from outisde
        for corner in range(4): # Add value in each corner
            sum += value
            value -= layer*2
    return sum

print(sumCorners(1001))
print(time.time()-start, "seconds")
