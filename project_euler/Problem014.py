# Runtime: 2.104935884475708 seconds
# Find the starting number, under one million, that produces the longest chain in Collatz Problem
import time
start = time.time()

# Brute Force Solution, no longer used (just here for historical purposes)
def checkEach(limit):
    maxLength = 0
    maxNum = 0
    for i in range(1, limit+1):
        length = 0
        n = i
        while n != 1:
            if n % 2 == 0:
                n = n/2
            else:
                n = 3*n + 1
            length += 1
        if length > maxLength:
            maxLength = length
            maxNum = i
        print(i, length)
    print("Max:", maxNum)

# Better solution, keeping track of previously found collatz sequence lengths
def smarterSolution(limit):
    sequenceLength = [0] * limit # list of collatz lengths for numbers less than limit, each number corresponds with index - 1
    sequenceLength[0] = 1 # Initialize first number
    maxLength = 1
    maxNum = 1
    for i in range(2, limit+1):
        length = 0
        n = i
        # Continue sequence until we reach a number whose seqence length we already have
        while n > limit or sequenceLength[int(n)-1] == 0:
            if n % 2 == 0:
                n /= 2
            else:
                n = (3 * n) + 1
            length += 1
        length += sequenceLength[int(n)-1]
        sequenceLength[i-1] = length
        if length > maxLength:
            maxLength = length
            maxNum = i
    print(maxNum)

# Driver for program
smarterSolution(1000000)
print(time.time()-start, "seconds")
