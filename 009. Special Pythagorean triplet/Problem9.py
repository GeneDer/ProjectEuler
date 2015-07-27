##Written by Gene Der Su at 7/27/2015
##Python verson 2.7.6
import time
import math

initialTime = time.time()

maxNumber=1000
for a in range(maxNumber/3):
    for b in range(a,maxNumber/2):
        c = math.sqrt(a**2 + b**2)
        if (c%1==0):
            c=int(c)
            if (a + b + c == maxNumber):
                print a*b*c
        
print time.time()-initialTime


