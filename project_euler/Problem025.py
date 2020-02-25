# Runtime: 0.03116607666015625 seconds
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
import time
start = time.time()

def fibonacciLength(limiter):
    num = 1
    index = 1 # set index at 1 because we end up skipping first fib term
    a = 0
    b = 1
    while len(str(num)) < limiter:
        if(a <= b):
            a += b
            index+=1
            num = a
        else:
            b += a
            index+=1
            num = b
    return index

print(fibonacciLength(1000))
print(time.time()-start, "seconds")
