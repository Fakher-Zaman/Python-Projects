from time import *
import random as r

def speedTime(timeStart, timeEnd, userInput):
    timeDelay = timeEnd - timeStart
    timeRound = round(timeDelay, 2)
    speed = len(userInput) / timeRound
    return round(speed)

def mistake(paraTest, userTest):
    errorCount = 0
    for i in range(len(paraTest)):
        try:
            if paraTest[i] != userTest[i]:
                errorCount += 1
        except:
            errorCount += 1
    return errorCount

if __name__ == '__main__':
    while True:
        check = input("Ready to test typing speed (y/n): ")
        if check == "y" or check == "Y":
            test = ["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
                    "I love pakistan", "Welcome to the world of python", "Nothing is impossible", "Attitude is everything",
                    "Something is better than nothing"]
            test1 = r.choice(test)
            print("\n\t~~~~~~~~Typing Speed Calculator~~~~~~~\n")
            print(test1)
            print()

            time1 = time()
            testInput = input("Type Here: ")
            time2 = time()

            print("Speed: ", speedTime(time1,time2, testInput), "word/sec")
            print("Error: ", mistake(test1, testInput))
            print()
        elif check == "n" or check == "N":
            print("Thank You!")
            break
        else:
            print("Invalid Input!")