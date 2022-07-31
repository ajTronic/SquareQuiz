from dataclasses import dataclass


@dataclass()
class StatsData:
    questionsAsked: int
    questionsRight: int
