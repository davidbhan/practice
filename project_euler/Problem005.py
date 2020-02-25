# Runtime: 9.989738464355469e-05 seconds
# Find smallest positive number that is evenly divisible by all of the numbers from 1 to 20
import time
start = time.time()

# Get array of factors of a number
def getFactors(n):
	f = []
	for i in range(2, n+1):
		while(n % i == 0):
			f.append(i)
			n /= i
	return f

# Gets the product of all numbers in an array
def multArray(array):
	product = 1
	for i in range(len(array)):
		product *= array[i]
	return product


factors = [1]
value = 20

# Add all unique factors of number 1-20 into a list
for i in range(2, value):
	temp = getFactors(i)
	for p in range(len(temp)):
		if(factors.count(temp[p]) < temp.count(temp[p])):
			factors.append(temp[p])
			
print(multArray(factors))
print(time.time()-start, "seconds")
