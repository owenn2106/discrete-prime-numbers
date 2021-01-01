import math
import random as rd
import time
import numpy as np

def main():
    def factorizationProgram():
        def prime_factors(x): 
            list_factor = []  
            while x % 2 == 0: 
                list_factor.append(2)
                x = x / 2
                
            for i in range(3, int(math.sqrt(x))+1, 2): 
                
                while x % i== 0: 
                    list_factor.append(int(i))
                    x = x / i 
                    
            if x > 2: 
                list_factor.append(int(x))
            
            print(list_factor)

        list_numbers = []
        digit = int(input("Masukkan nomor dengan berapa digit yang anda inginkan (dengan kelipatan sepuluh (10,20,30) sesuai soal): "))
        print()

        if digit % 10 != 0:
            print("Anda harus memasukkan digit berpekipatan sepuluh (10,20,30) sesuai soal")
        else:
            for _ in range(10):
                randomNumber = rd.randint(10**(digit-1), 10**(digit)-1)
                list_numbers.append(randomNumber)

        for i in range(len(list_numbers)):
            print("Nomor "+str(i+1)+" dengan "+str(digit)+" digit angka adalah "+str(list_numbers[i]))
            print("Faktornya adalah")
            start = time.time()
            prime_factors(list_numbers[i])
            end = time.time()
            waktu_proses= end - start
            print("Waktu yang dibutuhkan untuk melakukan faktorisasi: "+str(waktu_proses)+" detik")
            print()

    def estimateCount():
        num = int(input("Masukkan berapa digit angka yang ingin anda perkirakan (1000000, atau 10000000, atau 100000000) :"))

        # prime number theorem
        estimationPrime = num / np.log(num)
        print(estimationPrime)


    print("Which program do you want to use?")
    print("1. Prime Factorization")
    print("2. Estimating Number of Primes")
    mainInput = int(input("Choose a number (1 or 2): "))

    if mainInput == 1:
        factorizationProgram()
    elif mainInput == 2:
        estimateCount()
    else:
        print("You need to input either 1 or 2.")

    restart = input("Do you want to restart the program? (Y/N): ").upper()

    if restart == "Y":
            main()
    elif restart == "N":
        print("Program finished.")
    else:
        print("You need to input either Y or N.")

main()