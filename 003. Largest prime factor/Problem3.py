##Written by Gene Der Su at 7/24/2015
##Python version 2.7.6

belowNumber=600851475143
i=2
while i < belowNumber:
    if (belowNumber%i==0):
        belowNumber=belowNumber/i
    else:
        i+=1
        
print belowNumber


