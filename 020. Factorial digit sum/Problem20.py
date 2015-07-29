##Written by Gene Der Su at 7/29/2015
##Python verson 2.7.6

import math
import time

initialTime = time.time()

number = str(math.factorial(100))
sumDigits=0
for i in number:
    sumDigits+=int(i)
            
print time.time()-initialTime
print sumDigits
