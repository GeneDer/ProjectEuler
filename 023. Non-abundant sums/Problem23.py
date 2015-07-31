##Written by Gene Der Su at 7/30/2015
##Python verson 2.7.6
##Found a bug in my sumOfProperDivisors() and fixed it.
##For some reason, the same algorithm impleneted in c++
##only took 2.5 seconds to run where as in python it took 11 seconds.
##Definitely have room for improvements. 

import time
import math

def sumOfProperDivisors(n):
    divieorSum = 1
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i==0):
            divieorSum+=i
            tempNumber=n/i
            if (tempNumber!=i):
                divieorSum+=tempNumber
    return divieorSum
    

initialTime = time.time()

maxNumber = 28123
nonAbundantSet=set(range(2,maxNumber+1))
abundantSet=[]

for i in range(12,maxNumber+1):
    if (sumOfProperDivisors(i)>i):
##        nonAbundantSet.remove(i)
        abundantSet.append(i)

for i in range(len(abundantSet)):
    for j in range(i,len(abundantSet)):
        twoAbundant = abundantSet[i] + abundantSet[j]
        if twoAbundant in nonAbundantSet:
            nonAbundantSet.remove(twoAbundant)
                
nonAbundantSetSum=sum(nonAbundantSet)+1

print time.time()-initialTime
print nonAbundantSetSum
