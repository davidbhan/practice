# Runtime: 0.0026102066040039062 seconds
# In a given 2D array, find the maximum value of four adjacent numbers in a straight line (row, column, or diagonal)
import time
start = time.time()

# Finds the maximum vertical product with sequenceLength numbers
def verticalProduct(array, sequenceLength):
	maxProduct = 1
	product = 1
	for i in range(len(array) - (sequenceLength - 1)):
		for j in range(len(array)):
			for q in range(sequenceLength):
				product *= array[i+q][j]
				if(product > maxProduct):
					maxProduct = product
			product = 1
	return maxProduct

# Finds the maximum horizontal product with sequenceLength numbers
def horizontalProduct(array, sequenceLength):
	maxProduct = 1
	product = 1
	for i in range(len(array)):
		for j in range(len(array) - (sequenceLength - 1)):
			for q in range(sequenceLength):
				product *= array[i][j+q]
				if(product > maxProduct):
					maxProduct = product
			product = 1
	return maxProduct

# Finds the maximum down-right diagonal product with sequenceLength numbers
def downDiagProduct(array, sequenceLength):
	maxProduct = 1
	product = 1
	for i in range(len(array) - (sequenceLength - 1)):
		for j in range(len(array) - (sequenceLength - 1)):
			for q in range(sequenceLength):
				product *= array[i+q][j+q]
				if(product > maxProduct):
					maxProduct = product
			product = 1
	return maxProduct

# Finds the maximum up-right product with sequenceLength numbers
def upDiagProduct(array, sequenceLength):
	maxProduct = 1
	product = 1
	for i in range((sequenceLength - 1), len(array)):
		for j in range(len(array) - (sequenceLength - 1)):
			for q in range(sequenceLength):
				product *= array[i-q][j+q]
				if(product > maxProduct):
					maxProduct = product
			product = 1
	return maxProduct

# Read in numbers
text = open("Problem011.txt", "r")
data = [[int(n) for n in line.split()] for line in text] # Split string by space, convert to int, for each line in file

# Set maxProduct to maximum value of all the possible combinations
maxProduct = 0
if(verticalProduct(data, 4) > maxProduct):
	maxProduct = verticalProduct(data, 4)
if(horizontalProduct(data, 4) > maxProduct):
	maxProduct = horizontalProduct(data, 4)
if(downDiagProduct(data, 4) > maxProduct):
	maxProduct = downDiagProduct(data, 4)
if(upDiagProduct(data, 4) > maxProduct):
	maxProduct = upDiagProduct(data, 4)
print(maxProduct)
print(time.time()-start, "seconds")
