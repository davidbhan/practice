# Runtime: 0.007093906402587891 seconds
# What is the total of all the name scores in the file?
import time
start = time.time()
import re

# Gets alphabetical value of each letter and sums them
def getAlphabetValue(name):
    value = 0
    for char in name:
        value += (ord(char) - 64)
    return value

# Multiplies each alphabetical value with its position in a given array
def sumValues(data):
    total = 0
    for i in range(len(data)):
        total += (i+1) * getAlphabetValue(data[i])
    return total

# Driver
text = open("Problem022.txt", "r").read()
text = re.sub(r'"', '', text)
data = [word for word in text.split(',')]
data.sort()
print(sumValues(data))
print(time.time()-start, "seconds")
