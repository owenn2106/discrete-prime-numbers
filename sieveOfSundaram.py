import math
import time

def SieveOfSundaram(n): 

    nNew = int((n - 1) / 2)

    marked = [0] * (nNew + 1)
  
    for i in range(1, nNew + 1): 
        j = i
        while((i + j + 2 * i * j) <= nNew): 
            marked[i + j + 2 * i * j] = 1; 
            j += 1 
  
    if (n > 2): 
        primes.append(2)
  
    for i in range(1, nNew + 1): 
        if (marked[i] == 0): 
            primes.append(2 * i + 1)

primes = []
factorList = []

num = int(input())

start = time.time()

limit = math.sqrt(num)
SieveOfSundaram(limit)

for i in range(len(primes)):
    while num % primes[i] == 0:
        factorList.append(primes[i])
        num = num // primes[i]

if num > 2:
    factorList.append(int(num))

print(factorList)

end = time.time()

timeOfExecution = end - start
print("Time taken to factorize: "+str(timeOfExecution)+" seconds")