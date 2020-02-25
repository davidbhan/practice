# Runtime: 6.008148193359375e-05 seconds
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
import time
start = time.time()

def sumOfSquares(n):
	s = 0
	for i in range(1, n+1):
		s += i**2
	return s

def squareOfSums(n):
	s = 0
	for i in range(1, n+1):
		s += i
	return s**2

value = 100
print(squareOfSums(value) - sumOfSquares(value))
print(time.time()-start, "seconds")
