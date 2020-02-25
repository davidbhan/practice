# Runtime: 0.0003490447998046875 seconds
# Find the maximum total from top to bottom of the triangle
import time
start = time.time()

# Start from bottom of triangle, selecting larger of two adjacent values and adding to the row above it
# Height of triangle and width of base are the same length
def collapseTriangle(triangle):
    for row in range(len(triangle)-1, 0, -1): # Go from bottom row to top row
        for index in range(len(triangle[row])-1): # For each index in the row above the current row
            triangle[row-1][index] += max(triangle[row][index], triangle[row][index+1])
    return triangle

# Read in numbers
text = open("Problem018.txt", "r")
data = [[int(n) for n in line.split()] for line in text] # Split string by space, convert to int, for each line in file

# Driver
print(collapseTriangle(data)[0][0])
print(time.time()-start, "seconds")
