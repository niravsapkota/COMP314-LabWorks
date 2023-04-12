from random import sample
import time
import matplotlib.pyplot as plt
from search import linearSearch, binarySearch

def benchLinear(n):
    data=sample(range(1,n+1), n)

    startTime=time.time()
    linearSearch(data, data[-1])
    endTime=time.time()

    timeTaken=endTime-startTime
    return timeTaken

def plotLinear():
    xCor = []
    yCor = []
    for i in range(10000, 100000, 10000):
        xCor.append(i)
        yCor.append(benchLinear(i))

    plt.plot(xCor, yCor)
    plt.title("Linear Search")
    plt.xlabel("Number of Data ( n )")
    plt.ylabel("Time taken  ( t )")
    plt.show()

plotLinear()

def benchBinary(n):
    data=sample(range(1,n+1), n)
    dataSize=len(data)

    startTime=time.time()
    binarySearch(data, 0, dataSize-1, data[-1])
    endTime=time.time()

    timeTaken=endTime-startTime
    return timeTaken

def plotBinary():
    xCor = []
    yCor = []
    for i in range(10000, 1000000, 10000):
        xCor.append(i)
        yCor.append(benchBinary(i))

    plt.plot(xCor, yCor)
    plt.title("Binary Search")
    plt.xlabel("Number of Data ( n )")
    plt.ylabel("Time taken  ( t )")
    plt.show()

plotBinary()