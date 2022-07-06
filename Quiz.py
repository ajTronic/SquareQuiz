import random
import time
import os

os.system("cls")

def getTimeFrom(start):
    return str(round(time.time() - start)) + "s"

def getQuestionInput(curr):
    return (input(f"{curr}² = "))

def printStats():
    print("Stats: ")
    print(f"   Questions right: {stats['percentage']()}%")
    print(f"   Total time elapsed: {stats['timeElapsed'](startTime)}")
    print(f"   Question time elapsed: {stats['timeElapsed'](timeOnQuestion)}")
    print(f"   Questions asked: {stats['questionsAsked']}")
    print(f"   Questions right: {stats['questionsRight']}")


stats = {
    "questionsAsked": 0,
    "questionsRight": 0,
    "timeElapsed": (lambda time : getTimeFrom(time)),
    "percentage": (lambda : stats["questionsRight"] / stats["questionsAsked"] * 100)
}

startTime = time.time()
timeOnQuestion = time.time()

def init():
    while True:
        timeOnQuestion = time.time()
        curr = round(random.random() * 99)
        stats["questionsAsked"] += 1
        gotQuestionRight = True
        inputAnswer = getQuestionInput(curr)
        while inputAnswer.rstrip() != str(pow(curr, 2)):
            if inputAnswer == "q": return
            if inputAnswer == "s": 
                printStats()
                inputAnswer = getQuestionInput(curr)
                break
            print("Wrong! Try again.")
            gotQuestionRight = False
            inputAnswer = getQuestionInput(curr)
        if gotQuestionRight: stats["questionsRight"] += 1
        print("Correct!")

init()