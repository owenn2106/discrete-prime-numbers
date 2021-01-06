import math
import random as rd
import time

def primeFactors(n): 
    factorList = []  
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3, int(math.sqrt(n))+1, 2): 
          
        # while i divides n , print i and divide n 
        while n % i== 0: 
            factorList.append(int(i))
            n = n // i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        factorList.append(int(n))
    
    print(factorList)

numbers = []
digit = int(input("How many digits of numbers do you want to randomize (Multiple of 10 e.g. 10, 20, 30, etc.): "))
print()

if digit % 10 != 0:
    print("You need to input multiple of 10 e.g. 10, 20, 30, etc.")
else:
    for _ in range(10):
        randomNumber = rd.randrange(10**(digit-1)+1, 10**(digit)-1, 2)
        numbers.append(randomNumber)

for i in range(len(numbers)):
    print("The no."+str(i+1)+" "+str(digit)+"-digit number is "+str(numbers[i]))
    print("The factors are")
    start = time.time()
    primeFactors(numbers[i])
    end = time.time()
    timeOfExecution = end - start
    print("Time taken to factorize: "+str(timeOfExecution)+" seconds")
    print()

  