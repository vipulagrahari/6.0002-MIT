import math
import random
import string

class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1,37):
            self.pockets.append(i)
        self.ball = None
        self.pocketOdds = len(self.pockets) - 1
    def spin(self):
        self.ball = random.choice(self.pockets)
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else:
            return -amt
    def __str__(self):
        return "Fair Roulette"
class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append("0")
    def __str__(self):
        return "European Roulette"
class UsRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append("00")
    def __str__(self):
        return "American Roulette"

def playRoulette(game, numSpins, pocket, bet, toPrint = False):
    totPocket = 0
    for i in range(numSpins):
        game.spin()
        totPocket += game.betPocket(pocket, bet)
    if toPrint:
        print(numSpins, "spin of", game)
        print("Expected return betting", pocket, "=", str(100*totPocket/numSpins), "%\n")
    return (totPocket/numSpins)

random.seed(0)
game = FairRoulette()
game1 = EuRoulette()
game2 = UsRoulette()

for numSpins in (100, 1000000):
    for i in range(3):
        playRoulette(game, numSpins, 2, 1, True)
        playRoulette(game1, numSpins, 2, 1, True)
        playRoulette(game2, numSpins, 2, 1, True)
        print()
        
 
