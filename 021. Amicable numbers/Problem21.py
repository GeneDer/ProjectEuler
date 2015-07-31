##Written by Gene Der Su at 7/29/2015
##Python verson 2.7.6
##Modifided after reading the forum

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
maxNumber = 10000
amicable=set()

for i in range(2,maxNumber):
    if i not in amicable:
        tmpNumber1=sumOfProperDivisors(i)
        if (tmpNumber1!=i):
            tmpNumber2=sumOfProperDivisors(tmpNumber1)
            if (i==tmpNumber2):
                amicable.add(tmpNumber1)
                amicable.add(tmpNumber2)
                
amicableSum=sum(amicable)
print time.time()-initialTime
print amicableSum
