##Written by Gene Der Su at 7/24/2015
##Python version 2.7.6

belowNumber=4000000
sumNumber=2
fibonacci1=1
fibonacci2=2
while (fibonacci2<belowNumber):
    temp = fibonacci2
    fibonacci2 += fibonacci1
    fibonacci1 = temp
    if (fibonacci2%2==0):
        sumNumber+=fibonacci2
print sumNumber



