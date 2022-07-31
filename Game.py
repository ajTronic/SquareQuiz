import random
import os
import configparser
import Printer
import time
from Question import Question
from StatsData import StatsData


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
        self.statsData = StatsData(0, 0)

    def getQuestionInput(self, curr):
        if self.isDebug:
            return input(f"{curr[0]} * {curr[1]} ({curr[0] * curr[1]}) = ")
        else:
            return input(f"{curr[0]} * {curr[1]} = ")

    def stats(self):
        if self.statsData.questionsAsked > 0:
            Printer.printStats(self.statsData, self.startTime)
        else:
            Printer.noStats()

    def start(self):
        newQuestion = True
        questionNum = 0
        isSquaring = self.mode == "squaring"
        while questionNum < self.numQuestions:
            if newQuestion:
                currQuestion = None
                if isSquaring:
                    factor = round(random.randint(self.min, self.max))
                    currQuestion = Question(factor, factor)
                elif self.mode == "multiplication":
                    currQuestion = Question(
                        round(random.randint(self.min, self.max)),
                        round(random.randint(self.min, self.max)),
                    )
                questionFactors = currQuestion.getFactors()
            inputAnswer = self.getQuestionInput(questionFactors).rstrip()  # string
            if inputAnswer == "q":
                return
            elif inputAnswer == "s":
                self.stats()
                newQuestion = False
                continue
            elif inputAnswer == "n":
                os.system("py Game.py")
            else:  # check question
                self.statsData.questionsAsked += 1
                try:
                    inputInt = int(inputAnswer)
                except:
                    Printer.invalid()
                    continue
                if questionFactors[0] * questionFactors[1] == inputInt:
                    Printer.correct()
                    newQuestion = True
                    self.statsData.questionsRight += 1
                else:
                    Printer.wrong()
                    newQuestion = False
            questionNum += 1
        self.stats()
        Printer.finish()


os.system("cls")

game = Game("d:\Code\Python\SquareQuiz\settings.ini")
game.start()
