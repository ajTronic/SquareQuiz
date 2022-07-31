import random
import time
import os
import configparser

class Game:
    def __init__(self, settingsFile):
        self.startTime = time.time()
        self.settings = configparser.ConfigParser()
        self.settings.read(settingsFile)
        self.stats = {
            "questionsAsked": 0,
            "questionsRight": 0,
        }

    def getQuestionInput(self, curr): 
        if self.settings.get("debug", "debugMode") == "True":
            return (input(f"{curr}² ({curr**2}) = "))
        else: 
            return (input(f"{curr}² = "))

    def printStats(self):
        if self.stats["questionsAsked"] > 0:
            print("stats: ")
            print(f"""   Questions right: {
                self.stats['questionsRight']
            } / {
                self.stats['questionsAsked']
            }: {round(self.stats['questionsRight'] / self.stats['questionsAsked'] * 100)}%""")
            if self.stats["questionsRight"] > 0:
                print(f"   Average time: {round((time.time() - self.startTime) / self.stats['questionsRight'])}s")
        else: print("No stats to show.")

    def start(self):
        currQuestion = None
        newQuestion = True
        question = 0
        while question < int(self.settings.get("question", "numQuestions")):
            if newQuestion: 
                currQuestion = round(
                    random.randint(
                        int(self.settings.get("question", "min")),
                        int(self.settings.get("question", "max")),
                    )
                )
            inputAnswer = self.getQuestionInput(currQuestion).rstrip() # string
            if inputAnswer == "q": return
            elif inputAnswer == "s": 
                self.printStats() 
                newQuestion = False
                continue
            elif inputAnswer == "n": os.system("py Quiz.py")
            else: # check question
                self.stats["questionsAsked"] += 1
                try:
                    inputInt = int(inputAnswer)
                except:
                    print('Invalid Number.')
                    continue
                if currQuestion ** 2 == inputInt:
                    print("Correct!")
                    newQuestion = True
                    self.stats["questionsRight"] += 1
                else:
                    print("WRONG. Try again")
                    newQuestion = False
            question += 1
        self.printStats()
        print("\nThank you for playing SQUAREQUIZ™.\n")

os.system("cls")

game = Game('d:\Code\Python\SquareQuiz\settings.ini')
game.start()