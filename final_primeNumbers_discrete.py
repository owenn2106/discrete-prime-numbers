import math
import time
import random as rd

#get the first 20 prime numbers with getPrimes.py
smallPrimeFactors = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

def primeFactors(num):
    if num <= 1:
        print("No prime factors.")
    else:
        factorList = []

        while num % 2 == 0:
            factorList.append(2)
            num = num // 2

        for i in range(len(smallPrimeFactors)):
            while num % smallPrimeFactors[i] == 0:
                factorList.append(smallPrimeFactors[i])
                num = num // smallPrimeFactors[i]

        if num > 2:
            for j in range(73, int(math.sqrt(num))+1, 2): 
                while num % j == 0: 
                    factorList.append(int(j))
                    num = num // j 

            if num > 2: 
                factorList.append(int(num))
            
    print(factorList)

numbers = []
digit = int(input("How many digits of numbers do you want to randomize (Multiple of 10 e.g. 10, 20, 30, etc.): "))
print()

if digit % 10 != 0:
    print("You need to input multiple of 10 e.g. 10, 20, 30, etc.")
else:
    for _ in range(10):
        randomNumber = rd.randint(10**(digit-1), 10**(digit)-1)
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