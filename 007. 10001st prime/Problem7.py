##Written by Gene Der Su at 7/27/2015
##Python verson 2.7.6
import time

initialTime = time.time()

maxNumber = 10001
primeList=[2]
i=3
while (len(primeList) < maxNumber):
    check=0
    for j in range(len(primeList)-1):
        if (i%primeList[j]==0):
            check=1
            break
    if (check == 0):
        primeList.append(i)
    i+=2

print time.time()-initialTime
print primeList[len(primeList)-1]

