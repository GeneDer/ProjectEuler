##Written by Gene Der Su at 7/27/2015
##Python verson 2.7.6
##Using the sieve of Eratosthenes method
##Source: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_and_variants

import math
import time

initialTime = time.time()

maxNumber = 2000000
primeList=[True]*maxNumber
loopLimit=int(math.ceil(math.sqrt(maxNumber)))

for i in range(2,loopLimit):
    if primeList[i]:
        for j in range(i**2,maxNumber,i):
            primeList[j]=False
primeSum=0
for i in range(2,len(primeList)):
    if primeList[i]:
        primeSum+=i
 
print time.time()-initialTime
print primeSum

