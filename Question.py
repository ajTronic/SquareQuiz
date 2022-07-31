class Question:
    def __init__(self, factor1, factor2):
        self.__factor1 = factor1
        self.__factor2 = factor2

    def getFactors(self):
        return [self.__factor1, self.__factor2]
