import math
import random
import string

# #Roll Die
# def rolldie():
#     return random.choice([1,2,3,4,5,6])

# #Simulation for 1111 
# def runSim(goal, numTrials, txt):
#         total = 0
#         for i in range(numTrials):
#             result = ''
#             for j in range(len(goal)):
#                 result += str(rolldie())
#             if result == goal:
#                 total += 1
            
#         print('Actual probability of', txt, "=", round(1/(6**len(goal)), 8)) 
#         estimatedProbability = round(total/numTrials, 8)
#         print("Estimated probability of", txt, "=", estimatedProbability)

# runSim("11111", 1000, "11111")
# # output = Actual probability of 11111 = 0.0001286
# #          Estimated probability of 11111 = 0.001

# #Same birthdate model
# def sameDate(numPeople, numSame):
#     # possibleDates = [i for i in range(366)]
#     possibleDates = 4*list(range(0, 57)) + [58] +4*list(range(59, 366)) + 4*list(range(180, 270))
#     birthdays = [0]*366
#     for p in range(numPeople):
#         birthdate = random.choice(possibleDates)
#         birthdays[birthdate] += 1
#     return max(birthdays) >= numSame

# #same date simulation
# def birthdayProb(numPeople, numSame, numTrials):
#     numHits = 0
#     for i in range(numTrials):
#         if sameDate(numPeople, numSame):
#             numHits += 1
#     return numHits/numTrials   

# #test birthdate model 
# for numPeople in [10, 20, 40, 100]:
#     print('for', numPeople, "est probability of a shared birthday is ", birthdayProb(numPeople, 2, 10000))
#     numerator = math.factorial(366)
#     denominator = (366**numPeople)*(math.factorial(366-numPeople))
#     print('for', numPeople, "actual probability of a shared birthday is ",1 - numerator/denominator)
#     print()

#     output for first birthday set

# for 10 est probability of a shared birthday is  0.1128
# for 10 actual probability of a shared birthday is  0.1166454118039999

# for 20 est probability of a shared birthday is  0.4068
# for 20 actual probability of a shared birthday is  0.4105696370550831

# for 40 est probability of a shared birthday is  0.8834
# for 40 actual probability of a shared birthday is  0.89054476188945

# for 100 est probability of a shared birthday is  1.0
# for 100 actual probability of a shared birthday is  0.9999996784357714

#     output for second birthday set

# for 10 est probability of a shared birthday is  0.123
# for 10 actual probability of a shared birthday is  0.1166454118039999

# for 20 est probability of a shared birthday is  0.4464
# for 20 actual probability of a shared birthday is  0.4105696370550831

# for 40 est probability of a shared birthday is  0.9158
# for 40 actual probability of a shared birthday is  0.89054476188945

# for 100 est probability of a shared birthday is  1.0
# for 100 actual probability of a shared birthday is  0.9999996784357714

#Random walks

class location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x   
    def getY(self):
        return self.y

    def dist_from(self, other):
            xDist = self.x - other.getX()
            yDist = self.y - other.getY()
            return (xDist**2 + yDist**2)**0.5
    def __str__(self):
        return '<' + self.x + ',' + self.y + '>'

class drunk(object):
    def __init__(self, name = None):
        self.name = name 
    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'

class usual_drunk(drunk):
    def take_step(self):
        step_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(step_choices)

class masochist_drunk(drunk):
    def take_step(self):
        step_choices = [(0.0, 1.1), (1.0, 0.0), (0.0, -0.9), (-1.0, 0.0)]
        return random.choice(step_choices)
class Cold_drunk(drunk):
    def take_step(self):
        step_choices = [(0.0,1.0), (0.0,-2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)
class EW_drunk(drunk):
    def take_step(self):
        step_choices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)

class field(object):
    def __init__(self):
        self.drunks = {}
    def add_drunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError("Drunk already present!")
        else:
            self.drunks[drunk] = loc
    def get_loc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("No drunk found!") 
        else:
            return self.drunks[drunk]
    def move_drunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("drunk not in Field!")
        xDist, yDist = drunk.take_step()
        self.drunks[drunk] = self.drunks[drunk].move(xDist,yDist)

def walk(field, drunk, num_steps):
    start = field.get_loc(drunk)
    for s in range(num_steps):
        field.move_drunk(drunk)
    return start.dist_from(field.get_loc(drunk))

def simwalk(num_steps, num_trials, dClass):
    homer = dClass()
    distances = []
    origin = location(0, 0)
    for l in range(num_trials):
        f = field()
        f.add_drunk(homer, origin)
        distances.append(round(walk(f, homer, num_steps), 1))
    return distances

def drunk_test(walk_lengths,num_trials, dClass):
    for num_steps in walk_lengths:
        distances = simwalk(num_steps, num_trials, dClass)
        print(dClass.__name__, 'random walk of', num_steps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances),', Min =', min(distances))

random.seed(0)  
# drunk_test((10, 100, 1000, 10000), 100, usual_drunk)

#output - 
# usual_drunk random walk of 0 steps
#  Mean = 0.0
#  Max = 0.0 , Min = 0.0
# usual_drunk random walk of 1 steps
#  Mean = 1.0
#  Max = 1.0 , Min = 1.0
# usual_drunk random walk of 2 steps
#  Mean = 1.218
#  Max = 2.0 , Min = 0.0
# usual_drunk random walk of 10 steps
#  Mean = 2.863
#  Max = 7.2 , Min = 0.0
# usual_drunk random walk of 100 steps
#  Mean = 8.296
#  Max = 21.6 , Min = 1.4
# usual_drunk random walk of 1000 steps
#  Mean = 27.297
#  Max = 66.3 , Min = 4.2
# usual_drunk random walk of 10000 steps
#  Mean = 89.241
#  Max = 226.5 , Min = 10.0

def oddField(field):
    def __init__(self,  num_holes, xRange, yRange):
        field.__init__(self)
        self.wormholes = {}
        for w in range(num_holes):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            new_location = location(newX, newY)
            self.wormholes[(x, y)] = new_location
    
    def move_drunk(self, drunk):
        field.move_drunk(self, drunk):
        x = self.drunks[drunk].getX
        y = self.drunks[drunk].getY
        if (x,y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]

class style_iterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
    def next_style(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result