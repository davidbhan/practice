# Runtime: 1.8835067749023438e-05 seconds
# Find sum of even fibonacci numbers less than 4 million
import time
start = time.time()

def fibonacci(limiter):
	sum = 0
	a = 0
	b = 1

	while(a < limiter and b < limiter):
		if(a <= b):
			a += b
			if(a >= limiter):
				break
			if(a % 2 == 0):	
				sum += a
		else:
			b += a
			if(b >= limiter):
				break
			if(b % 2 == 0):	
				sum += b
	return sum

print(fibonacci(4000000))
print(time.time()-start, "seconds")
