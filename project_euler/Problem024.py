# Runtime: 0.0008020401000976562 seconds
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import time
start = time.time()
import math

# There are 10! = 3628800 total permutations of the numbers, which would take too long to brute force
# There are 9! = 362880 permutations for each starting value
# i.e. 0xxxxxxxxx covers the the 1st - 362880th lexographic permutations, 
# 1xxxxxxxxx covers the the 362881st - 725760th lexographic permutations, ...
# We can use this logic to recursively determine the lexographic permutation at a given position

# Returns the permutation of digits at the target lexographic index
# Assumes all digits are unique, and the target index < number of permutations
def getPermutation(digits, targetIndex):
    answer = ""
    digitsList = list(digits)
    digitsList.sort()
    target = targetIndex - 1  # Because first iteration starts at 0

    while len(digitsList) != 0:
        length = len(digitsList)
        # Find index of number in digits to put in the nth place (nth iteration)
        # Ex: for digits 0-9, we know that the targetIndex (1000000), lies between 2*9! and 3*9!
        # Thus, the first digit must be the second digit in order (in this case, 1)
        i = (target // math.factorial(length - 1))
        answer += digitsList[i]
        target -= (i) * math.factorial(length - 1)
        del digitsList[i]

    return answer

digits = "0123456789"
target = 1000000
print(getPermutation(digits, target))
print(time.time()-start, "seconds")
