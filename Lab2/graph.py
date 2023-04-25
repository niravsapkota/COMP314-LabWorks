import random
import time
import matplotlib.pyplot as plt
from main import insertionSort, mergeSort

def perfInsertion(n):
    data=random.sample(range(1,n+1),n)
    startTime=time.time()
    insertionSort(data)
    endTime=time.time()

    timeTaken=endTime-startTime
    return timeTaken

def plotInsertion():
    xCor = []
    yCor = []
    for i in range(1000,10000,1000):
        xCor.append(i)
        yCor.append(perfInsertion(i))

    plt.plot(xCor, yCor)
    plt.title("Insertion Sort")
    plt.xlabel("Number of Data ( n )")
    plt.ylabel("Time taken  ( t )")
    plt.show()

plotInsertion()

def perfMerge(n):
    data=random.sample(range(1,n+1),n)
    startTime=time.time()
    mergeSort(data,0,len(data)-1)
    endTime=time.time()

    timeTaken=endTime-startTime
    return timeTaken

def plotMerge():
    xCor = []
    yCor = []
    for i in range(10000,100000,10000):
        xCor.append(i)
        yCor.append(perfMerge(i))

    plt.plot(xCor, yCor)
    plt.title("Merge Sort")
    plt.xlabel("Number of Data ( n )")
    plt.ylabel("Time taken  ( t )")
    plt.show()

plotMerge()
