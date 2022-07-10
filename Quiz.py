import random
import time
import os
import configparser

os.system("cls")

startTime = time.time()
settings = configparser.ConfigParser()
settings.read("settings.ini")

stats = {
    "questionsAsked": 0,
    "questionsRight": 0,
}

def getQuestionInput(curr): 
    if settings.get("base", "debugMode") == "True":
        return (input(f"{curr}² ({curr**2}) = "))
    else: 
        return (input(f"{curr}² = "))

def printStats():
    if stats["questionsAsked"] > 0:
        print("Stats: ")
        print(f"""   Questions right: {
            stats['questionsRight']
        } / {
            stats['questionsAsked']
        }: {round(stats['questionsRight'] / stats['questionsAsked'] * 100)}%""")
        print(f"   Average time: {round(time.time() - startTime / stats['questionsRight'])}s")
    else: print("No stats to show.")

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
        elif inputAnswer == "n": os.system("py Quiz.py")
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