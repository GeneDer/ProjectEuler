##Written by Gene Der Su at 7/28/2015
##Python verson 2.7.6
##using divisor function to find number of divisor
##source: https://en.wikipedia.org/wiki/Divisor_function

import time

initialTime = time.time()

maxNumber=10
with open('numbers.txt','r') as i:
    lines = i.readlines()

sumNumber=0
for line in lines:
    sumNumber+=int(line)
    
print time.time()-initialTime
print str(sumNumber)[0:maxNumber]
