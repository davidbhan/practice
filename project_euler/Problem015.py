# Runtime: 0.0005891323089599609 seconds
# Starting in the top left corner of a 20×20 grid, and only being able to move to the right and down, how many routes to the bottom right corner?
import time
start = time.time()
import math

# This problem does not require a computer, we can do it with pure counting
# We know we must do a total of 20 down, and 20 right
# There are 40 total moves, with 2 distinct types of moves
# Thus, the total number of moves we need to make is 40! / (20! * 20!)
gridSize = 20
moves = int(math.factorial(2*gridSize) / (math.pow(math.factorial(gridSize), 2)))
print(moves)
print(time.time()-start, "seconds")
