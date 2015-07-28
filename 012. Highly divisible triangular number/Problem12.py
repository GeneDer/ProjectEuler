##Written by Gene Der Su at 7/28/2015
##Python verson 2.7.6
##using divisor function to find number of divisor
##source: https://en.wikipedia.org/wiki/Divisor_function

import math
import time

initialTime = time.time()

def constructPrimeList(initial, final, primeList):
    for i in range(initial, final):
        primeList.append(True)
        
    loopLimit=int(math.ceil(math.sqrt(final)))

    for i in range(initial,loopLimit):
        if primeList[i]:
            for j in range(i**2,final,i):
                primeList[j]=False
    
    return primeList

def divisor(numberToCheck, primeList):
    numberOfDivisor=1
    for i in range(2,len(primeList)):
        if primeList[i]&(numberToCheck%i==0):
            counter=1
            while (numberToCheck%i==0):
                numberToCheck/=i
                counter+=1
            numberOfDivisor*=counter

    return numberOfDivisor 

minNumber=500
numberOfDivisor=0
currentCheck=1
count=1
primeList=[False, False]
primeList = constructPrimeList(2, minNumber*2, primeList)
while (numberOfDivisor < minNumber):
    count+=1
    currentCheck+=count
    numberOfDivisor = divisor(currentCheck, primeList)
    
print time.time()-initialTime
print currentCheck
