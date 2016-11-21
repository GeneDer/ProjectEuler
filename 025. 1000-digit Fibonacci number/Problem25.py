##Written by Gene Der Su at 11/21/2016
##Python verson 2.7.12

import time
import math

initialTime = time.time()

n = 1000

m = n-1
f0 = 1
f1 = 1
idx = 2
while math.log10(f1) <= m:
    tmp = f0 + f1
    f0 = f1
    f1 = tmp
    idx += 1

print time.time()-initialTime
print idx
