# Runtime: 0.00023794174194335938 seconds
# How many different ways can £2 be made using any number of coins?
import time
start = time.time()

# Creates and array of number of possible combinations for each index, and returns possible combinations for target
def numCombinations(target):
    coins = [1, 2, 5, 10, 20, 50, 100, 200] # Types of coins
    combinations = [1] + [0]*target # Each value is number of possible combinations for given index, initialize 0 as 1
    for coin in coins: # For every coin
        for i in range(coin, target+1): # For each possible value greater than the coin
            combinations[i] += combinations[i-coin] # We add the number of possible combinations minus that coin
            """ Explanation:
                Say, for example, we want to figure out how many combinations there for the a value of 20
                Then we know that the possible combinations for 20 include the combinations for 19 (plus 1p), 18 (plus 2p), ...
            """

    return combinations[target]

print(numCombinations(200))
print(time.time()-start, "seconds")
