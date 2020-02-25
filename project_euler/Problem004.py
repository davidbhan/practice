# Runtime: 0.25446486473083496 seconds
# Finds the largest palindrome made from the product of two 3-digit numbers.
import time
start = time.time()

def isPalindrome(n):
	if(str(n) == str(n)[::-1]):
		return True
	else:
		return False

largestPalindrome = 0

for i in range(100, 1000):
	for j in range(i, 1000):
		if(isPalindrome(i*j) and i*j > largestPalindrome):
			largestPalindrome = i*j

print(largestPalindrome)
print(time.time()-start, "seconds")
