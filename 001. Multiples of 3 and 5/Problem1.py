##Written by Gene Der Su at 7/24/2015
##Python version 2.7.6

belowNumber=1000
sumNumber=0
for i in range(belowNumber):
    if ((i%3==0)|(i%5==0)):
        sumNumber+=i
print sumNumber



