import time


def printStats(stats, startTime):
    print("stats: ")
    print(
        f"""   Questions right: {
            stats.questionsRight
        } / {
            stats.questionsAsked
        }: {round(stats.questionsRight / stats.questionsAsked * 100)}%"""
    )
    if stats.questionsRight > 0:
        print(
            f"   Average time: {round((time.time() - startTime) / stats.questionsRight)}s"
        )


def invalid():
    print("Invalid Number.")


def wrong():
    print("WRONG. Try again")


def finish():
    print("\nThank you for playing SQUAREQUIZ.\n")


def unkownGameMode():
    print("Unkown GameMode.")


def newGame(gameMode):
    print(f"Starting a new {gameMode} game.")


def correct():
    print("Correct!")


def noStats():
    print("No stats to show.")
