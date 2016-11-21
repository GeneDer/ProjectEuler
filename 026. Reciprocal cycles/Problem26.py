##Written by Gene Der Su at 11/21/2016
##Python verson 2.7.12

import time
import math

m = 1000

def get_length(n):
    # this part came from https://oeis.org/A051626
    lpow=1
    while True:
        for mpow in range(lpow-1, -1, -1):
            if (10**lpow-10**mpow) % n == 0:
                return lpow-mpow
        lpow += 1



initialTime = time.time()

max_num = 2
max_length = 0
for i in xrange(3,m):
    if i%2 != 0 and i%3 != 0 and i%5 != 0:
        i_length = get_length(i)
        if i_length > max_length:
            max_length = i_length
            max_num = i

print time.time()-initialTime
print max_num, max_length
