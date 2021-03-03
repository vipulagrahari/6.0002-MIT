import numpy
import random


def throwNeedles(numNeedles):
    inCircle = 0
    for needles in range(1, numNeedles - 1):
        x = random.random()
        y = random.random()
        if (x * x + y * y) ** 0.5 <= 1:
            inCircle += 1
    return 4 * (inCircle / numNeedles)


def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = numpy.std(estimates)
    curEst = sum(estimates) / len(estimates)
    print('Est. = {0}, Std. dev. = {1}, Needles = {2}'.format(str(curEst), str(round(sDev, 6)), str(numNeedles)))
    return curEst, sDev

def estPercision(percision, numTrials):
    numNeedles = 1000
    sDev = percision
    while sDev > percision / 1.96:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst


estPercision(0.01, 1000)
