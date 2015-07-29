##Written by Gene Der Su at 7/29/2015
##Python verson 2.7.6

import time

initialTime = time.time()

maxNumber=1000
digits = str(2**maxNumber)
sumOfDigits=0
for i in digits:
    sumOfDigits += int(i)

print time.time()-initialTime
print sumOfDigits
