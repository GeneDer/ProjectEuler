##Written by Gene Der Su at 7/29/2015
##Python verson 2.7.6

import time

initialTime = time.time()

year=1900
week=1

if (year%4==0):
    week+=366
    if ((year%100==0)&(year%400!=0)):
        week-=1
else:
    week+=365
year+=1
week=week%7

numberOfFirstSunday=0
while (year<2001):
    for i in range(1,13):
        if ((i==4)|(i==6)|(i==9)|(i==11)):
            week=(week+30)%7
        elif (i==2):
            ##knowing that 2000 is the only centry in the period and it is a
            ##lear year, so skip the check for divisible by 400
            if (year%4==0):
                week=(week+29)%7
            else:
                week=(week+28)%7
        else:
            week=(week+31)%7
        if (week==0):
            numberOfFirstSunday+=1
    year+=1
            
print time.time()-initialTime
print numberOfFirstSunday
