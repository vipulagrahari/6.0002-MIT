import pylab
import random
import numpy


def getBMData(filename):
    data = {}
    data['name'], data['gender'], data['age'] = [], [], []
    data['division'], data['country'], data['time'] = [], [], []

    with open(filename, 'r') as infile:
        for line in infile:
            split = line.split(',')
            data['name'].append(split[0])
            data['gender'].append(split[1])
            data['age'].append(int(split[2]))
            data['division'].append(int(split[3]))
            data['country'].append(split[4])
            data['time'].append(float(split[5][:-1]))

    return data


def makeHist(data, bins, title, xLabel, yLabel):
    pylab.hist(data, bins)
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    mean = sum(data) / len(data)
    sDev = numpy.std(mean)
    pylab.annotate('Mean = {0} \n SD = {1}'.format(str(round(mean, 2)), str(round(sDev, 2))), fontsize=20, xy=(0.65, 0.75),
                   xycoords='axes fraction')
    pylab.show()

times = getBMData("samples.txt")['time']
# makeHist(times, 20, '2012 Boston Marathon','Minutes to Complete Race', 'Number of Runners')

def sample_times(times, numExamples):
    sample = random.sample(times, numExamples)
    makeHist(sample, 10, 'sample of size', str(numExamples), 'minutes to complete', "number of runners")

sampleSize = 40
sample_times(times, sampleSize)