##Written by Gene Der Su at 7/27/2015
##Python verson 2.7.6

maxNumber = 100
sumNumber = 0
squareSum = 0

for i in range(1,maxNumber+1):
    sumNumber+=i
    squareSum+=pow(i,2)

print abs(pow(sumNumber,2)-squareSum)
