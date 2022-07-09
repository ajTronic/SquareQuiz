import random
import time
import os


os.system("cls")

def getTimeFrom(start):
    return round(time.time() - start)

def getQuestionInput(curr):
    return (input(f"{curr}² ({curr ** 2}) = "))

def printStats():
    print("Stats: ")
    print(f"   Questions right: {round(stats['questionsRight'])} / {stats['questionsAsked']}: {stats['percentage']()}%")
    print(f"   Avarage speed: {stats['avgSpd']()}s")

def getPercentage(total, correct):
    if total == 0 or correct == 0: return 0
    return (correct / total) * 100

startTime = time.time()

stats = {
    "questionsAsked": 0,
    "questionsRight": 0,
    "avgSpd": lambda: (getTimeFrom(startTime) / max(stats["questionsAsked"], 1)),
    "percentage": lambda: (getPercentage(stats["questionsAsked"], stats["questionsRight"])),
}

def init():
    currQuestion = None
    newQuestion = True
    while True:
        if newQuestion: 
            currQuestion = round(random.random() * 99)
        inputAnswer = getQuestionInput(currQuestion).rstrip() # string
        if inputAnswer == "q": return
        elif inputAnswer == "s": 
            printStats() 
            newQuestion = False
        else: # check question
            stats["questionsAsked"] += 1
            try:
                inputInt = int(inputAnswer)
            except:
                print('Invalid Number.')
                continue
            if currQuestion ** 2 == inputInt:
                print("Correct!")
                newQuestion = True
                stats["questionsRight"] += 1
            else:
                print("WRONG. Try again")
                newQuestion = False

init()