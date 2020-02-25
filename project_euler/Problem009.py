# Runtime: 0.06825995445251465 seconds
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc
import time
start = time.time()
import math

def isPythagorean(a, b, c):
	return a**2 + b**2 == c**2

def testCombinations(value):
	for a in range(1, value):
		for b in range(a, value - a):
			c = value - a - b
			if(c < b):
				break
			if(isPythagorean(a, b, c) and a + b + c == value):
				#print(a, b, c)
				return(a*b*c)

print(testCombinations(1000))
print(time.time()-start, "seconds")
