# Runtime: 2.3538339138031006 seconds
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import time
start = time.time()
import math

# Sums divisors of a number, returns a float
def sumDivisors(num):
    sum = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            sum += (i + num/i)
    sum -= num
    if math.sqrt(num).is_integer(): # Checks for squares, loses accuracy for large num
        sum -= int(math.sqrt(num))  
    return sum

# Returns a list of amicable numbers
def getAbundantNumbers(limit):
    abundantNumbers = []
    for i in range(1, limit):
        if sumDivisors(i) > i:
            abundantNumbers.append(i)
    return abundantNumbers

# Find all possible combinations of 2 abundant numbers < upperLimit
def getPossibleCombinations(abundantNumbers, upperLimit):
    possibleCombinations = set()
    for i in range(len(abundantNumbers)):
        for j in range(i, len(abundantNumbers)):
            combination = abundantNumbers[i] + abundantNumbers[j]
            if combination > upperLimit:
                break
            else:
                possibleCombinations.add(combination)
    return possibleCombinations

# Driver
upperLimit = 23183
abundantNumbers = getAbundantNumbers(upperLimit)
possibleCombinations = getPossibleCombinations(abundantNumbers, upperLimit)

# Sum 1 to 23183
totalSum = (upperLimit) * (upperLimit + 1) / 2
# Sum all numbers in set of possible combinations
combinationSum = 0
for number in possibleCombinations: 
    combinationSum += number
# Answer is sum of all number that are NOT in combinationSum
answer = int(totalSum - combinationSum)
print(answer)
print(time.time()-start, "seconds")
