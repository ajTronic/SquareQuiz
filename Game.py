import random
import os
import configparser
import Printer
import time


class Game:
    def __init__(self, settingsFile):
        # settings
        settings = configparser.ConfigParser()
        settings.read(settingsFile)
        question = settings["question"]
        self.min = int(question["min"])
        self.max = int(question["max"])
        self.mode = question["mode"]
        self.numQuestions = int(question["numQuestions"])
        self.isDebug = settings.get("debug", "on") == "True"

        self.startTime = time.time()
        self.statsData = {
            "questionsAsked": 0,
            "questionsRight": 0,
        }

    def getQuestionInput(self, curr):
        if self.isDebug:
            return input(f"{curr}² ({curr**2}) = ")
        else:
            return input(f"{curr}² = ")

    def stats(self):
        if self.statsData["questionsAsked"] > 0:
            Printer.printStats(self.statsData, self.startTime)
        else:
            Printer.noStats()

    def start(self):
        currQuestion = None
        newQuestion = True
        question = 0
        while question < self.numQuestions:
            if newQuestion:
                currQuestion = currQuestion = round(
                    random.randint(
                        self.min,
                        self.max,
                    )
                )
            inputAnswer = self.getQuestionInput(currQuestion).rstrip()  # string
            if inputAnswer == "q":
                return
            elif inputAnswer == "s":
                self.stats()
                continue
            elif inputAnswer == "n":
                os.system("py Quiz.py")
            else:  # check question
                self.statsData["questionsAsked"] += 1
                try:
                    inputInt = int(inputAnswer)
                except:
                    Printer.invalid()
                    continue
                if currQuestion**2 == inputInt:
                    Printer.correct()
                    newQuestion = True
                    self.statsData["questionsRight"] += 1
                else:
                    Printer.wrong()
                    newQuestion = False
            question += 1
        self.stats()
        Printer.finish()


os.system("cls")

game = Game("d:\Code\Python\SquareQuiz\settings.ini")
game.start()
