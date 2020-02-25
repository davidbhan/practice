# Runtime: 0.002048015594482422 seconds
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
import time
start = time.time()

unitsWords = "skipZero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
tensWords = "skipZero ten twenty thirty forty fifty sixty seventy eighty ninety".split()

# Returns english name of number recursively
def numToWord(num):
    if num == 1000:
        return "one thousand"
    elif num >= 100:
        hundreds = unitsWords[num // 100] + " hundred"
        num %= 100
        if num == 0:
            return hundreds
        else:
            return hundreds + " and " + numToWord(num)
    elif num >= 20:
        tens = tensWords[num // 10]
        num %= 10
        if num == 0:
            return tens
        else:
            return tens + "-" + numToWord(num)
    else:
        return unitsWords[num]

# Counts number of letters in a word without spaces and hyphens
def countLetters(word):
    return len(word) - word.count(' ') - word.count('-')

# Driver for program
print( sum(countLetters(numToWord(i)) for i in range(1, 1001)) )
print(time.time()-start, "seconds")
