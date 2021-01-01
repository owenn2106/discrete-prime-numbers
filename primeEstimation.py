import numpy as np

def estimateCount():

    num = int(input("Enter the highest number: "))

    # prime number theorem
    estimationPrime = num / np.log(num)
    print(estimationPrime)

    restart = input("Do you want to restart the program? (Y/N): ").upper()

    if restart == "Y":
        estimateCount()
    elif restart == "N":
        print("Program finished.")
    else:
        print("You need to input either Y or N.")

estimateCount()




# https://www.youtube.com/watch?v=7jzCJJIc59E&ab_channel=KhanAcademyLabs